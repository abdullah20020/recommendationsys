from flask import Flask, jsonify, request
from model import train_model
from recommend import get_top_n_recommendations

app = Flask(__name__)
algo, trainset = train_model()

@app.route('/recommendations', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    if user_id is None:
        return jsonify({"error": "UserId is required!"}), 400


    predictions = algo.test(trainset.build_anti_testset())
    top_n = get_top_n_recommendations(predictions, n=5)
    user_recommendations = top_n.get(user_id, [])

    return jsonify({
        "user_id": user_id,
        "recommendations": user_recommendations  # دي عبارة عن List of Book IDs
    })
if __name__ == '__main__':
    app.run(debug=True)
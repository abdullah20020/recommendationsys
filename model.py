from surprise import KNNBasic, Dataset, Reader
from db import get_user_interests

def train_model():
    df = get_user_interests()
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['UserId', 'BookId', 'Rating']], reader)
    trainset = data.build_full_trainset()

    algo = KNNBasic(sim_options={'name': 'cosine', 'user_based': True})
    algo.fit(trainset)
  
    return algo, trainset
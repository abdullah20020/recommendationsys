from sqlalchemy import create_engine, text
import pandas as pd

def get_user_interests():
    try:
        connection_string = "mssql+pyodbc://localhost/Rawydbs?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
        engine = create_engine(connection_string)

        with engine.connect() as connection:
            result = connection.execute(text("SELECT UserId, BookId FROM UserInterests"))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())

        df['Rating'] = 1

        print(df.head())

        return df

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

get_user_interests()

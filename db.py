from sqlalchemy import create_engine
import pandas as pd


def get_user_interests():
    try:

        connection_string = "mssql+pyodbc://@./Rawydbs?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
        engine = create_engine(connection_string)
     
        df = pd.read_sql("SELECT UserId, BookId FROM UserInterests", engine)
        
        # إضافة عمود 'Rating' مع القيمة 1
        df['Rating'] = 1

        print(df.head())
        
        return df
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# تنفيذ الوظيفة لقراءة البيانات
get_user_interests()
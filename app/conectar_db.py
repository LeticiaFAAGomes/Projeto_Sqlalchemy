from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        engine = create_engine(os.getenv('LOGIN'))
        session = sessionmaker(bind=engine)()
        
        with open('app\\db\\script-mysql.sql', 'r') as sql:
            script_sql = sql.read().split(';')
            
        for comando in script_sql:
            if comando.strip():
                session.execute(text(comando))
                session.commit()
        
    except Exception as ex:
        print(ex)
        
    return session


def desconectar(session):
    if (session):
        session.close()
        
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def conectar():
    try:
        engine = create_engine("mysql+pymysql://root:root@localhost/infnet")
        session = sessionmaker(bind=engine)()
        
    except Exception as ex:
        print(ex)
        
    return session


def desconectar(session):
    if (session):
        session.close()
        
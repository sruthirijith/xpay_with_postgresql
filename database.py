from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:ivania2019@localhost:5432/xpay_new"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():    # to get all the tables in this database
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    print("create tables")
    Base.metadata.create_all(bind=engine)
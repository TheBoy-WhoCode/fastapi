from sqlalchemy import create_engine
from sqlalchemy.engine.create import engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHMEY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<database_name>"

SQLALCHMEY_DATABASE_URL = "postgresql://postgres:Elliot@localhost/fastapi"

engine = create_engine(SQLALCHMEY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

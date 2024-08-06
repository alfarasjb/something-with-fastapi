from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.definitions.credentials import EnvVariables, Credentials


# user: postgres
# password: admin
HOST = EnvVariables.db_host()
PORT = EnvVariables.db_port()
USERNAME = Credentials.db_username()
PASSWORD = Credentials.db_password()
DB_NAME = EnvVariables.db_name()
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    # connect_args={"check_same_thread": False}  # connect args is only needed for sqlite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

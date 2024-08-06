from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# user: postgres
# password: admin
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/TestDB"

engine = create_engine(
    DATABASE_URL,
    # connect_args={"check_same_thread": False}  # connect args is only needed for sqlite
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

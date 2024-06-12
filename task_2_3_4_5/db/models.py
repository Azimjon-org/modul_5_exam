

import datetime
import enum
from os import getenv

from dotenv import load_dotenv
from sqlalchemy import INT, BigInteger, VARCHAR, Boolean, TIMESTAMP, func, Integer, Enum, TEXT, DECIMAL, SMALLINT, \
    ForeignKey, Column, create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
load_dotenv()

engine = create_engine(f"postgresql+psycopg2://{getenv('DB_USER')}:{getenv('PASSWORD')}@{getenv('HOST')}/{getenv('DB_NAME')}",
                       echo=False)



class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


class CustomAbstarct(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.current_timestamp())
    updated_at: Mapped[datetime] = Column(TIMESTAMP, default=func.current_timestamp(),
                                          onupdate=func.current_timestamp())

class User(CustomAbstarct):
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str] = mapped_column(VARCHAR(255))
    last_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    phone_number: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)

    def __repr__(self):
        return self.first_name

Base.metadata.create_all(engine)
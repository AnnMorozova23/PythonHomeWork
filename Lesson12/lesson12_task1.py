from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    ForeignKey,
    TIMESTAMP,
    TEXT,
    create_engine,
    CheckConstraint,
    select,
    update,
    delete,
    and_,
    any_,
    all_,
    or_
)

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, declared_attr, Session


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)
    engine = create_engine('postgresql://annaalchemy:password@127.0.0.1:5432/alchemydb')
    session = sessionmaker(bind=engine)


class Categories(Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(24), nullable=False, unique=True)

    products = relationship(argument='Products', back_populates='categories')


class Products(Base):
    __tablename__ = 'products'

    title = Column(VARCHAR(24), nullable=False, unique=True)
    description = Column(VARCHAR(124))
    category_id = Column(INT, ForeignKey(column='categories.id'), nullable=False)

    categories = relationship(argument=Categories, back_populates='products')


class Usres(Base):
    __tablename__ = 'users'

    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False, unique=True)


class Statuses(Base):
    __tablename__ = 'statuses'

    name = Column(VARCHAR(10), nullable=False)


class Orders(Base):
    __tablename__ = 'orders'

    user_id = Column(INT, ForeignKey(column='users.id'), nullable=False)
    status_id = Column(INT, ForeignKey(column='statuses.id'), nullable=False)


class OrderItems(Base):
    __tablename__ = 'order_items'

    id = Column(INT, primary_key=True)
    order_id = Column(INT, ForeignKey(column='orders.id'), nullable=False)
    product_id = Column(INT, ForeignKey(column='products.id'), nullable=False)


Base.metadata.drop_all(bind=Base.engine)
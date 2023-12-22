from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text, Time
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://postgres:marichka1104@localhost:5432/postgres')

class Author(Base):
    __tablename__ = 'Author'

    Login = Column(String, primary_key=True)
    Name = Column(String, nullable=False)
    Password = Column(String, nullable=False)
    recipes = relationship('Recipe', back_populates='author')


class Recipe(Base):
    __tablename__ = 'Recipe'

    Recipe_ID = Column(String, primary_key=True)
    Author_login = Column(String, ForeignKey('Author.Login'))
    Name = Column(String, nullable=False)
    Calories = Column(Integer)
    Time = Column(Time)
    Photos = Column(Text)
    Steps = Column(Text, nullable=False)

    author = relationship('Author', back_populates='recipes')
    includes = relationship('Includes', back_populates='recipe')
    consists = relationship('Consists', back_populates='recipe')


class Ingredients(Base):
    __tablename__ = 'Ingredients'

    Ingredients_ID = Column(String, primary_key=True)
    Name = Column(String, nullable=False)
    consists = relationship('Consists', back_populates='ingredient')


class Category(Base):
    __tablename__ = 'Category'

    Category_ID = Column(String, primary_key=True)
    Difficulty = Column(String)
    Type = Column(String, nullable=False)
    Country = Column(String)
    includes = relationship('Includes', back_populates='category')


class Includes(Base):
    __tablename__ = 'Includes'

    Category_FK = Column(String, ForeignKey('Category.Category_ID'), primary_key=True)
    Recipe_FK = Column(String, ForeignKey('Recipe.Recipe_ID'), primary_key=True)

    recipe = relationship('Recipe', back_populates='includes')
    category = relationship('Category', back_populates='includes')


class Consists(Base):
    __tablename__ = 'Consists'

    Recipe_FK = Column(String, ForeignKey('Recipe.Recipe_ID'), primary_key=True)
    Ingredients_FK = Column(String, ForeignKey('Ingredients.Ingredients_ID'), primary_key=True)
    Amount = Column(Integer, nullable=False)
    Measurement_unit = Column(String, nullable=False)
    Temperature = Column(Integer)

    recipe = relationship('Recipe', back_populates='consists')
    ingredient = relationship('Ingredients', back_populates='consists')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()

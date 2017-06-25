"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# An instance method


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter_by(brand_id='ram').one()
# q1 = db.session.query(Brand).filter(Brand.brand_id == 'ram').one()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = db.session.query(Model).filter(Model.name == 'Corvette', Model.brand_id == 'che').all()

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = db.session.query(Model).filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = None

# Get all models whose brand_id is not ``for``.
q8 = None



# -------------------------------------------------------------------
# Part 4: Write Functions

def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_info_by_year = db.session.query(Model).join(Brand).filter(Model.year == year).all()
    print "\nInformation regarding models from {}:\n".format(year)
    for model in model_info_by_year:
        print model.name + '\n' + model.brand.name + '\n' + model.brand.headquarters + '\n'


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brands = db.session.query(Brand).join(Model).distinct().all()
    print "\nSummary of models by brand:\n"
    for brand in brands:
        print '\n' + brand.name + ' - '
        for model in brand.models:
            print str(model.year) + '\t' + model.name


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    pass


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    pass


import model
from sqlalchemy import orm
from sqlalchemy import create_engine

#create the engine
#TODO - get the url for db from .ini file
engine = create_engine('postgresql://ckan_default:pass@localhost/ckan_default', echo=True)
model.metadata.bind = engine
model.metadata.create_all()

# Set up the session
sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False,
    expire_on_commit=True)
session = orm.scoped_session(sm)
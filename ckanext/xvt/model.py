from sqlalchemy import Table, Column, types
from sqlalchemy import orm
from sqlalchemy import schema, types

from ckan.model.meta import metadata

alpha_table = Table('alpha', metadata,
                        Column('id', types.Integer, primary_key=True),
                        Column('title', types.UnicodeText, default=u''),
                       )
class Alpha(object):
    pass

#map the Alpha class to the alpha table
orm.mapper(Alpha, alpha_table)


#example of adding a record to the alpha table
def add_record():
    from object_test import session

    #create Alpha object
    test_alpha = Alpha()

    #add data to fields
    test_alpha.id = '1'
    test_alpha.title = 'this is the first entry'

    #add the Alpha object to the session
    session.add(test_alpha)

    #send to database
    session.flush()

    #commit the change
    session.commit()


# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

from oik_const import DBPATH


class Params(object):
    pass


#----------------------------------------------------------------------
def loadSession():
    """"""
    engine = create_engine('postgresql://%s' % DBPATH, echo=False)

    metadata = MetaData(engine)
    params = Table('params', metadata, autoload=True)
    mapper(Params, params)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == "__main__":
    session = loadSession()
    for prm in session.query(Params).all():
        print('{} -> {}'.format(prm.prmname, prm.last_value))

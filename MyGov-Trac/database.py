from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# MySQL Connection
MYSQL_USER 		= 'root'
MYSQL_PASSWORD 	= 'Mharooney'
MYSQL_HOST_IP 	= '127.0.0.1'
MYSQL_PORT		= 3306
MYSQL_DATABASE	= 'gov_tracker_db'

engine = create_engine('mysql+mysqlconnector://'+MYSQL_USER+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST_IP+':'+str(MYSQL_PORT)+'/'+MYSQL_DATABASE, echo=False)


db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker, ColumnProperty
from sqlalchemy.schema import Column, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.types import Boolean, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

Base = declarative_base()

class TimestampMixin(object):
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=True, default=None)
    deleted_at = Column(DateTime, nullable=True, default=None)
    

class GalleryInfo(TimestampMixin, Base):
    __tablename__ ="gallery_info"
    
    g_id = Column(String, primary_key=True)
    g_token = Column(String, primary_key=True)
    g_hash = ColumnProperty(g_id + "_" + g_token)

    title = Column(String)
    title_jp = Column(String)
    title_cleaned = Column(String)
    posted_at = Column(DateTime, default=datetime.utcnow, unique=True)
    posted_by = Column(String)
    category = Column(String)
    language = Column(String)
    is_translated = Column(Boolean)
    is_visible = Column(Boolean)
    is_expunged = Column(Boolean)
    reason = Column(String, nullable=True)
    nb_pages = Column(Integer)
    file_size = Column(String)
    parent_gid = Column(String)
    id_favorited = Column(Boolean, default=True)
    favorite_category= Column(String)
    my_rating = Column(Float)







class Main:

    @staticmethod
    def run():
        #   INSERT
        if not session.query(exists().where(GalleryInfo.g_hash == '123_abc456')).scalar():
            g1 = GalleryInfo(title="[Hajime Isayama] Shingeki no Kyojin | Attack on Titan", title_jp="進撃の巨人", g_id="123", g_token="abc456")
            g1.my_rating = 4.5
            g1.language = "English"
            g1.is_translated = True
            g.category = "Manga"

            # g1.address = a1
            # session.add(a1)
            session.add(g1)
            session.commit()
        else:
            print("Already in : G#123_abc456")

        #print session.query(GalleryInfo).filter_by(language='English').count()
        #print bool( session.query(GalleryInfo).filter_by(language='English').count())

        #   SELECT
        if session.query(exists().where(GalleryInfo.language == 'English')).scalar():
            g2 = session.query(GalleryInfo).filter_by(language='English').first()
            print(g2.title)






if __name__ == '__main__':
    # database_uri = 'mysql+pymysql://user:pwd@localhost:3306/test'
    database_uri = 'sqlite:///tmp/db.sqlite3'
    engine = create_engine(database_uri, echo=False)
    
    Base.metadata.create_all(engine)

    connection = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    Main.run()

    connection.close()




    
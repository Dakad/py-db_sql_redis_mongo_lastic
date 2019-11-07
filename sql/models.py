from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker, ColumnProperty
from sqlalchemy.schema import Column, ForeignKey, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.types import Boolean, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

Base = declarative_base()

class TimestampMixin(object):
    created_at = Column(DateTime, unique=True, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True, default=None)
    deleted_at = Column(DateTime, nullable=True, default=None)
    

class GalleryInfo(Base, TimestampMixin):
    __tablename__ ="gallery_infos"

    g_hash = Column(String, primary_key=True)

    g_id = Column(String, nullable=False)
    g_token = Column(String, nullable=False)

    title = Column(String)
    title_jp = Column(String)
    title_cleaned = Column(String)
    posted_at = Column(DateTime, default=datetime.utcnow, unique=True)
    posted_by = Column(String)
    category = Column(String)
    language = Column(String)
    is_translated = Column(Boolean, default=False)
    is_visible = Column(Boolean, default=True)
    is_expunged = Column(Boolean, default=False)
    reason = Column(String, nullable=True)
    nb_pages = Column(Integer)
    file_size = Column(String)
    parent_gid = Column(String)
    is_favorited = Column(Boolean, default=True)
    favorite_category= Column(String)
    my_rating = Column(Float)

    thumbnail_link = relationship('GalleryThumbnail', backref="gallery_infos", uselist=False)


    def __init__(self, **kwargs):
        for (var_name, var_val) in kwargs.items():
            setattr(self, var_name, var_val)
        self.g_hash = GalleryInfo.generate_hash(
            kwargs.get("g_id"), 
            kwargs.get("g_token")
        )

    @staticmethod
    def generate_hash(g_id, g_token, separator="_"):
        return "{}{}{}".format(g_id, separator, g_token)


class GalleryThumbnail(Base, TimestampMixin):
    __tablename__ = "gallery_thumbnails"
    
    g_hash = Column(Integer, ForeignKey(GalleryInfo.g_hash), primary_key=True)
    thumb_link = Column(String, nullable=False)



    





class Main:

    @staticmethod
    def run():

        #   INSERT
        if not session.query(exists().where(GalleryInfo.g_hash == '123_abc456')).scalar():
            g1_id = "123"
            g1_token = "abc456"
            # g1_hash = GalleryInfo.generate_hash(g1_id, g1_token)
            g1 = GalleryInfo(title="[Hajime Isayama] Shingeki no Kyojin | Attack on Titan", title_jp="進撃の巨人", g_id="123", g_token=g1_token)
            g1.posted_at = datetime(2016, 1, 1)
            g1.my_rating = 4.5
            g1.language = "English"
            g1.is_translated = True
            g1.category = "manga"

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
            print(g2.g_hash, g2.title)






if __name__ == '__main__':
    # database_uri = 'mysql+pymysql://user:pwd@localhost:3306/test'
    database_uri = 'sqlite:///tmp/db.sqlite3'
    engine = create_engine(database_uri, echo=False)
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    connection = engine.connect()
    Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    session = Session()

    Main.run()

    connection.close()




    

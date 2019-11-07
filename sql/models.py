from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker, ColumnProperty
from sqlalchemy.schema import Column, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.types import Boolean, DateTime, Float, Integer, String
from sqlalchemy.ext import declarative_base

from datetime import datetime

Base = declarative_base()

class TimestampMixin(object):
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=True, default=None)
    deleted_at = Column(DateTime, nullable=True, default=None)
    

class GalleryInfo(TimestampMixin, Base):
    __tablename__ ="gallery_info"
    
    g_id = Column(String, primary_key=true)
    g_token = Column(String, primary_key=true)
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
    my_ratings = Column(Float)
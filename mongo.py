from mongoengine import StringField, ListField, FloatField, BooleanField, DateTimeField

from datetime import datetime



class GalleryTags(Document):
    gallery_hash = StringField(required=True, unique=True)
    artist = ListField(default=None)
    group = ListField(default=None)
    male = ListField(default=None)
    female = ListField(default=None)
    misc = ListField(default=None)
    language = ListField(default=None)
    characters = ListField(default=None)
    reclass = StringField(default=None)
    language = ListField(default=None)

    created_at = DateTimeField(default=datetime.utcnow)
    last_fetched = DateTimeField()

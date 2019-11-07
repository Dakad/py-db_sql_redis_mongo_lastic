from mongoengine import StringField, ListField, FloatField, BooleanField, DateTimeField

from datetime import datetime



class GalleryTags(Document):
    gallery_hash = StringField(required=True, unique=True)
    artist = ListField()
    group = ListField(default=[])
    signed_in = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)
    last_fetched = DateTimeField()

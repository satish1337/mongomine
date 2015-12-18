from mongoengine import *
from django.conf import settings

connect(settings.MONGO_DATABASE_NAME, host=settings.MONGO_HOST, port=settings.MONGO_PORT)

class Candidate(DynamicDocument):
    """
    Document to store candidate in mongo
    """
    meta = {'collection': 'candidate'}
    uid = StringField()
    name = StringField()
    bio = StringField()
    location = StringField()
    designation = StringField()
    created_at = StringField()
    updated_at = DateTimeField()

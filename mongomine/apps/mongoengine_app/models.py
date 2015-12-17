from mongoengine import *

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

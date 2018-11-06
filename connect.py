from mongoengine import *
import pymongo
from pymongo import MongoClient
from pprint import pprint


#connect('sushi', username='sushi', password='shushi1122QAZxsw', authentication_source='sushi')
#client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.sushi

collection = db.object_output

cursor = collection.find({"image": "5bdbd71e38802c59e0afa93a"}, {"bbox": 1, "classes": 1})

for i in cursor:
	pprint(i)


#mycursor = db.sushi.find({})

# class Support(Document):
	"""docstring for Support"""
	

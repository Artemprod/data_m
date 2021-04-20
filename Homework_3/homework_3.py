from pymongo import MongoClient
import pickle
from pprint import pprint



def open_doc(path):
    with open(path, 'rb') as f:
        doc = pickle.load(f)
        return doc

def insert_data(collectio_name, file_name):
    data = collectio_name.insert_many(file_name)
    return data

def find_all_data(collection_name):
    data = collection_name.find({})
    return data

def find_particular_salary(collection_name, salary):
    result = collection_name.find({
        'min salary': {'$gt': salary}

    })
    return result


file_path = 'Product_vacansy_json.json'
mongo_db = 'vacansy'
client = MongoClient('localhost', 27017)


with MongoClient('localhost', 27017) as client:
    db = client[mongo_db]
    collection = db['product_manager']
    file = open_doc(file_path)
    data_insert = insert_data(collection, file)
    neded_salary = find_particular_salary(collection, 1000)
    for item in neded_salary.sort('max salary', -1):
        print(item)





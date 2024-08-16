from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        #
        # Connection Variables
        #
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32206
        DB = 'AAC'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]

# Method takes data as argument and inserts into AAC database
    def create(self, data): # data should be dictionary
        if data is not None:
            success = self.database.animals.insert_one(data)  
            if success != 0:
                return True
            else:
                return False
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Method takes search query as argument and prints list of matching results
    def read(self, search): # search should be dictionary
        if search is not None:
            data = self.database.animals.find(search) 
            results = list(data)
            if len(results) == 0:
                print("No results found")
            else:
                i = 1
                for result in results:
                    print("{}. {}\n".format(i, result))
                    i += 1
        else:
            raise Exception("Nothing to read, because search parameter is empty")
        

# Method takes criteria for initial search and new data to update and prints the number of documents modified
    def update(self, criteria, newData): # criteria and newData should both be dictionaries
        if criteria is not None:
            if self.database.animals.count_documents(criteria, limit = 1) != 0: # ensures at least one record matches
                update = self.database.animals.update_many(criteria, {"$set": newData})
                print(update.modified_count, "results updated.")
            else:
                print("No results with matching criteria")
        else:
            raise Exception("Nothing to update, because criteria parameter is empty")
# Method takes criteria for search and prints the number of documents deleted            
    def delete(self, criteria): # criteria should be dictionary
        if criteria is not None:
            if self.database.animals.count_documents(criteria, limit = 1) != 0: #ensures at least one record matchs
                delete = self.database.animals.delete_many(criteria) 
                print(delete.deleted_count, "results deleted.")
            else:
                print("No results with matching criteria")
        else:
            raise Exception("Nothing to delete, because criteria parameter is empty")
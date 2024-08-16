################################################################
# CRUD.py                                                      #
#                                                              #
# Contains the backend logic for querying the MongoDB database #
################################################################

from pymongo import MongoClient
from bson.objectid import ObjectId


class CourseCatalog(object):
    """ CRUD operations for course catalog in MongoDB """

    def __init__(self, USER, PASS):
        HOST = 'localhost'
        PORT = 27017
        DB = 'catalog'

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]

    
    def create(self, data): # data should be dictionary
        if data is not None:
            success = self.database.courses.insert_one(data)  
            if success != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    
    def createStudentAccount(self, data): # data should be dictionary
        if data is not None:
            success = self.database.students.insert_one(data)
            if success != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
        
    # Method takes search query as argument and prints list of matching results
    def readCourse(self, search): # search should be dictionary
        if search is not None:
            data = self.database.courses.find(search).sort({'Acad Group':1, 'Subject Code':1, 'Course Nbr':1}) 
            results = list(data)
            return results
            if len(results) == 0:
                print("No results found")
            else:
                i = 1
                for result in results:
                    print("{}. {}\n".format(i, result))
                    i += 1
        else:
            raise Exception("Nothing to read, because search parameter is empty")

    
    def readStudent(self, search):
        if search is not None:
            data = self.database.students.find(search) 
            results = list(data)
            if len(results) == 0:
                print("No results found")
            else:
                i = 1
                for result in results:
                    print("{}. {}\n".format(i, result))
                    i += 1
            return results
        else:
            raise Exception("Nothing to read, because search parameter is empty")
        

# Method takes criteria for initial search and new data to update and prints the number of documents modified
    def update(self, criteria, newData): # criteria and newData should both be dictionaries
        if criteria is not None:
            if self.database.courses.count_documents(criteria, limit = 1) != 0: # ensures at least one record matches
                update = self.database.courses.update_many(criteria, {"$set": newData})
                print(update.modified_count, "results updated.")
            else:
                print("No results with matching criteria")
        else:
            raise Exception("Nothing to update, because criteria parameter is empty

                            
# Method takes criteria for search and prints the number of documents deleted            
    def delete(self, criteria): # criteria should be dictionary
        if criteria is not None:
            if self.database.courses.count_documents(criteria, limit = 1) != 0: #ensures at least one record matchs
                delete = self.database.courses.delete_many(criteria) 
                print(delete.deleted_count, "results deleted.")
            else:
                print("No results with matching criteria")
        else:
            raise Exception("Nothing to delete, because criteria parameter is empty")

    
# Verifies the existence of a given student
    def studentVerify(self, first, last, studentId):
        if self.database.students.count_documents({"First Name" : first, "Last Name": last, "Student ID": studentId}) != 0:
            return True
        else:
            return False

    
# Registers student with ID: {studentId} to a course
    def register(self, criteria, studentId):
        update = self.database.courses.update_many(criteria, {'$push': {'registered':studentId}})
        print(update.modified_count, "results updated.")

    
# Deregisters student with ID: {studentId} from a course  
    def deregister(self, criteria, studentId):
        update = self.database.courses.update_many(criteria, {'$pull': {'registered':studentId}})
        print(update.modified_count, "results updated.")

    
# Checks to see whether a given student with ID: {studentId} is registered for course {subjectCode}-{courseNbr}
    def verifyRegistration(self, courseNbr, subjectCode, studentId):
        if self.database.courses.count_documents({"Subject Code":subjectCode, "Course Nbr":courseNbr, "registered": {"$in": [studentId]}}) != 0:
            return True
        else:
            return False

## Dat 6th - MONGo DB

from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv () # load environment variables from .env file

mongo_uri = os.getenv ('MONGODB_ATLAS_CLUSTER_URI')

class DatabaseManager:
    def __init__(self, db_name = 'expmongo_db', connection_string=mongo_uri):
        self.client  = MongoClient (connection_string)
        self.db = self.client [db_name]
        self.users_collection = self.db.users
        self.posts_collection = self.db.posts
        self.init_database ()

    def init_database (self):
        """Initialize database with collections and indexes"""

        # Create unique index on email for users
        self.users_collection.create_index ("email", unique=True)

        # Create index on user_id for posts for better query performance
        self.posts_collection.create_index ("user_id")
    
    # Create Function

    def create_user (self, name, email, age):
        """ Create a New User"""
        try:
            user_doc = {
                "name": name,
                "email": email,
                "age": age,
                "created_at": datetime.now ()
            }
            result = self.users_collection.insert_one (user_doc)
            return str (result.inserted_id)
        except Exception as e:
            print (f"Error: {e}")
            return None
        
    def create_post (self, user_id, title, content):
        """ Create a New Post"""
        try:
            # convert string user_id to ObjectiIdif it's a valid ObjectId
            if ObjectId.is_valid (user_id):
                user_object_id = ObjectId (user_id)
            else:
                user_object_id = user_id
            
            post_doc = {
                "user_id": user_object_id,
                "title": title,
                "content": content,
                "created_at": datetime.now ()
            }
            result = self.posts_collection.insert_one (post_doc)
            return str (result.inserted_id)
        except Exception as e:
            print (f"Error Creating Post: {e}")
            return None
    
    # Read Function
        
    def get_all_users (self):
        """ Get all users """
        try:
            users =list (self.users_collection.find ())
            # Convert ObjectID to string for display
            for user in users:
                user ['_id'] = str (user ['_id'])
            return users
        except Exception as e:
            print (f"Error Fetching Users: {e}")
            return []
        
    def get_user_posts (self, user_id):
        """ get posts by user """
        try:
            # Convert string user_id to ObjectID if it's a valid ObjectID
            if ObjectId.is_valid (user_id):
                user_object_id = ObjectId (user_id)
            else:
                user_object_id = user_id
            
            posts =list (self.posts_collection.find (
                {"user_id": user_object_id}
            ).sort ("created_at", -1))

            # Convert ObjectId to string for display
            for post in posts:
                post ['_id'] = str (post ['_id'])
                post ['user_id'] = str (post ['user_id']) 
            return posts
        
        except Exception as e:
            print (f"Error Fetching Users: {e}")
            return []
    
    # Delete Function:

    def delete_user (self, user_id):
        """ Delete user and their posts """
        try:
            # Convert string user_id to ObjectId if's a valid ObjectId
            if ObjectId.is_valid (user_id):
                user_object_id = ObjectId (user_id)
            else:
                user_object_id = user_id

            # Delete user's posts first
            self.posts_collection.delete_many ({"user_id": user_object_id})

            # Delete the user
            result = self.users_collection.delete_one ({"_id": user_object_id})
            return result.deleted_count > 0
        except Exception as e:
            print (f"Error Deleting Users: {e}")
            return False
        
    # Close DB Function

    def close_connection (self):
        """ Close the MongoDB Connection """
        self.client.close ()

def display_menu ():
    """ display The Main Menu """
    print ("\n" + "="*40)
    print ("           DATABASE MANAGER")
    print ("="*40)
    print ("1. Create User")
    print ("2. View All Users")
    print ("3. create Post")
    print ("4. View user posts")
    print ("5. Delete User")
    print ("6. Exit")
    print ("="*40)
    
def main ():
    """ Main interactive CLI Function """
    try:
        db = DatabaseManager ()
        print ("Connected to MongoDB Successfully!")
    except Exception as e:
        print (f" Failed to Connect to MongoDB: {e}")
        print ("Make sure MangoDB is Running on localhost")
        return
        
    while True:
        display_menu ()
        choice = input ("Enter your Choice (1-6):").strip ()

        if choice == '1':
            print ("\n--- Create New user ---")
            name = input ("Enter Name:").strip ()
            email = input ("Enter Email:").strip ()
            try:
                age = int (input ("Enter Age:").strip ())
                user_id = db.create_user (name, email, age)
                if user_id:
                    print (f"User Created Successfully! ID: {user_id}")
                else:
                    print ("Failed to create user")
            except ValueError:
                print ("Invalid Age. Please enter a number")
        
        elif choice == '2':
            print ("\n --- All users ---")
            users = db.get_all_users ()
            if users:
                for user in users:
                    print (f"ID: {user['_id']} | Name: {user ['name']} | Email: {user['email']} | Age: {user['age']}")
                else:
                    print ("No User Found")
        
        elif choice == '3':
            print ("\n--- Create New post ---")
            user_id = input ("Enter User ID:").strip ()
            title = input ("Enter Post Title:").strip ()
            content = input ("Enter Post Content:").strip ()
            post_id = db.create_post (user_id, title, content)
            if post_id:
                print (f"Post Created Successfully, ID: {post_id}")
            else:
                print ("Failed to create post")
            
        elif choice == '4':
            print ("\n --- View User Posts ---")
            user_id = input ("Enter User ID:").strip ()
            posts = db.get_user_posts (user_id)
            if posts:
                for post in posts:
                    print (f"\n Post ID: {post['_id']}")
                    print (f"Title: {post['title']}")
                    print (f"Content: {post['content']}")
                    print (f"created: {post['created_at']}")
                    print ("-"*30)
            else:
                print ("No posts Found for This User")
  
        
        elif choice == '5':
            print ("\n --- Delete User ---")
            user_id = input ("Enter user ID to Delete:").strip()
            confirm = input (f"Are you sure want to delete user {user_id}? (y/N):").strip().lower()
            if confirm == 'y':
                if db.delete_user (user_id):
                    print ("User deleted Successfully!!!")
                else:
                    print ("User not Found or Deletion Failed.")
            else:
                    print ("Deletion Cancelled.")
            

        elif choice == '6':
            print ("\n Closing database Connection")
            db.close_connection ()
            print ("\n Goodbye!!!")
            break
           
        else:
            print ("Invalid Choice. Please Enter 1-6:")

        input ("\n Press Enter to Continue...")

if __name__ == "__main__":
    main ()

        



        
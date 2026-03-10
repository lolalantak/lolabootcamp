## Day 6 - SQ Lite

import sqlite3

class DatabaseManager:
    def __init__(self, db_name= 'Lola.db'):
        self.db_name = db_name
        self.init_database ()

    def init_database (self):
        """Initialize Database with Tables"""
        with sqlite3.connect (self.db_name) as conn:
            cursor = conn.cursor ()

            cursor.execute ('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            cursor.execute ('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
                
## Create Data (Insert)

    def create_user (self, name, email, age):
        try:
            with sqlite3.connect (self.db_name) as conn:
                cursor = conn.cursor ()
                cursor.execute ('''
                    INSERT INTO users (name, email, age)
                    VALUES (?, ?, ?)
                ''', (name, email, age))
                return cursor.lastrowid
            
        except sqlite3.IntegrityError as e:
            print (f"Error: {e}")
            return None
        
    def create_post (self, user_id, title, content):
        with sqlite3.connect (self.db_name) as conn:
            cursor = conn.cursor ()
            cursor.execute ('''
                INSERT INTO posts (user_id, title, content)
                VALUES (?, ?, ?)
            ''', (user_id,title, content))
            return cursor.lastrowid

## Read Data (Select)

    def get_all_users (self):
        with sqlite3.connect (self.db_name) as conn:
            cursor = conn.cursor ()
            cursor.execute ('SELECT * FROM users')
            return cursor.fetchall ()
    
    def get_user_posts (self, user_id):
        with sqlite3.connect (self.db_name) as conn:
            cursor = conn.cursor ()
            cursor.execute ('''
                SELECT p.id, p.title, p.content, p.created_at
                FROM posts p
                WHERE p.user_id = ?
                ORDER BY p.created_at DESC
            ''', (user_id,))
            return cursor.fetchall ()
        
## Delete Data (Delete)

    def delete_user (self, user_id):
        with sqlite3.connect (self.db_name) as conn:
            cursor =conn.cursor ()
            cursor.execute ('DELETE FROM posts WHERE user_id = ?', (user_id,))
            cursor.execute ('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount > 0

## Run On Terminal Function

def display_menu ():
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
    db = DatabaseManager ()

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
                        print (f"ID: {user[0]} | Name: {user [1]} | Email: {user[2]} | Age: {user[3]}")
                else:
                        print ("No User Found")
            
        elif choice == '3':
            print ("\n--- Create New post ---")
            try:
                user_id = int (input ("Enter User ID:").strip ())
                title = input ("Enter Post Title:").strip ()
                content = input ("Enter Post Content:").strip ()
                post_id = db.create_post (user_id, title, content)
                if post_id:
                    print (f"Post Created Successfully, ID: {post_id}")
                else:
                        print ("Failed to create post")
            except ValueError:
                    print ("Invalid user ID. Plase enter a Number.")

        elif choice == '4':
            print ("\n --- View User Posts ---")
            try:
                user_id = int (input ("Enter User ID:").strip ())
                posts = db.get_user_posts (user_id)
                if posts:
                    for post in posts:
                        print (f"\n Post ID: {post[0]}")
                        print (f"Title: {post[1]}")
                        print (f"Content: {post[2]}")
                        print (f"created: {post[3]}")
                        print ("-"*30)
                else:
                        print ("No posts Found for This User")
            except ValueError:
                    print ("Invalid user ID. Please enter a Number.")

        elif choice == '5':
            print ("\n --- Delete User ---")
            try:
                user_id = int (input ("Enter user ID to Delete:").strip())
                confirm = input (f"Are you sure want to delete user {user_id}? (Y/N):").strip().lower()
                if confirm == 'y':
                    if db.delete_user (user_id):
                        print ("User deleted Successfully!!!")
                    else:
                        print ("User not Found or Deletion Failed.")
                else:
                    print ("Deletion Cancelled.")
            except ValueError:
                    print ("Invalid user ID. Please Enter a Number.")

        elif choice == '6':
            print ("\n Goodbye!!!")
            break

        else:
            print ("Invalid Choice. Please Enter 1-6:")

        input ("\n Press Enter to Continue...")

if __name__ == "__main__":
    main ()

                

        
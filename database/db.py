import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:

    def __init__(self):

        self.connection = mysql.connector.connect(
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )

        self.cursor = self.connection.cursor()

    def create_database(self):
        self.cursor.execute(
            "CREATE DATABASE IF NOT EXISTS ticket_system"
        )

        self.cursor.execute("USE ticket_system")
        print("Database was created!")

    def create_table_tickets(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS tickets (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                status VARCHAR(20) NOT NULL,
                priority INT NOT NULL,
                CHECK (priority BETWEEN 1 AND 10)
            );
            """
        )
    def create_table_users(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                surname VARCHAR(50) NOT NULL
            );
            """
        )

    def create_user(self, first_name, surname):
        self.cursor.execute(
            """
            INSERT INTO users (first_name, surname)
            VALUES (%s, %s)
            """, (first_name, surname)
        )

        self.connection.commit()

    def remove_user(self, user_id):
        self.cursor.execute(
            """
            DELETE FROM users
            WHERE user_id = %s
            """, (user_id,)
        )

        self.connection.commit()

    def get_users(self):
        self.cursor.execute(
            """
            SELECT * FROM users
            """
        )
        return self.cursor.fetchall()



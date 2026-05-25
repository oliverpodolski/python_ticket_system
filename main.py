from database.db import DatabaseManager

db = DatabaseManager()

db.create_database()
db.create_table_tickets()
db.create_table_users()

# users = db.get_users()
# for user in users:
#   print(user)

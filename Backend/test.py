# import mysql.connector

# def setup_db():
#   # Using mysql-connector-python
#   mydb = mysql.connector.connect(
#   host="localhost",       # or your host, e.g., "127.0.0.1"
#   user="root",    # your database username
#   password="root",# your database password
#   database="summaraize"   # the name of the database you want to connect to
#   )
#   return mydb


# # def get_userinterests(userid):
# #     try:
# #         db = setup_db()
# #         cursor = db.cursor()
# #         print(12)
# #         sql = "SELECT interests FROM summaraize.interests where useremailid = %s"
# #         cursor.execute(sql, (userid))
# #         return cursor.fetchall()
# #     except Exception as e:
# #         return {"success" : False, "error_message" : str(e)}
  
# # def accessuserfeed(userId):
# #     user_interests = get_userinterests(userId)
# #     print("here I am",user_interests)
# #     lst_user_interests = user_interests
# #     get_feeddetails(lst_user_interests,userId)
# #     return {'userId': userId, 'message': 'Im still under build'}

# # accessuserfeed('testuser123@gmail.com')

# # print(get_userinterests('testuser123@gmail.com'))

# db = setup_db()
# cursor = db.cursor()
# print(123)
# # val = 'testuser123@gmail.com'
# # sql = f'Select interests from summaraize.interests where useremailid = {val}'
# # cursor.execute(sql)
# # print(cursor.fetchall())


# # use this

# val = 'testuser123@gmail.com'
# sql = 'SELECT interests FROM summaraize.interests WHERE useremailid = %s'
# cursor.execute(sql, (val,))
# print(cursor.fetchall())


# Output from the database
# data = [('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, activex, actionx',), ('testx, activex, actionx',)]

# # Create a list by unpacking the tuples
# data_list = [item for item, in data]

# # Print the resulting list
# print(data_list)


# Output from the database
data = [('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, restx, actionx',), ('testx, activex, actionx',), ('testx, activex, actionx',)]

# Flatten the list of tuples and split each string on ','
fields = [field.strip() for row in data for field in row[0].split(',')]

# Convert the list to a set to remove duplicates, then back to a list
unique_fields = list(set(fields))

print(unique_fields)

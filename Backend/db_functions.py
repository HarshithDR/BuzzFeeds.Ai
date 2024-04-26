import mysql.connector

# db = ""
def setup_db():
  # Using mysql-connector-python
  mydb = mysql.connector.connect(
  host="localhost",       # or your host, e.g., "127.0.0.1"
  user="root",    # your database username
  password="root",# your database password
  database="summaraize"   # the name of the database you want to connect to
  )
  return mydb

def set_userinterest(useremail,interests):
    print(useremail,interests)
    try:
        db = setup_db()
        cursor = db.cursor()
        sql = "INSERT INTO interests (useremailid, interests) VALUES (%s, %s)"
        val = (useremail, interests)
        cursor.execute(sql, val)
        # Retrieve the last inserted ID
        last_insert_id = cursor.lastrowid
        db.commit()
        db.close()
        print(cursor.rowcount, "record inserted.")
        return {"success" : True, "record_id" : last_insert_id}
    except Exception as e:
        return {"success" : False, "error_message" : str(e)}
  
def set_user_interests(useremail,interests):
    print(useremail,interests)
    return set_userinterest(useremail,interests)
  
def get_feeddetails(interests,userId):
  try:
      db = setup_db()
      cursor = db.cursor()
      # Constructing the placeholders for the IN clause
      placeholders = ', '.join(['%s' for _ in range(len(interests))])
      sql = f"SELECT * FROM summaraize.newsfeedinfo WHERE domain IN ({placeholders}) LIMIT 25;"
      cursor.execute(sql, (interests))
      return {"success" : True, "user" : userId, "newsFeed" : cursor.fetchall()}
  except Exception as e:
      return {"success" : False, "error_message" : str(e)}

def get_userinterests(userid):
    try:
        db = setup_db()
        cursor = db.cursor()
        sql = "SELECT interests FROM summaraize.interests where id = %s"
        cursor.execute(sql, (userid))
        return cursor.fetchall()
    except Exception as e:
        return {"success" : False, "error_message" : str(e)}
  
def accessuserfeed(userId):
    user_interests = get_userinterests(userId)
    print("here I am",user_interests)
    #lst_user_interests = user_interests.split(",")
    #get_feeddetails(lst_user_interests,userId)
    return {'userId': userId, 'message': 'Im still under build'}
  

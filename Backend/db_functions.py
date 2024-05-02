import mysql.connector

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
    #   placeholders = interests
    placeholders = ', '.join(['%s'] * len(interests))

    sql = f"SELECT * FROM summaraize.newsfeedinfo WHERE domain IN ({placeholders}) LIMIT 25;"
    cursor.execute(sql, interests)
    data  = cursor.fetchall()
    return {"success" : True, "user" : userId, "newsFeed" : data}
  except Exception as e:
      return {"success" : False, "error_message" : str(e)}

def get_userinterests(userid):
    try:
        db = setup_db()
        cursor = db.cursor()
        sql = "SELECT interests FROM summaraize.interests where useremailid = %s"
        cursor.execute(sql, (userid,))
        return cursor.fetchall()
    except Exception as e:
        return {"success" : False, "error_message" : str(e)}
  
def accessuserfeed(userId):
    user_interests = get_userinterests(userId)
    # print("here I am",user_interests)
    fields = [field.strip() for row in user_interests for field in row[0].split(',')]
    unique_fields = list(set(fields))
    # print(unique_fields)
    lst_user_interests = unique_fields
    # print(get_feeddetails(lst_user_interests,userId))
    return get_feeddetails(lst_user_interests,userId)

def set_feed_details(data):
    try:
        db = setup_db()
        cursor = db.cursor()
        sql = "INSERT INTO newsfeedinfo (domain, json_path, videopath)"
        cursor.execute(sql, data)
        last_insert_id = cursor.lastrowid
        db.commit()
        db.close()
        print(cursor.rowcount, "record inserted.")
        return {"success" : True, "record_id" : last_insert_id}
    except Exception as e:
        return {"success" : False, "error_message" : str(e)}
        

# print(accessuserfeed('testuser123@gmail.com'))
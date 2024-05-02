import mysql.connector
import json

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

def get_feed_details(interests,userId):
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

# def accessuserfeed(userId):
#     user_interests = get_userinterests(userId)
#     # print("here I am",user_interests)
#     fields = [field.strip() for row in user_interests for field in row[0].split(',')]
#     unique_fields = list(set(fields))
#     # print(unique_fields)
#     lst_user_interests = unique_fields
#     # print(get_feeddetails(lst_user_interests,userId))
#     return get_feed_details(lst_user_interests,userId)

def set_feed_details(data):
    # print(data)
    # print(json.loads(data))
    try:
        db = setup_db()
        cursor = db.cursor()
        sql = "INSERT INTO newsfeedinfo (domain, json_path, videopath) VALUES (%s, %s, %s)"
        # Provide values as a tuple to the execute function
        values = (data["interest"], data["json_url"], data["video_url"])
        cursor.execute(sql, values)
        last_insert_id = cursor.lastrowid
        db.commit()
        db.close()
        print(cursor.rowcount, "record inserted.")
        return {"success" : True, "record_id" : last_insert_id}
    except Exception as e:
        return {"success" : False, "error_message" : str(e)}
       
def retrieve_json_path_from_id(id):
    try:
        db = setup_db()
        cursor = db.cursor()
        sql = "SELECT json_path FROM newsfeedinfo WHERE id = %s"
        cursor.execute(sql,(id,))
        return cursor.fetchall()
    except Exception as e:
        return {"success" : False, "error_message" : str(e)}
    
# print(retrieve_json_path_from_id(1))
        
        
def accessuserfeed(userId):
    user_interests = get_userinterests(userId)
    result = {}
    for row in user_interests:
        interests_str = row[0]  # Extract the interests string from the tuple
        interests_list = interests_str.split(',')  # Split the string into a list of individual interests
        for interest in interests_list:
            feed_details = get_feed_details([interest], userId)
            if feed_details["success"]:
                feed_data = feed_details["newsFeed"]
                interest_data = []
                for feed_item in feed_data:
                    interest_data.append({
                        "video": feed_item[3],
                        "link": feed_item[2],
                        "dbid": feed_item[0]
                    })
                result.setdefault(interest, []).extend(interest_data)
    return result

# print(accessuserfeed('1'))
# print(set_feed_details({"interest":"ai","json_url":"lasdghasd.json","video_url":"http://sldfhsd.com"}))


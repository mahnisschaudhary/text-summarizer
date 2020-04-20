from pymongo import MongoClient
import datetime
def mongo_conn():
    try:
        print ("mongo")
        conn = MongoClient(host='127.0.0.1', port=27017)
        print("MongoDB Connected", conn)
        return conn.textsummarizer
    except Exception as e:
        print ("Error in mongo connection: ", e)


db = mongo_conn()

def register_model(first_name,last_name,username,email,password):
	print ('inside mode')
	db.users.insert({'first_name':first_name,'last_name':last_name,'email':email,'username':username,'password':password})


def login_model(username, pwd):
	data = db.users.find_one({'username':username, 'password':pwd})

	if data:
		return data['username']



def is_active(uname,phone_no):
	db.user_master.update({'name':uname,'phone':phone_no},{'$set':{'active':1}})

def is_inactive(uname,phone_no):
	db.user_master.update({'name':uname,'phone':phone_no},{'$set':{'active':0}})

def is_online(current_user):
	online_users = []
	db_data = db.user_master.find({'active':1})
	for data in db_data :
		if data.get('name') != current_user:
			online_users.append(data.get('name'))
	return online_users
def chat_db(from_m,to,msg):
    now = datetime.datetime.now()
    db.chat_db.insert({"msg_from":from_m, "msg_to" : to, "text_msg": msg , "timestamp" : now})



def get_all_msg_db(frm,to):
	msg = []
	db_data =  db.chat_db.find(
		{
			'msg_from': {'$in':[frm,to]},
			'msg_to' : {'$in': [frm,to]}
		}
	)
	for data in db_data:
		msg.append(data)
    # cursor = db.cursor()
    # # stmt = """ Select message, msg_from, msg_to from chat_db where msg_from = '%s' or msg_to = '%s' """%(frm,to)
    # stmt = """ SELECT * FROM `chat_db` WHERE msg_from IN('%s','%s') and msg_to IN('%s','%s') """%(frm,to,frm,to)
    # cursor.execute(stmt);
    # c = cursor.fetchall()
    # # print "messages   ", c
    # return c
	return msg

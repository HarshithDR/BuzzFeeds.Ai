from flask import Flask, jsonify, request
# from db_functions import *

app = Flask(__name__)

# print(setup_db())

@app.route('/interests', methods=['POST','GET'])
def userinterest():
    data = request.json
    customer_id = data.get('customer_id')
    user_interest = data.get('interests')
    print(user_interest, customer_id)
    # report = set_user_interests(user_email,user_interest)
    # if report['success']:
    #     flow.start()  
    # print(2342342143)
    # return report
    return "asahdfoiahsdgfasdfasdf"

@app.route('/newsfeed', methods=['GET'])
def newsfeed():
    # print('Im here',request.args.get('user_id'))
    data = request.json
    customer_id = data.get('user_id')
    # user_interest = data.get('interests')
    print(customer_id)
    # return accessuserfeed(request.args.get('user_id'))
    return "got your message"

@app.route('/url_source', methods = ['POST','GET']
def url_source():
    data = request.json
    url = data.get('url')
    return "got the url"

@app.route('/chat_query', methods=['POST'])
def chat_query():
    data = request.json
    user_question=data.get('question')
    # if user_question:
        # bot_response=run_chatbot(user_question)
        # return jsonify({'Response':bot_response})
    # else:
    #     return jsonify({'Error':'No Question !!'})
    print(user_question)
    return "hi how are you?"

if __name__ == '__main__':
    # Run the app on http://localhost:5000/ by default
    app.run(debug=True,port=5001)
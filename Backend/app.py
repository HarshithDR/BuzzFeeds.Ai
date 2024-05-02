from flask import Flask, jsonify, request

# from db_functions import *

app = Flask(__name__)

# print(setup_db())

# connection done
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



@app.route('/newsfeed', methods=['POST','GET'])
def newsfeed():
    # print('Im here',request.args.get('user_id'))
    # data = request.json
    # customer_id = data.get('user_id')
    # customer_id = data.get('customer_id')
    # user_interest = data.get('interests')
    # print(data)
    # return accessuserfeed(request.args.get('user_id'))
    # return "got your message"


    # Retrieve customer_id from query parameters
    customer_id = request.args.get('customer_id')
    if customer_id:
        print(f"Received customer_id: {customer_id}")
        # Here, you can process the customer_id as needed

        output = {
            "interest1": [
                {"video": "Backend/final_video_folder/output_9ee7ac98-492a-40b7-a1f9-37e1cde8c357.mp4", "link": "https://www.wikipedia.com","dbid":123},
                {"video": "Backend/final_video_folder/output_9ee7ac98-492a-40b7-a1f9-37e1cde8c357.mp4", "link": "https://www.wikipedia.com","dbid":456}
                # Add other items here if necessary
            ],
            "interest2": [
                {"video": "Backend/final_video_folder/output_44699a1d-0295-41d3-8f2b-194ec63baca3.mp4", "link": "https://www.wikipedia.com","dbid":789}  # Example placeholder
                # Add other items here if necessary
            ]
        }

        return output, 200
    else:
        return "No customer_id provided", 400


@app.route('/url_source', methods = ['POST','GET'])
def url_source():
    data = request.json
    id = data.get('id')
    print(id)
    return {}

@app.route('/chat_query', methods=['POST','GET'])
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



from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': "Homepage", "Message": "Succesfully loaded to the home page", 'Timestamp': time.time()}

    json_value = json.dumps(data_set)

    return json_value

@app.route('/user/', methods=['GET'])
def request_users():
    user_query = str(request.args.get('user')) # /user/?user=TEST

    data_set = {'Page': 'User Page', 'Message': f'Successfully got the user {user_query}', 'Timestamp': time.time()}
    json_value = json.dumps(data_set)
    return json_value

@app.route('/api/create_user/<user_id>', methods=['GET', 'POST'])
def add_message(user_id):
    data_set = {'Page': "Add Message", "Message": user_id, 'Timestamp': time.time()}

    json_value = json.dumps(data_set)

    return json_value

@app.route('/form-api', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        return '''
                  <h2>The firstname value is: {}</h2>
                  <h2>The lastname value is: {}</h2>'''.format(firstname, lastname)
    return '''
           <form method="POST">
               <div><label>Firstname: <input type="text" name="firstname"></label></div><br>
               <div><label>Lastname: <input type="text" name="lastname"></label></div><br>
               <input type="submit" value="Submit">
           </form>'''

@app.route('/api/create_user/', methods=['GET', 'POST'])
def create_user_param():
    
    query_parameter = str(request.args.get('username')) # /api/create_user/?username=TEST

    data_set = {'Page': 'User Page', 'Message': f'Successfully added the user {query_parameter}', 'Timestamp': time.time()}
    json_value = json.dumps(data_set)
    return json_value

@app.route('/api/delete_user/', methods=['DELETE'])
def delete_user() :
    delete_query = str(request.args.DELETE('delete_username')) # /api/delete_user/?delete_username=value 

    data_set = { 'Page': "Delete User Page", "Message": f'Successfully deleted user {delete_query}', 'Timestamp': time.time()}
    json.value = json.dumps(data_set)

    return delete_query

if __name__ == '__main__':
    app.run(port=7777)

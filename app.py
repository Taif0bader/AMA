from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://raghadalharbi02:<password>@cluster0.r2tqga5.mongodb.net/?retryWrites=true&w=majority" # replace with your database URI
mongo = PyMongo(app)

@app.route('/api/userTodoList', methods=['GET'])
def get_data():
    collection_name1 = mongo.db.collection_name1  # replace with your collection name
    output = []
    for s in collection_name1.find():
        output.append({'task' : s['task'], 'priority' : s['priority'],'due_date':s['due_date'],'done':s['done']})  # replace with your document structure
    return jsonify({'result' : output})


if __name__ == "__main__":
    app.run(debug=True)




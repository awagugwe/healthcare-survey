from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db']
users_collection = db['users']

class User:
    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses
        self.timestamp = datetime.now()
    
    def to_dict(self):
        return {
            'age': self.age,
            'gender': self.gender,
            'income': self.income,
            'expenses': self.expenses,
            'timestamp': self.timestamp
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        data = {
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'income': float(request.form['income']),
            'expenses': {
                'utilities': float(request.form.get('utilities', 0)),
                'entertainment': float(request.form.get('entertainment', 0)),
                'school_fees': float(request.form.get('school_fees', 0)),
                'shopping': float(request.form.get('shopping', 0)),
                'healthcare': float(request.form.get('healthcare', 0))
            }
        }
        
        # Create User instance
        user = User(data['age'], data['gender'], data['income'], data['expenses'])
        
        # Save to MongoDB
        users_collection.insert_one(user.to_dict())
        
        return jsonify({'status': 'success', 'message': 'Data submitted successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
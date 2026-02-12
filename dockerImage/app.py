import os
from flask import Flask, render_template, request, redirect, url_for
import boto3
from decimal import Decimal

app = Flask(__name__)

# Initialize DynamoDB Connection
# Ensure your AWS CLI is configured or env vars are set
dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')
table = dynamodb.Table('ProductsTable')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('contact.html')

@app.route('/contact')
def contact():
    return render_template('about.html')



@app.route('/menu')
def menu():  # Changed from 'home' to 'menu'
    try:
        response = table.scan()
        products = response.get('Items', [])
    except Exception as e:
        print(f"Connection Error: {e}")
        products = []

    return render_template('menu.html', products=products)


if __name__ == '__main__':
    # Set debug=True for development
    app.run(host='0.0.0.0', port=5000, debug=True)
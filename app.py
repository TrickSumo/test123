import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from openai import OpenAI



app = Flask(__name__)



@app.route('/tokenize', methods=['GET'])
def tokenize():
    # Retrieve text from query parameter


    return jsonify("texts")


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

from flask import Flask, request, jsonify
import openai
import boto3
import os

app = Flask(__name__)

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('ChatHistory')

openai.api_key = os.getenv(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)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    ai_reply = response["choices"][0]["message"]["content"]

    # Store chat in DynamoDB
    table.put_item(
        Item={
            "session_id": "12345",
            "user_message": user_message,
            "ai_response": ai_reply
        }
    )

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)

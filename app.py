from flask import Flask, request, jsonify, render_template
import openai
import os

# Load your OpenAI API key
openai.api_key = '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'  # Replace with your actual OpenAI API key

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_message', methods=['POST'])
def handle_message():
    message = request.json['message']

    try:
        # Use OpenAI's Chat API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" for GPT-4
            messages=[
                {"role": "user", "content": message}
            ]
        )

        # Extract the response text from OpenAI's API response
        bot_response = response['choices'][0]['message']['content'].strip()

        return jsonify({'response': bot_response})

    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

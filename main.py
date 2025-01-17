import openai
import os

# Set up your API key
openai.api_key = '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'  # Replace with your actual API key

def chatgpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error communicating with ChatGPT: {str(e)}"

def get_response(intents_list, intents_json, user_message):
    if intents_list and intents_list[0]['probability'] > '0.75':
        tag = intents_list[0]['intent']
        for intent in intents_json['intents']:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
    
    # Use ChatGPT API if no suitable predefined intent is found
    gpt_response = chatgpt_response(user_message)
    return gpt_response or "I'm sorry, I didn't understand that."

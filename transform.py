import dependencies
import openai
from extract import extract_data

openai_api_key = 'YOUR_API_KEY'
openai.api_key = openai_api_key

def generate_api_analysis():
  values_data = extract_data()
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Você é um especialista em emendas parlamentares"},
    {
      "role": "user",
      "content": f'com os valores das emendas passados em que devo me atentar? valores das emendas: {values_data} (maximo 200 caracteres)'}
    ]
  )
  response_chat_gpt = completion.choices[0].message.content.strip('\"')
  return response_chat_gpt

# analysis = generate_api_analysis()
# print(analysis)
# add_log_and_analysis(analysis=analysis)




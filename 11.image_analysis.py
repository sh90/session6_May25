import base64

import openai
import data_info
openai.api_key = data_info.open_ai_key
#gpt-4o-mini - > Images can not be analysed
with open("bowser_open/google_news.png", "rb") as image_file:
    file_data = base64.b64encode(image_file.read()).decode()
    response = openai.ChatCompletion.create(
         model="gpt-4o",
         messages=[
             {"role": "user", "content": [
                 {"type": "text", "text": "Describe what's in this image."},
                 {"type": "image_url", "image_url": {"url": "data:image/png;base64," + base64.b64encode(image_file.read()).decode()}}
             ]}
         ],
         max_tokens=1000
     )

print(response["choices"][0]["message"]["content"])
print("Hi")




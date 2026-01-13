import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

processed_data = []

for user in data:
    processed_data.append({
        "Name": user["name"],
        "Email": user["email"],
        "City": user["address"]["city"],
        "Company": user["company"]["name"]
    })

df = pd.DataFrame(processed_data)
df.to_csv("data.csv", index=False)

print("Automation Completed Successfully!")

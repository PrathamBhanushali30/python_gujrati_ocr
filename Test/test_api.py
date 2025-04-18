import requests

# URL of your local server API
url = "http://localhost:5000/upload"

# Path to your test image
image_path = "guj_final_input.jpg"

# Open the image file in binary mode
with open(image_path, 'rb') as img_file:
    files = {'image': img_file}
    response = requests.post(url, files=files)

# Check and print the response
if response.status_code == 200:
    print("✅ API Response:")
    print(response.json())
else:
    print("❌ Failed to connect to API")
    print("Status Code:", response.status_code)
    print(response.text)
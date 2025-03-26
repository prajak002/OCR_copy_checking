import requests
import base64
import os

GEMINI_API_KEY = "AIzaSyDv_WWyNUhVBiRWMg_rPQwNdW8yqDluJHI"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={GEMINI_API_KEY}"

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def run_gemini(image_path):
    image_b64 = image_to_base64(image_path)
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": "Extract clean Bengali text from this handwritten image:"},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_b64
                        }
                    }
                ]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        print("Gemini Error:", response.status_code, response.text)
        return ""

def process_all_images(image_folder, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for filename in os.listdir(image_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                image_path = os.path.join(image_folder, filename)
                print(f"Processing: {image_path}")
                gemini_result = run_gemini(image_path)
                f.write(f"\n--- {filename} ---\n")
                f.write(gemini_result + "\n")
    print(f"\n✅ All OCR results saved to '{output_file}'")

# Example usage
process_all_images("Sayantan_Das", "Sayantan_Das_ans.txt")

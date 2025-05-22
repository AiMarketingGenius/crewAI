import os
import requests
import datetime

def summarize_docx(file_path):
    print(f"🧠 [System Memory] Summarizing {file_path}")

    # Simulate summary task (replace with real logic)
    file_name = os.path.basename(file_path)
    summary = f"Summary of {file_name}: [This is a placeholder summary.]"

    # Webhook URL from Make
    WEBHOOK_URL = "https://hook.us2.make.com/jtbb5ibl9swe7liukmhozig11qc57aty"

    # Build the payload
    payload = {
        "date": str(datetime.datetime.utcnow()),
        "project": "AI Marketing Genius",
        "agent": "Dr. SEO Strategist",
        "user_id": "growyourbusiness@drseo.io",
        "original_file_url": f"https://github.com/AiMarketingGenius/crewAI/blob/main/test_kb_uploads/{file_name}",
        "summary": summary,
        "kb_tags": ["SEO", "Strategy"]
    }

    # Send the POST request
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"📬 Webhook POST response: {response.status_code}")
    except Exception as e:
        print(f"❌ Webhook POST failed: {e}")

import os
import requests
import datetime  # ✅ This was missing

def summarize_docx(file_path):
    print(f"🧠 [System Memory] Summarizing {file_path}")

    # Simulate summary task
    file_name = os.path.basename(file_path)
    summary = f"Summary of {file_name}: [This is a placeholder summary.]"

    # Simulate saving summary
    summary_file = file_path.replace(".docx", "_summary.txt")
    with open(summary_file, "w") as f:
        f.write(summary)

    # Webhook URL from Make
    WEBHOOK_URL = "https://hook.us2.make.com/jtbb5ibl9swe7liukmhozig11qc57aty"

    # Build the payload for Make webhook
    payload = {
        "date": str(datetime.datetime.utcnow()),
        "project": "AI Marketing Genius",
        "agent": "Dr. SEO Research Assistant",
        "user_id": "growyourbusiness@drseo.io",
        "original_file_url": file_path,
        "summary": summary,
        "kb_tags": ["SEO", "Experts", "Prompts"]
    }

    # Send the POST request to Make
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"📬 Webhook POST response: {response.status_code}")
    except Exception as e:
        print(f"❌ Webhook POST failed: {e}")

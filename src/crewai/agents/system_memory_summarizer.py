import os
import datetime
import requests

def summarize_docx(file_path):
    print(f"🧠 [System Memory] Summarizing {file_path}")

    # Simulate summary task (replace with real logic)
    file_name = os.path.basename(file_path)
    summary = f"Summary of {file_name}: [This is a placeholder summary.]"

    # Simulate saving summary locally
    summary_file = file_path.replace(".docx", "_summary.txt")
    with open(summary_file, "w") as f:
        f.write(summary)

    print(f"✅ Summary saved: {summary_file}")

    # === POST to Make.com Webhook ===
    WEBHOOK_URL = "https://hook.us2.make.com/jtbb5ibl9swe7liukmhozig11qc57aty"  # Make sure this matches your active scenario

    payload = {
        "date": str(datetime.datetime.utcnow()),
        "project": "AI Marketing Genius",
        "agent": "Dr. SEO Research Assistant",
        "user_id": "growyourbusiness@drseo.io",
        "original_file_url": file_path,
        "summary": summary,
        "kb_tags": ["SEO", "strategies", "prompts"]
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"📡 Webhook POST response: {response.status_code}")
    except Exception as e:
        print(f"❌ Webhook POST failed: {e}")

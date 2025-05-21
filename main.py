import sys
sys.path.append('./src')
from crewai.main import crew

# === System Memory Trigger Patch ===
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from crewai.agents.system_memory_summarizer import summarize_docx

class KBWatcher(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".docx") and "System Memory Archives" in event.src_path:
            print(f"📄 New KB Detected: {event.src_path}")
            summarize_docx(event.src_path)

if __name__ == "__main__":
    crew.kickoff()

    path = os.getenv("KB_WATCH_FOLDER", "./test_kb_uploads")
    os.makedirs(path, exist_ok=True)  # Make sure the folder exists
    event_handler = KBWatcher()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print(f"👀 Watching KB folder: {path}")

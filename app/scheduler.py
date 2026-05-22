
from apscheduler.schedulers.background import BackgroundScheduler
from app.scraper import fetch_jobs
from app.ai_filter import filter_jobs
from app.notifier import send_telegram_message

scheduler = BackgroundScheduler()


sent_job_urls = set()

def run_agent():
    print("\n--- Checking jobs ---")

    jobs = fetch_jobs()
    print(f"Found {len(jobs)} jobs")

    filtered_jobs = filter_jobs(jobs)
    print(f"Filtered {len(filtered_jobs)} backend jobs")

    new_jobs = [j for j in filtered_jobs if j["url"] not in sent_job_urls]
    print(f"New (unsent) jobs: {len(new_jobs)}")

    if not new_jobs:
        print("No new jobs to send.")
        return

    for job in new_jobs:
        message = (
            f"🚀 <b>Backend Gig Found!</b>\n\n"
            f"📝 <b>{job['title']}</b>\n\n"
            f"📄 {job['description'][:200]}...\n\n"
            f"🔗 {job['url']}"
        )
        send_telegram_message(message)
        sent_job_urls.add(job["url"])
        print(f"  Sent: {job['title'][:60]}")

def start_scheduler():
    run_agent() 
    scheduler.add_job(run_agent, "interval", hours=3)
    scheduler.start()
    print("Scheduler started — runs every 3 hours.")

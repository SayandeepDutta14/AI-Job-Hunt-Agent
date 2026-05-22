
import requests
import re

JOBICY_BASE = "https://jobicy.com/api/v2/remote-jobs"
SEARCH_TAGS = ["python", "backend", "fastapi", "django", "nodejs", "api"]

def strip_html(text):
    clean = re.sub(r"<[^>]+>", " ", text)     
    clean = re.sub(r"\s+", " ", clean).strip()  
    return clean

def fetch_jobs():
    all_jobs = []
    seen_ids = set()

    for tag in SEARCH_TAGS:
        try:
            response = requests.get(
                JOBICY_BASE,
                params={"count": 20, "tag": tag},
                timeout=10
            )
            print(f"Jobicy [{tag}] status: {response.status_code}")

            if response.status_code != 200:
                print(f"  Error: {response.text[:200]}")
                continue

            data = response.json()
            jobs = data.get("jobs", [])
            print(f"  Found {len(jobs)} jobs for tag '{tag}'")

            for job in jobs:
                job_id  = job.get("id")
                title   = job.get("jobTitle", "")
                company = job.get("companyName", "")
                url     = job.get("url", "")
                desc    = strip_html(job.get("jobDescription", ""))[:400]

                if job_id and job_id not in seen_ids:
                    seen_ids.add(job_id)
                    all_jobs.append({
                        "title": f"{title} @ {company}",
                        "url": url,
                        "description": desc,
                    })

        except Exception as e:
            print(f"  Fetch error for tag '{tag}': {e}")

    print(f"Total unique backend jobs fetched: {len(all_jobs)}")
    return all_jobs

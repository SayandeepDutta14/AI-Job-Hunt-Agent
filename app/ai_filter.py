GOOD_KEYWORDS = [
    "python", "fastapi", "django", "flask", "backend", "rest api",
    "node", "express", "api developer", "microservices", "postgresql",
    "mongodb", "graphql", "docker", "aws", "sql", "java", "spring boot"
]

BAD_KEYWORDS = [
    "frontend only", "react only", "wordpress", "shopify", "data entry",
    "virtual assistant", "customer support", "content writing", "seo only"
]

def filter_jobs(jobs):
    filtered = []

    for job in jobs:
        combined = (job["title"] + " " + job["description"]).lower()

        has_good = any(kw in combined for kw in GOOD_KEYWORDS)
        has_bad  = any(kw in combined for kw in BAD_KEYWORDS)

        if has_good and not has_bad:
            filtered.append(job)
            print(f"  [PASS] {job['title'][:70]}")
        else:
            print(f"  [SKIP] {job['title'][:70]}")

    return filtered

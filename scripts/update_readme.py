import os
import re
import json
import urllib.request
from datetime import datetime

# GitHub Config
USERNAME = "shobhitrawal-skr"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") # Optional but recommended to avoid rate limits

def make_request(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Antigravity-README-Updater")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
    try:
        with urllib.request.urlopen(req) as response:
            return response.read()
    except Exception as e:
        print(f"Error requesting {url}: {e}")
        return None

def fetch_latest_repos():
    # Fetch user's public repositories
    url = f"https://api.github.com/users/{USERNAME}/repos?sort=created&direction=desc&per_page=30"
    data = make_request(url)
    if not data:
        return ""
    
    repos = json.loads(data.decode("utf-8"))
    # Filter out forks and profile repository
    filtered_repos = []
    for r in repos:
        if r.get("fork"):
            continue
        name = r.get("name")
        if name in [USERNAME, "my-profile"]:
            continue
        filtered_repos.append(r)
        if len(filtered_repos) >= 4:
            break
            
    content = ""
    for r in filtered_repos:
        name = r.get("name")
        html_url = r.get("html_url")
        desc = r.get("description") or "No description provided."
        lang = r.get("language")
        lang_str = f" • ` {lang} `" if lang else ""
        content += f"*   **[{name}]({html_url})**{lang_str} — {desc}\n"
    return content

def fetch_recent_activity():
    url = f"https://api.github.com/users/{USERNAME}/events/public?per_page=20"
    data = make_request(url)
    if not data:
        return ""
        
    events = json.loads(data.decode("utf-8"))
    activity_lines = []
    seen_events = set()
    
    for event in events:
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name")
        if not repo:
            continue
            
        repo_url = f"https://github.com/{repo}"
        repo_link = f"[{repo}]({repo_url})"
        
        # Format events nicely
        line = ""
        if event_type == "PushEvent":
            commits = event.get("payload", {}).get("commits", [])
            num_commits = len(commits)
            if num_commits == 0:
                continue
            commit_msg = commits[0].get("message", "").split("\n")[0]
            # Truncate commit msg if too long
            if len(commit_msg) > 60:
                commit_msg = commit_msg[:57] + "..."
            line = f"🚀 Pushed {num_commits} commit(s) to {repo_link}: `{commit_msg}`"
        elif event_type == "PullRequestEvent":
            action = event.get("payload", {}).get("action")
            pr_title = event.get("payload", {}).get("pull_request", {}).get("title")
            pr_url = event.get("payload", {}).get("pull_request", {}).get("html_url")
            line = f"🔧 {action.capitalize()} Pull Request **[{pr_title}]({pr_url})** in {repo_link}"
        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action")
            issue_title = event.get("payload", {}).get("issue", {}).get("title")
            issue_url = event.get("payload", {}).get("issue", {}).get("html_url")
            line = f"💬 {action.capitalize()} Issue **[{issue_title}]({issue_url})** in {repo_link}"
        elif event_type == "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type")
            if ref_type == "repository":
                line = f"📦 Created repository {repo_link}"
            elif ref_type == "branch":
                branch_name = event.get("payload", {}).get("ref")
                line = f"🌱 Created branch `{branch_name}` in {repo_link}"
        
        if line and line not in seen_events:
            activity_lines.append(line)
            seen_events.add(line)
            if len(activity_lines) >= 5:
                break
                
    if not activity_lines:
        return "*   *No recent public activity found.*\n"
        
    return "\n".join(f"*   {line}" for line in activity_lines) + "\n"

def fetch_rss_feed():
    rss_url = os.getenv("RSS_FEED_URL")
    if not rss_url:
        return None # Do not overwrite content block if feed is not set
        
    data = make_request(rss_url)
    if not data:
        return None
        
    import xml.etree.ElementTree as ET
    try:
        root = ET.fromstring(data)
        posts = []
        # Support RSS 2.0 (channel/item) and Atom (feed/entry)
        for item in root.findall(".//item"):
            title_node = item.find("title")
            link_node = item.find("link")
            title = title_node.text if title_node is not None else "Untitled Post"
            link = link_node.text if link_node is not None else ""
            posts.append((title, link))
        if not posts:
            for entry in root.findall(".//{http://www.w3.org/2005/Atom}entry"):
                title_node = entry.find("{http://www.w3.org/2005/Atom}title")
                title = title_node.text if title_node is not None else "Untitled Post"
                link_elem = entry.find("{http://www.w3.org/2005/Atom}link")
                link = link_elem.attrib.get("href") if link_elem is not None else ""
                posts.append((title, link))
                
        content = ""
        for title, link in posts[:4]:
            content += f"*   📰 **[{title}]({link})**\n"
        return content
    except Exception as e:
        print(f"Error parsing RSS feed: {e}")
        return None

def update_section(readme_content, section_name, new_value):
    pattern = re.compile(
        rf"(<!--\s*START_SECTION:{section_name}\s*-->).*?(<!--\s*END_SECTION:{section_name}\s*-->)",
        re.DOTALL
    )
    # Check if section tags exist
    if not pattern.search(readme_content):
        print(f"Warning: Section tags for '{section_name}' not found.")
        return readme_content
    return pattern.sub(rf"\1\n{new_value}\2", readme_content)

def main():
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    readme_path = os.path.abspath(readme_path)
    
    if not os.path.exists(readme_path):
        print(f"README.md not found at {readme_path}")
        return
        
    with open(readme_path, "r", encoding="utf-8") as f:
        original_content = f.read()
        
    updated_content = original_content
    
    # 1. Fetch & update repositories
    repos_content = fetch_latest_repos()
    if repos_content:
        updated_content = update_section(updated_content, "repositories", repos_content)
        
    # 2. Fetch & update activity
    activity_content = fetch_recent_activity()
    if activity_content:
        updated_content = update_section(updated_content, "activity", activity_content)
        
    # 3. Fetch & update RSS content (only if configured)
    rss_content = fetch_rss_feed()
    if rss_content is not None:
        updated_content = update_section(updated_content, "content", rss_content)
        
    # Write only if content changed
    if updated_content != original_content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("README.md updated successfully.")
    else:
        print("No changes detected in README.md.")

if __name__ == "__main__":
    main()

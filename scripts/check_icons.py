import urllib.request
import urllib.error

def check_icon(key):
    url = f"https://skillicons.dev/icons?i={key}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            content = response.read().decode('utf-8')
            # If the icon is not found, skill-icons usually returns an empty SVG or a placeholder.
            # Let's print the length and a snippet of the SVG to see what it contains.
            print(f"Key '{key}': length={len(content)}, valid={'<svg' in content and key in content.lower()}")
    except Exception as e:
        print(f"Key '{key}': failed with error: {e}")

def main():
    keys = ["spark", "apachespark", "airflow", "snowflake", "snow", "databricks", "azure", "aws", "python", "postgres", "django", "fastapi"]
    for key in keys:
        check_icon(key)

if __name__ == "__main__":
    main()

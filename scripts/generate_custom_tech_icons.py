import os
import urllib.request
import re

FALLBACK_ICONS = {
    "apachespark": ("#E25A2C", "M12 2A10 10 0 002 12a10 10 0 0010 10 10 10 0 0010-10A10 10 0 0012 2zm0 18a8 8 0 110-16 8 8 0 010 16z"),
    "databricks": ("#FF3621", "M12 2L2 7l10 5 10-5-10-5zm0 10L2 17l10 5 10-5-10-5z"),
    "apacheairflow": ("#017CEE", "M12 2a10 10 0 100 20 10 10 0 000-20zm1 14.5v-3l2.5 1.5-2.5 1.5zm-2-5v3l-2.5-1.5 2.5-1.5z"),
    "snowflake": ("#29B6F6", "M12 2v20M2 12h20M5 5l14 14M5 19L19 5"),
    "deltalake": ("#007ACC", "M12 2L2 22h20L12 2zm0 4l7 14H5l7-14z"),
    "amazonwebservices": ("#FF9900", "M12 2L2 7l10 5 10-5-10-5zm0 15v5"),
    "microsoftazure": ("#0089D6", "M2 2h20v20H2z"),
    "python": ("#3776AB", "M12 2a5 5 0 00-5 5v2h5v1H7v3a5 5 0 005 5h2a5 5 0 005-5v-2h-5v-1h5V7a5 5 0 00-5-5z"),
    "postgresql": ("#417690", "M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2z"),
    "django": ("#092E20", "M12 2H4v20h8a10 10 0 000-20z"),
    "fastapi": ("#009688", "M12 2L2 14h9v8l10-12h-9z"),
    "git": ("#F05032", "M20.6 8.5L13.5 1.4c-.8-.8-2-.8-2.8 0L8.5 3.6l3 3c.8-.3 1.8-.1 2.4.5.6.6.8 1.6.5 2.4l3 3c.8-.3 1.8-.1 2.4.5.8.8.8 2 0 2.8s-2 .8-2.8 0c-.6-.6-.8-1.6-.5-2.4L14 10.4c-.3.3-.7.5-1.2.5-.5 0-.9-.2-1.2-.5-.6-.6-.8-1.6-.5-2.4L7.5 4.4 1.4 10.5c-.8.8-.8 2 0 2.8l7.1 7.1c.8.8 2 .8 2.8 0l7.1-7.1c.9-.8.9-2 .2-2.8z"),
    "github": ("#FFFFFF", "M12 .3C5.4.3 0 5.7 0 12.4c0 5.4 3.5 9.9 8.3 11.5.6.1.8-.3.8-.6 0-.3 0-1.1 0-2.2-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.9 1.2 1.9 1.2 1.1 1.9 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-6 0-1.3.5-2.4 1.3-3.2-.1-.3-.6-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 016 0c2.3-1.5 3.3-1.2 3.3-1.2.7 1.6.2 2.9.1 3.2.8.8 1.3 1.9 1.3 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2 0 1.6 0 2.9 0 3.3 0 .3.2.7.8.6C20.5 22.3 24 17.8 24 12.4 24 5.7 18.6.3 12 .3z"),
    "openai": ("#412991", "M12 2A10 10 0 1022 12A10 10 0 0012 2zm1 11h-2v-2h2v2z"),
    "pytorch": ("#EE4C2C", "M12 2L4 22h16L12 2z")
}

def get_simple_icon_path(slug):
    url = f"https://raw.githubusercontent.com/simple-icons/simple-icons/master/icons/{slug}.svg"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            content = response.read().decode('utf-8')
            paths = re.findall(r'd="([^"]+)"', content)
            if paths:
                return paths[0]
    except Exception as e:
        print(f"Failed to fetch {slug} from simple-icons: {e}")
    return None

def create_squircle_icon(name, slug, color, output_dir):
    path_data = get_simple_icon_path(slug)
    if not path_data:
        color, path_data = FALLBACK_ICONS.get(slug, ("#58a6ff", "M12 2L2 22h20L12 2z"))
        print(f"Using fallback path for {slug}")
        
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <!-- Clean squircle background card -->
  <rect x="1" y="1" width="46" height="46" rx="10" fill="#0d1117" stroke="#30363d" stroke-width="1.2" />
  
  <!-- Centered SVG Logo -->
  <g transform="translate(8.4, 8.4) scale(1.3)" fill="{color}">
    <path d="{path_data}" />
  </g>
</svg>
"""
    filename = os.path.join(output_dir, f"{name}.svg")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Created squircle icon: {filename}")

def main():
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "icons")
    assets_dir = os.path.abspath(assets_dir)
    os.makedirs(assets_dir, exist_ok=True)
    
    icons_to_make = {
        "python": ("python", "#3776AB"),
        "postgres": ("postgresql", "#417690"),
        "spark": ("apachespark", "#E25A2C"),
        "databricks": ("databricks", "#FF3621"),
        "airflow": ("apacheairflow", "#017CEE"),
        "snowflake": ("snowflake", "#29B6F6"),
        "azure": ("microsoftazure", "#0089D6"),
        "aws": ("amazonwebservices", "#FF9900"),
        "django": ("django", "#092E20"),
        "fastapi": ("fastapi", "#009688"),
        "git": ("git", "#F05032"),
        "github": ("github", "#FFFFFF"),
        "openai": ("openai", "#412991"),
        "pytorch": ("pytorch", "#EE4C2C"),
        "deltalake": ("deltalake", "#007ACC")
    }
    
    for name, (slug, color) in icons_to_make.items():
        create_squircle_icon(name, slug, color, assets_dir)

if __name__ == "__main__":
    main()

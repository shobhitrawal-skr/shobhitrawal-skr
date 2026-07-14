import os

def create_section_header(title, filename, icon="❖", width=320, height=45):
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#bc8cff" />
      <stop offset="60%" stop-color="#58a6ff" />
      <stop offset="100%" stop-color="#56d4dd" />
    </linearGradient>
    <linearGradient id="line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#bc8cff" />
      <stop offset="50%" stop-color="#58a6ff" />
      <stop offset="100%" stop-color="transparent" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .icon {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 16px;
      fill: #56d4dd;
      filter: url(#glow);
    }}
    .text {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      font-weight: 800;
      font-size: 18px;
      fill: url(#text-grad);
      letter-spacing: 1px;
    }}
    .underline {{
      fill: none;
      stroke: url(#line-grad);
      stroke-width: 2;
    }}
  </style>
  <text x="10" y="28" class="icon">{icon}</text>
  <text x="32" y="28" class="text">{title.upper()}</text>
  <path d="M 10 38 L {width - 20} 38" class="underline" />
</svg>
"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated section header: {filename}")

def create_category_tab(title, color, filename, icon="❖", width=280, height=36):
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="tab-bg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#161b22" />
      <stop offset="100%" stop-color="#0d1117" />
    </linearGradient>
  </defs>
  <style>
    .bg {{ fill: url(#tab-bg); stroke: #30363d; stroke-width: 1.2; rx: 6px; }}
    .bar {{ fill: {color}; rx: 2px; }}
    .icon {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 13px;
      fill: {color};
    }}
    .text {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-weight: 700;
      font-size: 12px;
      fill: #c9d1d9;
      letter-spacing: 0.5px;
    }}
  </style>
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" class="bg" />
  <rect x="8" y="8" width="4" height="{height - 16}" class="bar" />
  <text x="20" y="22" class="icon">{icon}</text>
  <text x="38" y="22" class="text">{title.upper()}</text>
</svg>
"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated category tab: {filename}")

def create_divider(filename, width=800, height=10):
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">
  <defs>
    <linearGradient id="div-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="transparent" />
      <stop offset="20%" stop-color="#bc8cff" />
      <stop offset="50%" stop-color="#58a6ff" />
      <stop offset="80%" stop-color="#56d4dd" />
      <stop offset="100%" stop-color="transparent" />
    </linearGradient>
    <filter id="glow" x="-10%" y="-30%" width="120%" height="160%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .line {{
      fill: none;
      stroke: url(#div-grad);
      stroke-width: 2;
      filter: url(#glow);
      opacity: 0.8;
    }}
  </style>
  <path d="M 10 5 L {width - 10} 5" class="line" />
</svg>
"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated divider: {filename}")

def main():
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    assets_dir = os.path.abspath(assets_dir)
    
    # Generate main section headers
    create_section_header("About Me", os.path.join(assets_dir, "section-about.svg"), icon="👤")
    create_section_header("Tech Stack", os.path.join(assets_dir, "section-tech.svg"), icon="🛠️")
    create_section_header("Featured Projects", os.path.join(assets_dir, "section-projects.svg"), icon="📂")
    create_section_header("Currently Exploring", os.path.join(assets_dir, "section-exploring.svg"), icon="🔍")
    create_section_header("GitHub Analytics", os.path.join(assets_dir, "section-analytics.svg"), icon="📈")
    create_section_header("Latest Content", os.path.join(assets_dir, "section-content.svg"), icon="📝")
    create_section_header("Recent Activity", os.path.join(assets_dir, "section-activity.svg"), icon="⚡")
    create_section_header("Latest Repositories", os.path.join(assets_dir, "section-repositories.svg"), icon="📦")
    create_section_header("Connect With Me", os.path.join(assets_dir, "section-connect.svg"), icon="🤝")
    
    # Generate sub-category dashboard tabs for Tech Stack
    create_category_tab("Data Engineering", "#bc8cff", os.path.join(assets_dir, "tab-data.svg"), icon="📊")
    create_category_tab("AI Engineering & Agents", "#56d4dd", os.path.join(assets_dir, "tab-ai.svg"), icon="🤖")
    create_category_tab("Cloud & Platform", "#58a6ff", os.path.join(assets_dir, "tab-cloud.svg"), icon="☁️")
    create_category_tab("Languages & Development", "#7ee787", os.path.join(assets_dir, "tab-dev.svg"), icon="💻")
    
    # Generate divider
    create_divider(os.path.join(assets_dir, "divider.svg"))

if __name__ == "__main__":
    main()

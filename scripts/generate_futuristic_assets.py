import os
import xml.etree.ElementTree as ET

def generate_about_card(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 180" width="800" height="180">
  <defs>
    <linearGradient id="glow-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#bc8cff" />
      <stop offset="50%" stop-color="#58a6ff" />
      <stop offset="100%" stop-color="#56d4dd" />
    </linearGradient>
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1.5; rx: 8px; }
    .accent-bar { fill: url(#glow-grad); }
    .terminal-header {
      font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, monospace;
      font-size: 13px;
      fill: #8b949e;
    }
    .terminal-body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      font-size: 14.5px;
      fill: #c9d1d9;
      line-height: 1.6;
    }
    .bold-text { font-weight: bold; fill: #58a6ff; }
    .highlight-text { font-weight: bold; fill: #bc8cff; }
    .cyan-text { fill: #56d4dd; }
  </style>
  <rect x="2" y="2" width="796" height="176" class="bg" />
  <rect x="2" y="2" width="4" height="176" class="accent-bar" />

  <!-- Terminal Command -->
  <text x="25" y="32" class="terminal-header">shobhitrawal-skr ~ $ <tspan fill="#7ee787">cat about_me.md</tspan></text>

  <!-- Bio Content -->
  <g class="terminal-body">
    <text x="25" y="65">I am a <tspan class="bold-text">Senior Data Engineer</tspan> &amp; <tspan class="bold-text">AI Builder</tspan> with <tspan class="highlight-text">9+ years of professional experience</tspan> designing and constructing</text>
    <text x="25" y="90">scalable, resilient data architectures. My core focus lies in building big data pipelines (PySpark, Spark),</text>
    <text x="25" y="115">orchestrating workflows (Airflow), and leveraging cloud systems (Azure &amp; AWS) to deliver clean software products.</text>
    <text x="25" y="145" class="cyan-text" font-family="ui-monospace, monospace" font-size="13px">🤖 Currently exploring AI Agents, Claude Code, MCP Servers, RAG systems, and open-source AI tools.</text>
  </g>
</svg>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {filename}")

def generate_tech_card(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 270" width="800" height="270">
  <defs>
    <linearGradient id="glow-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#bc8cff" />
      <stop offset="50%" stop-color="#58a6ff" />
      <stop offset="100%" stop-color="#56d4dd" />
    </linearGradient>
  </defs>
  <style>
    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1.5; rx: 8px; }
    .accent-bar { fill: url(#glow-grad); }
    .category-title {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 13px;
      font-weight: 700;
      fill: #8b949e;
      letter-spacing: 1px;
    }
    .badge-bg { fill: #161b22; stroke: #30363d; stroke-width: 1; rx: 4px; }
    .badge-text {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 11px;
      font-weight: 600;
      fill: #c9d1d9;
    }
  </style>
  <rect x="2" y="2" width="796" height="266" class="bg" />
  <rect x="2" y="2" width="4" height="266" class="accent-bar" />

  <!-- Data Engineering Column -->
  <g transform="translate(25, 25)">
    <text x="0" y="15" class="category-title" fill="#bc8cff">📊 DATA ENGINEERING</text>
    <g transform="translate(0, 30)">
      <rect x="0" y="0" width="105" height="22" class="badge-bg" />
      <text x="12" y="15" class="badge-text">Apache Spark</text>
      
      <rect x="0" y="30" width="105" height="22" class="badge-bg" />
      <text x="12" y="45" class="badge-text">PySpark</text>
      
      <rect x="0" y="60" width="105" height="22" class="badge-bg" />
      <text x="12" y="75" class="badge-text">Databricks</text>
      
      <rect x="0" y="90" width="105" height="22" class="badge-bg" />
      <text x="12" y="105" class="badge-text">Delta Lake</text>

      <rect x="0" y="120" width="105" height="22" class="badge-bg" />
      <text x="12" y="135" class="badge-text">Apache Airflow</text>

      <rect x="0" y="150" width="105" height="22" class="badge-bg" />
      <text x="12" y="165" class="badge-text">Snowflake</text>
    </g>
  </g>

  <!-- AI Engineering Column -->
  <g transform="translate(175, 25)">
    <text x="0" y="15" class="category-title" fill="#d2a8ff">🤖 AI ENGINEERING</text>
    <g transform="translate(0, 30)">
      <rect x="0" y="0" width="115" height="22" class="badge-bg" />
      <text x="12" y="15" class="badge-text">LLMs</text>
      
      <rect x="0" y="30" width="115" height="22" class="badge-bg" />
      <text x="12" y="45" class="badge-text">RAG Systems</text>
      
      <rect x="0" y="60" width="115" height="22" class="badge-bg" />
      <text x="12" y="75" class="badge-text">AI Agents</text>
      
      <rect x="0" y="90" width="115" height="22" class="badge-bg" />
      <text x="12" y="105" class="badge-text">Claude Code</text>

      <rect x="0" y="120" width="115" height="22" class="badge-bg" />
      <text x="12" y="135" class="badge-text">MCP Servers</text>
    </g>
  </g>

  <!-- Cloud Column -->
  <g transform="translate(335, 25)">
    <text x="0" y="15" class="category-title" fill="#58a6ff">☁️ CLOUD PLATFORM</text>
    <g transform="translate(0, 30)">
      <rect x="0" y="0" width="110" height="22" class="badge-bg" />
      <text x="12" y="15" class="badge-text">Microsoft Azure</text>
      
      <rect x="0" y="30" width="110" height="22" class="badge-bg" />
      <text x="12" y="45" class="badge-text">AWS</text>
      
      <rect x="0" y="60" width="110" height="22" class="badge-bg" />
      <text x="12" y="75" class="badge-text">Data Factory</text>
    </g>
  </g>

  <!-- Languages Column -->
  <g transform="translate(490, 25)">
    <text x="0" y="15" class="category-title" fill="#7ee787">💻 LANGUAGES</text>
    <g transform="translate(0, 30)">
      <rect x="0" y="0" width="100" height="22" class="badge-bg" />
      <text x="12" y="15" class="badge-text">Python</text>
      
      <rect x="0" y="30" width="100" height="22" class="badge-bg" />
      <text x="12" y="45" class="badge-text">SQL</text>
    </g>
  </g>

  <!-- Backend & Development Column -->
  <g transform="translate(635, 25)">
    <text x="0" y="15" class="category-title" fill="#56d4dd">🛠️ DEVELOPMENT</text>
    <g transform="translate(0, 30)">
      <rect x="0" y="0" width="110" height="22" class="badge-bg" />
      <text x="12" y="15" class="badge-text">Django</text>
      
      <rect x="0" y="30" width="110" height="22" class="badge-bg" />
      <text x="12" y="45" class="badge-text">FastAPI</text>

      <rect x="0" y="60" width="110" height="22" class="badge-bg" />
      <text x="12" y="75" class="badge-text">Git</text>

      <rect x="0" y="90" width="110" height="22" class="badge-bg" />
      <text x="12" y="105" class="badge-text">GitHub</text>
    </g>
  </g>
</svg>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {filename}")

def generate_project_card(filename, title, description, tech_list, index):
    colors = ["#bc8cff", "#58a6ff", "#56d4dd", "#d2a8ff", "#7ee787"]
    accent_color = colors[index % len(colors)]
    
    tech_badges = ""
    x_offset = 25
    for tech in tech_list:
        tech_width = len(tech) * 7 + 16
        tech_badges += f"""
      <rect x="{x_offset}" y="82" width="{tech_width}" height="20" class="tech-badge-bg" />
      <text x="{x_offset + 8}" y="95" class="tech-badge-text" fill="{accent_color}">{tech}</text>"""
        x_offset += tech_width + 8

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 115" width="800" height="115">
  <defs>
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1.5; rx: 6px; }}
    .accent-bar {{ fill: {accent_color}; }}
    .project-title {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 15px;
      font-weight: 700;
      fill: {accent_color};
    }}
    .project-desc {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 12.5px;
      fill: #8b949e;
    }}
    .tech-badge-bg {{ fill: #161b22; stroke: #30363d; stroke-width: 1; rx: 4px; }}
    .tech-badge-text {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 10px;
      font-weight: 600;
    }}
    .star-icon {{ fill: #f0883e; opacity: 0.85; }}
  </style>
  <rect x="2" y="2" width="796" height="111" class="bg" />
  <rect x="2" y="2" width="4" height="111" class="accent-bar" />

  <!-- Repo Icon / Title -->
  <g transform="translate(25, 20)">
    <!-- Book/Repo Icon -->
    <path d="M 0 3 L 3 0 L 11 0 L 14 3 L 14 13 L 11 16 L 3 16 L 0 13 Z" fill="none" stroke="{accent_color}" stroke-width="1.5" />
    <path d="M 3 0 L 3 16 M 11 0 L 11 16" stroke="{accent_color}" stroke-width="1" opacity="0.5" />
    
    <text x="22" y="13" class="project-title">{title}</text>
  </g>

  <!-- Description -->
  <text x="25" y="58" class="project-desc">{description}</text>

  <!-- Tech tags -->
  <g>{tech_badges}</g>

  <!-- Star highlight -->
  <g transform="translate(755, 15)">
    <path class="star-icon" d="M 8 0 L 10.5 5.5 L 16 6 L 12 10 L 13.5 15.5 L 8 12.5 L 2.5 15.5 L 4 10 L 0 6 L 5.5 5.5 Z" />
  </g>
</svg>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated project card: {filename}")

def main():
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    assets_dir = os.path.abspath(assets_dir)
    os.makedirs(assets_dir, exist_ok=True)
    
    generate_about_card(os.path.join(assets_dir, "about-card.svg"))
    generate_tech_card(os.path.join(assets_dir, "tech-card.svg"))
    
    # Generate 5 project cards
    generate_project_card(
        os.path.join(assets_dir, "project-card-1.svg"),
        "senior-data-engineer-interview-playbook",
        "A complete playbook with SQL, PySpark, Spark internals, Databricks, Azure architectures, System Design, and coding questions.",
        ["PySpark", "Apache Spark", "SQL", "Databricks", "Azure", "Delta Lake"],
        0
    )
    generate_project_card(
        os.path.join(assets_dir, "project-card-2.svg"),
        "stitchr-release",
        "Desktop application assets and packages for Stitchr - a tool providing a quick, easy, and powerful video stitching experience.",
        ["Video Stitching", "Desktop Application", "Product Packaging"],
        1
    )
    generate_project_card(
        os.path.join(assets_dir, "project-card-3.svg"),
        "vidnestor-web",
        "Web client dashboard and interface for the VidNestor ecosystem, enabling nested video layout and video library organization.",
        ["JavaScript", "HTML5", "CSS3", "Web Client"],
        2
    )
    generate_project_card(
        os.path.join(assets_dir, "project-card-4.svg"),
        "second-brain-guide",
        "Personal knowledge management guide and resources based on the Second Brain methodology to optimize developer productivity.",
        ["Markdown", "HTML", "Productivity Workflows"],
        3
    )
    generate_project_card(
        os.path.join(assets_dir, "project-card-5.svg"),
        "vidnestor-release",
        "Deployment packages and release assets for the VidNestor nested video manager application.",
        ["Release Engineering", "Application Packaging", "Deployment"],
        4
    )

if __name__ == "__main__":
    main()

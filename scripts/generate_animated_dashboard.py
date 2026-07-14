import os
import re

def get_g_block(name, assets_dir):
    filepath = os.path.join(assets_dir, "icons", f"{name}.svg")
    try:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                # Extract the logo group <g transform="translate(8.4, 8.4) scale(1.3)" fill="..."> ... </g>
                match = re.search(r'(<g transform="translate\(8\.4,\s*8\.4\)\s*scale\(1\.3\)"[^>]*>.*?</g>)', content, re.DOTALL)
                if match:
                    return match.group(1)
                # Alternative match if spacing is different
                match = re.search(r'(<g [^>]*fill="[^"]+"[^>]*>.*?</g>)', content, re.DOTALL)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Failed to read SVG group for {name}: {e}")
    return None

def make_embedded_pill(name, displayName, x, y, color, assets_dir):
    g_block = get_g_block(name, assets_dir)
    
    # Scale down the group coordinates from 48x48 container to fit inside a 32px height pill
    if g_block:
        g_block = g_block.replace('transform="translate(8.4, 8.4) scale(1.3)"', 'transform="translate(6, 6) scale(0.8)"')
        g_block = g_block.replace('transform="translate(8.4,8.4) scale(1.3)"', 'transform="translate(6, 6) scale(0.8)"')
    else:
        # Fallback if file not found or couldn't parse
        g_block = f'<g transform="translate(6, 6) scale(0.8)" fill="{color}"><rect width="24" height="24" rx="4" /></g>'
        
    return f"""
      <g transform="translate({x}, {y})">
        <!-- Glowing Halo behind pill -->
        <rect x="-1" y="-1" width="114" height="34" rx="6" class="icon-halo icon-glow" stroke="{color}" />
        <!-- Pill Background -->
        <rect x="0" y="0" width="112" height="32" rx="6" fill="#161b22" stroke="#30363d" stroke-width="1.2" />
        <!-- Logo -->
        {g_block}
        <!-- Technology Name -->
        <text x="32" y="20" font-family="-apple-system, BlinkMacSystemFont, &apos;Segoe UI&apos;, sans-serif" font-weight="700" font-size="10px" fill="#c9d1d9" letter-spacing="0.2px">{displayName}</text>
      </g>"""

def generate_animated_about(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 220" width="800" height="220">
  <defs>
    <!-- Background Grid -->
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#161b22" stroke-width="1" />
    </pattern>
    <!-- Border Gradient -->
    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#bc8cff" />
      <stop offset="50%" stop-color="#58a6ff" />
      <stop offset="100%" stop-color="#56d4dd" />
    </linearGradient>
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  
  <style>
    .bg { fill: #030712; stroke: url(#border-grad); stroke-width: 1.5; rx: 8px; }
    .laser-border {
      fill: none;
      stroke: url(#border-grad);
      stroke-width: 2;
      stroke-dasharray: 80 400;
      stroke-dashoffset: 0;
      animation: laser-travel 6s linear infinite;
    }
    .grid-bg { fill: url(#grid); }
    
    /* Hologram Radar Styles */
    .radar-circle {
      fill: none;
      stroke: #56d4dd;
      stroke-width: 1;
      opacity: 0.5;
    }
    .radar-pulse {
      fill: none;
      stroke: #56d4dd;
      stroke-width: 1.5;
      transform-origin: 80px 110px;
      animation: pulse-out 3s cubic-bezier(0.1, 0.8, 0.3, 1) infinite;
    }
    .radar-sweep {
      fill: none;
      stroke: #58a6ff;
      stroke-width: 1.5;
      opacity: 0.8;
      transform-origin: 80px 110px;
      animation: rotate-sweep 4s linear infinite;
    }

    /* Terminal Text styles */
    .term-title {
      font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, monospace;
      font-weight: 800;
      font-size: 11px;
      fill: #bc8cff;
      letter-spacing: 2px;
      opacity: 0.8;
    }
    .term-text {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 14px;
      fill: #c9d1d9;
      line-height: 1.6;
    }
    .term-highlight { font-weight: bold; fill: #58a6ff; }
    .term-green { fill: #7ee787; font-family: monospace; }
    .term-cyan { fill: #56d4dd; }

    /* Pulse Status Light */
    .status-glow {
      fill: none;
      stroke: #3fb950;
      stroke-width: 2;
      transform-origin: 715px 32px;
      animation: status-pulse 2s ease-out infinite;
    }

    @keyframes laser-travel {
      from { stroke-dashoffset: 0; }
      to { stroke-dashoffset: -480; }
    }
    @keyframes pulse-out {
      0% { r: 10px; opacity: 0.8; }
      100% { r: 55px; opacity: 0; }
    }
    @keyframes rotate-sweep {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    @keyframes status-pulse {
      0% { r: 4px; opacity: 0.8; }
      100% { r: 12px; opacity: 0; }
    }
  </style>

  <!-- Solid Outer Background -->
  <rect x="2" y="2" width="796" height="216" class="bg" />
  <!-- Grid Pattern Overlay -->
  <rect x="3" y="3" width="794" height="214" class="grid-bg" />
  
  <!-- Animated Traveling Laser Border -->
  <rect x="2" y="2" width="796" height="216" rx="8" class="laser-border" />

  <!-- Holographic Sonar / Radar Graphic (Left Column) -->
  <g transform="translate(15, 0)">
    <!-- Radar Base Circles -->
    <circle cx="80" cy="110" r="50" class="radar-circle" stroke-dasharray="4 4" />
    <circle cx="80" cy="110" r="35" class="radar-circle" />
    <circle cx="80" cy="110" r="20" class="radar-circle" stroke-dasharray="2 2" />
    
    <!-- Crosshairs -->
    <line x1="25" y1="110" x2="135" y2="110" class="radar-circle" stroke-width="0.5" />
    <line x1="80" y1="55" x2="80" y2="165" class="radar-circle" stroke-width="0.5" />

    <!-- Animated Sonar Pulses -->
    <circle cx="80" cy="110" r="10" class="radar-pulse" />
    <circle cx="80" cy="110" r="10" class="radar-pulse" style="animation-delay: 1.5s;" />

    <!-- Rotating Sonar Sweep Line -->
    <line x1="80" y1="110" x2="128" y2="78" class="radar-sweep" />
    <circle cx="80" cy="110" r="4" fill="#56d4dd" filter="url(#neon-glow)" />
  </g>

  <!-- Right Column Content (Diagnostics / Specs) -->
  <g transform="translate(170, 0)">
    <!-- Section Sub-Header -->
    <text x="10" y="36" class="term-title">❖ CORE SYSTEM DIAGNOSTICS</text>
    
    <!-- Pulse Online Status -->
    <circle cx="545" cy="32" r="4" fill="#3fb950" />
    <circle cx="545" cy="32" r="4" class="status-glow" />
    <text x="556" y="36" font-family="monospace" font-size="11px" fill="#3fb950">ONLINE</text>

    <!-- Horizontal divider inside panel -->
    <line x1="10" y1="48" x2="600" y2="48" stroke="#30363d" stroke-width="1" />

    <!-- Specifications List -->
    <g class="term-text" transform="translate(10, 72)">
      <text x="0" y="0"><tspan class="term-cyan">identity.name  :</tspan> <tspan class="term-highlight">Shobhit Rawal</tspan></text>
      <text x="0" y="24"><tspan class="term-cyan">identity.role  :</tspan> Senior Data Engineer &amp; AI Builder</text>
      <text x="0" y="48"><tspan class="term-cyan">identity.expr  :</tspan> 9+ Years designing scalable platforms</text>
      
      <!-- Specialties Row -->
      <text x="0" y="74"><tspan class="term-cyan">specialties    :</tspan></text>
      <g transform="translate(105, 74)" font-size="13px">
        <!-- Styled Tech blocks -->
        <text x="0" y="0" class="term-green">[Big Data Pipelines]</text>
        <text x="145" y="0" class="term-green">[Workflow Orchestration]</text>
        <text x="310" y="0" class="term-green">[Agentic AI &amp; MCP]</text>
      </g>

      <text x="0" y="104"><tspan class="term-cyan">identity.brand :</tspan> its_shobhit.ai</text>
    </g>
  </g>
</svg>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {filename}")

def generate_animated_tech_dashboard(filename, assets_dir):
    svg_header = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 320" width="800" height="320">
  <defs>
    <!-- Background Grid -->
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#161b22" stroke-width="1" />
    </pattern>
    <!-- Border Gradient -->
    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#bc8cff" />
      <stop offset="50%" stop-color="#58a6ff" />
      <stop offset="100%" stop-color="#56d4dd" />
    </linearGradient>
    <filter id="neon-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  
  <style>
    .bg { fill: #030712; stroke: url(#border-grad); stroke-width: 1.5; rx: 8px; }
    .laser-border {
      fill: none;
      stroke: url(#border-grad);
      stroke-width: 2;
      stroke-dasharray: 80 400;
      stroke-dashoffset: 0;
      animation: laser-travel 6s linear infinite;
    }
    .grid-bg { fill: url(#grid); }
    
    /* Panel styling */
    .panel-bg { fill: #0d1117; stroke: #30363d; stroke-width: 1; rx: 6px; }
    .panel-accent { rx: 1.5px; }
    
    .panel-title {
      font-family: ui-monospace, monospace;
      font-weight: 700;
      font-size: 11px;
      letter-spacing: 1px;
    }
    
    /* Icon halo animations */
    .icon-halo {
      fill: none;
      stroke-width: 2;
      opacity: 0.15;
      rx: 6px;
    }
    .icon-glow {
      animation: icon-pulse 3s ease-in-out infinite;
    }
    
    @keyframes laser-travel {
      from { stroke-dashoffset: 0; }
      to { stroke-dashoffset: -480; }
    }
    @keyframes icon-pulse {
      0% { opacity: 0.1; }
      50% { opacity: 0.45; }
      100% { opacity: 0.1; }
    }
  </style>

  <!-- Background -->
  <rect x="2" y="2" width="796" height="316" class="bg" />
  <rect x="3" y="3" width="794" height="314" class="grid-bg" />
  
  <!-- Laser animated border -->
  <rect x="2" y="2" width="796" height="316" rx="8" class="laser-border" />
"""

    panels = []
    
    # 1. Data Engineering Panel (x=15, y=15, w=245, h=140)
    p1 = f"""
  <!-- Data Engineering Panel -->
  <g transform="translate(15, 15)">
    <rect width="245" height="140" class="panel-bg" />
    <rect x="8" y="8" width="3" height="14" class="panel-accent" fill="#bc8cff" />
    <text x="18" y="19" class="panel-title" fill="#bc8cff">📊 DATA ENGINEERING</text>
    
    <!-- Pills Layout -->
    <g transform="translate(10, 35)">
      {make_embedded_pill("spark", "Spark", 0, 0, "#E25A2C", assets_dir)}
      {make_embedded_pill("deltalake", "Delta Lake", 115, 0, "#007ACC", assets_dir)}
      {make_embedded_pill("databricks", "Databricks", 0, 37, "#FF3621", assets_dir)}
      {make_embedded_pill("airflow", "Airflow", 115, 37, "#017CEE", assets_dir)}
      {make_embedded_pill("snowflake", "Snowflake", 0, 74, "#29B6F6", assets_dir)}
    </g>
  </g>
"""
    panels.append(p1)

    # 2. AI Engineering Panel (x=270, y=15, w=245, h=140)
    p2 = f"""
  <!-- AI Engineering Panel -->
  <g transform="translate(270, 15)">
    <rect width="245" height="140" class="panel-bg" />
    <rect x="8" y="8" width="3" height="14" class="panel-accent" fill="#56d4dd" />
    <text x="18" y="19" class="panel-title" fill="#56d4dd">🤖 AI &amp; AGENTS</text>
    
    <g transform="translate(10, 35)">
      {make_embedded_pill("openai", "OpenAI / LLM", 0, 0, "#412991", assets_dir)}
      {make_embedded_pill("pytorch", "PyTorch", 115, 0, "#EE4C2C", assets_dir)}
      {make_embedded_pill("fastapi", "MCP / APIs", 0, 37, "#009688", assets_dir)}
      {make_embedded_pill("python", "AI Core", 115, 37, "#3776AB", assets_dir)}
    </g>
  </g>
"""
    panels.append(p2)

    # 3. Cloud & Platforms (x=525, y=15, w=260, h=140)
    p3 = f"""
  <!-- Cloud & Platforms Panel -->
  <g transform="translate(525, 15)">
    <rect width="260" height="140" class="panel-bg" />
    <rect x="8" y="8" width="3" height="14" class="panel-accent" fill="#58a6ff" />
    <text x="18" y="19" class="panel-title" fill="#58a6ff">☁️ CLOUD &amp; PLATFORM</text>
    
    <g transform="translate(10, 35)">
      {make_embedded_pill("azure", "MS Azure", 0, 0, "#0089D6", assets_dir)}
      {make_embedded_pill("aws", "AWS Cloud", 115, 0, "#FF9900", assets_dir)}
    </g>
  </g>
"""
    panels.append(p3)

    # 4. Languages (x=15, y=165, w=375, h=140)
    p4 = f"""
  <!-- Languages Panel -->
  <g transform="translate(15, 165)">
    <rect width="375" height="140" class="panel-bg" />
    <rect x="8" y="8" width="3" height="14" class="panel-accent" fill="#7ee787" />
    <text x="18" y="19" class="panel-title" fill="#7ee787">💻 LANGUAGES</text>
    
    <g transform="translate(10, 35)">
      {make_embedded_pill("python", "Python", 0, 0, "#3776AB", assets_dir)}
      {make_embedded_pill("postgres", "PostgreSQL", 115, 0, "#417690", assets_dir)}
    </g>
  </g>
"""
    panels.append(p4)

    # 5. Backend & Development (x=400, y=165, w=385, h=140)
    p5 = f"""
  <!-- Backend & Dev Panel -->
  <g transform="translate(400, 165)">
    <rect width="385" height="140" class="panel-bg" />
    <rect x="8" y="8" width="3" height="14" class="panel-accent" fill="#d2a8ff" />
    <text x="18" y="19" class="panel-title" fill="#d2a8ff">🛠️ BACKEND &amp; DEVELOPMENT</text>
    
    <g transform="translate(10, 35)">
      {make_embedded_pill("django", "Django", 0, 0, "#092E20", assets_dir)}
      {make_embedded_pill("fastapi", "FastAPI", 115, 0, "#009688", assets_dir)}
      {make_embedded_pill("git", "Git VCS", 230, 0, "#F05032", assets_dir)}
      {make_embedded_pill("github", "GitHub", 0, 37, "#FFFFFF", assets_dir)}
    </g>
  </g>
"""
    panels.append(p5)

    svg_footer = "\n</svg>"
    
    full_content = svg_header + "".join(panels) + svg_footer
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"Generated animated tech dashboard: {filename}")

def main():
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    assets_dir = os.path.abspath(assets_dir)
    os.makedirs(assets_dir, exist_ok=True)
    
    generate_animated_about(os.path.join(assets_dir, "animated-about.svg"))
    generate_animated_tech_dashboard(os.path.join(assets_dir, "animated-tech.svg"), assets_dir)

if __name__ == "__main__":
    main()

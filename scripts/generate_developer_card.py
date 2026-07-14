import os

def main():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 180" width="250" height="180">
  <defs>
    <linearGradient id="glow-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#bc8cff" />
      <stop offset="50%" stop-color="#58a6ff" />
      <stop offset="100%" stop-color="#56d4dd" />
    </linearGradient>
    <linearGradient id="circuit-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#30363d" />
      <stop offset="100%" stop-color="#161b22" />
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
    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1.5; rx: 8px; }
    .bar { fill: url(#glow-grad); }
    .title {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-weight: 800;
      font-size: 16px;
      fill: #ffffff;
      letter-spacing: 0.5px;
    }
    .subtitle {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-weight: 700;
      font-size: 11px;
      fill: #bc8cff;
      letter-spacing: 1px;
    }
    .tag {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-weight: 600;
      font-size: 11px;
      fill: #56d4dd;
      letter-spacing: 0.5px;
    }
    .brand {
      font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, monospace;
      font-size: 11px;
      fill: #8b949e;
    }
    .node { fill: #58a6ff; filter: url(#neon-glow); }
    .path-line { fill: none; stroke: #30363d; stroke-width: 1.5; }
    .path-glow { fill: none; stroke: #58a6ff; stroke-width: 1.5; filter: url(#neon-glow); opacity: 0.7; }
  </style>

  <!-- Card Background -->
  <rect x="2" y="2" width="246" height="176" class="bg" />
  <rect x="2" y="2" width="4" height="176" class="bar" />

  <!-- Abstract Data Pipeline/Circuit Graphics (Data & AI Theme) -->
  <g opacity="0.6">
    <path d="M 120 150 L 160 150 L 180 130 L 220 130" class="path-line" />
    <path d="M 160 50 L 190 80 L 230 80" class="path-line" />
    <path d="M 120 150 L 160 150 L 180 130" class="path-glow" />
    
    <!-- Nodes -->
    <circle cx="120" cy="150" r="4" class="node" fill="#bc8cff" />
    <circle cx="180" cy="130" r="3" class="node" fill="#58a6ff" />
    <circle cx="220" cy="130" r="4" class="node" fill="#56d4dd" />
    <circle cx="160" cy="50" r="3.5" class="node" fill="#58a6ff" />
    <circle cx="230" cy="80" r="4" class="node" fill="#bc8cff" />
  </g>

  <!-- Identity Text -->
  <g transform="translate(20, 25)">
    <text x="0" y="15" class="title">SHOBHIT RAWAL</text>
    <text x="0" y="38" class="subtitle">SR. DATA ENGINEER</text>
    <text x="0" y="56" class="tag">AI BUILDER &amp; EXPLORER</text>
    
    <!-- Tech Brand -->
    <g transform="translate(0, 95)">
      <!-- Mini terminal prompt design -->
      <text x="0" y="0" class="brand" fill="#8b949e">brand: <tspan fill="#7ee787">its_shobhit.ai</tspan></text>
      <text x="0" y="18" class="brand" fill="#8b949e">status: <tspan fill="#58a6ff">active_builder</tspan></text>
    </g>
  </g>
</svg>"""
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    assets_dir = os.path.abspath(assets_dir)
    os.makedirs(assets_dir, exist_ok=True)
    
    filename = os.path.join(assets_dir, "developer-card.svg")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated developer card: {filename}")

if __name__ == "__main__":
    main()

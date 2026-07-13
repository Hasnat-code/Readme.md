import base64
from pathlib import Path


IMAGE_PATH = Path("ascii_art.png")
OUTPUT_PATH = Path("profile.svg")


def image_to_base64(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Could not find: {path}")

    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


image_data = image_to_base64(IMAGE_PATH)

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="1200"
    height="620"
    viewBox="0 0 1200 620"
    font-family="ConsolasFallback, Consolas, 'Courier New', monospace"
    font-size="17"
>
<style>
    @font-face {{
        src: local("Consolas"), local("Consolas Bold");
        font-family: "ConsolasFallback";
        font-display: swap;
        size-adjust: 109%;
    }}

    text, tspan {{
        white-space: pre;
    }}

    .main {{
        fill: #c9d1d9;
    }}

    .username {{
        fill: #39ff72;
        font-weight: 700;
    }}

    .orange {{
        fill: #ffa657;
        font-weight: 700;
    }}

    .yellow {{
        fill: #f2e85c;
        font-weight: 700;
    }}

    .cyan {{
        fill: #66d9ef;
        font-weight: 700;
    }}

    .purple {{
        fill: #c678dd;
        font-weight: 700;
    }}

    .pink {{
        fill: #ff5fd2;
        font-weight: 700;
    }}

    .green {{
        fill: #50fa7b;
        font-weight: 700;
    }}

    .value {{
        fill: #e6edf3;
    }}

    .dots {{
        fill: #616e7f;
    }}

    .line {{
        stroke: #616e7f;
        stroke-width: 1;
    }}
</style>

<!-- Full terminal card -->
<rect
    width="1200"
    height="620"
    rx="18"
    fill="#0d0f10"
/>

<!-- Left ASCII artwork -->
<image
    href="{image_data}"
    x="18"
    y="18"
    width="545"
    height="584"
    preserveAspectRatio="xMidYMid meet"
/>

<!-- Right terminal information -->
<text x="590" y="42" class="main">

    <tspan x="590" y="42" class="username">hasnat@dev</tspan>

    <tspan x="590" y="70" class="dots">──────────────────────────────────────────</tspan>

    <tspan x="590" y="103" class="orange">Role:</tspan>
    <tspan class="value"> Software Engineering Student</tspan>

    <tspan x="590" y="132" class="orange">Focus:</tspan>
    <tspan class="value"> Cybersecurity, DevOps, Web Development,</tspan>

    <tspan x="660" y="160" class="value">Software Testing</tspan>

    <tspan x="590" y="202" class="yellow">Languages &amp; Frameworks</tspan>

    <tspan x="590" y="234" class="cyan">Frontend:</tspan>
    <tspan class="value"> JavaScript, React, Next.js, HTML, CSS</tspan>

    <tspan x="590" y="264" class="cyan">Backend:</tspan>
    <tspan class="value"> Node.js, Java, Python, C++</tspan>

    <tspan x="590" y="294" class="cyan">Concepts:</tspan>
    <tspan class="value"> OOP, DSA, Databases</tspan>

    <tspan x="590" y="336" class="purple">Interests</tspan>

    <tspan x="590" y="368" class="pink">Industry:</tspan>
    <tspan class="value"> System Design, Software Development,</tspan>

    <tspan x="684" y="397" class="value">Web Development, UI/UX Design, Web Design,</tspan>

    <tspan x="684" y="426" class="value">DevOps, Cybersecurity, Software Testing</tspan>

    <tspan x="590" y="468" class="green">Tools</tspan>

    <tspan x="590" y="500" font-weight="700">AI:</tspan>
    <tspan class="value"> Claude, ChatGPT</tspan>

    <tspan x="590" y="530" font-weight="700">Dev:</tspan>
    <tspan class="value"> VS Code, Git, GitHub, IntelliJ, CLion, Vercel</tspan>

    <tspan x="590" y="562" class="dots">──────────────────────────────────────────</tspan>

    <tspan x="590" y="592" class="yellow">Contact</tspan>

</text>
</svg>
'''

OUTPUT_PATH.write_text(svg, encoding="utf-8")

print(f"Created successfully: {OUTPUT_PATH}")

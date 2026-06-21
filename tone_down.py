import re

def tone_down_effects():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Strip out data-scroll-speed and data-scroll-delay to stop floaty parallax
    html = re.sub(r' data-scroll-speed="[^"]*"', '', html)
    html = re.sub(r' data-scroll-delay="[^"]*"', '', html)
    html = re.sub(r' data-scroll-direction="[^"]*"', '', html)

    # 2. Inject CSS for cleaner, more formal UX
    formal_css = """
<style>
/* Formal UX overrides */
body, h1, h2, h3, p, div {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
}

/* Reduce the giant hero text size to feel more formal and less aggressive */
.ml3._1, .ml3._2, .ml3._3 {
    font-size: 6vw !important;
    line-height: 1.1 !important;
    text-transform: none !important;
    letter-spacing: -1px !important;
}

/* Make section titles more understated */
.section-title--small {
    letter-spacing: 2px !important;
    color: rgba(255, 255, 255, 0.6) !important;
    font-size: 12px !important;
    text-transform: uppercase !important;
}

/* Remove decorative noise */
.title--line-thin {
    display: none !important;
}

/* Tone down hover scales if any */
a, .news-slider__card {
    transition: transform 0.2s ease, opacity 0.2s ease !important;
}
a:hover, .news-slider__card:hover {
    transform: none !important;
    opacity: 0.8 !important;
}

/* Ensure background overlays are solid for better contrast */
.overlay {
    background-color: rgba(10, 15, 25, 0.5) !important;
}

/* Standardize text line heights for better readability */
.paragraph--medium {
    line-height: 1.6 !important;
    font-size: 1.5rem !important;
    font-weight: 400 !important;
}
</style>
</head>
"""
    # Replace </head> with the new styles injected just before it
    html = html.replace('</head>', formal_css)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    tone_down_effects()
    print("Effects toned down")

import os

def fix_html():
    # 1. Restore original HTML from content.md
    with open(r'C:\Users\kunsa\.gemini\antigravity\brain\dd57f100-162c-4770-898e-926d288c2ab2\.system_generated\steps\44\content.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Strip first 8 lines
    html = "".join(lines[8:])

    # 2. Text Replacements
    html = html.replace('<title>SRMG</title>', '<title>Nagi - AI-native research environment</title>')

    html = html.replace('<div class="nav-txtxlinks en">About</div>', '<div class="nav-txtxlinks en">The Problem</div>')
    html = html.replace('<div class="nav-txtxlinks en">Group Companies</div>', '<div class="nav-txtxlinks en">Features</div>')
    html = html.replace('<div class="nav-txtxlinks en">Brands</div>', '<div class="nav-txtxlinks en">Workflow</div>')
    html = html.replace('<div class="nav-txtxlinks en">Pillars</div>', '<div class="nav-txtxlinks en">Pricing</div>')
    html = html.replace('<div class="nav-txtxlinks en">News</div>', '<div class="nav-txtxlinks en">Start</div>')
    
    html = html.replace('<p class="ml4 en">WE&nbsp;ARE</p>', '<p class="ml4 en">NAGI&nbsp;IS</p>')
    html = html.replace('<h1 class="ml3 _1 en">A global media</h1>', '<h1 class="ml3 _1 en">An AI-native</h1>')
    html = html.replace('<h1 class="ml3 _2 en">group from the<br></h1>', '<h1 class="ml3 _2 en">research<br></h1>')
    html = html.replace('<h1 class="ml3 _3 en">Middle East</h1>', '<h1 class="ml3 _3 en">environment</h1>')
    
    html = html.replace('<p class="section-title--small en">WE&nbsp;ARE</p>', '<p class="section-title--small en">NAGI&nbsp;IS</p>')
    html = html.replace(
        '<h2 class="paragraph--medium en">Our leading journalists, creators and innovators empower audiences with bold, purposeful and inspiring content. Through 6 integrated companies, we offer partners a One-Stop solution from strategy, creative, production to distribution.</h2>',
        '<h2 class="paragraph--medium en" style="max-width: 800px">Google Scholar shows you 50,000 papers. Nagi shows you the 10 that matter — and helps you actually understand them. The ocean of research doesn\'t get smaller. Nagi teaches you to navigate it.</h2>'
    )

    html = html.replace('<p class="section-title--small en">ABOUT&nbsp;US</p>', '<p class="section-title--small en">THE PROBLEM</p>')
    html = html.replace('<p class="heading--long en">For 50 years, we’ve been in the business<br></p>', '<p class="heading--long en">People don\'t lack access to papers.<br></p>')
    html = html.replace('<p class="heading--long en">of</p>', '<p class="heading--long en">They lack</p>')
    html = html.replace(
        '<p>Our network of media brands leads pioneering conversations, inspires innovation and documents change. Our company started in 1972 and since then, has grown to more than 2,000 employees, across 18 cities around the world. We are home to some of the best&nbsp;journalists,creators, and thought-leaders on the planet. &nbsp;</p>',
        '<p>Someone gets a research topic, opens Google Scholar, gets 50,000 results, has no idea which papers matter, opens a paper and hits a wall of jargon. 100 million people worldwide engage with academic research. Almost none of them have the right environment to do it properly.</p>'
    )
    html = html.replace(
        '<p>&nbsp;</p>\n\n<p>Together, our team creates internationally&nbsp;recognised&nbsp;content with a global audience of 165 million.&nbsp;&nbsp;</p>',
        ''
    )
    html = html.replace('["information","knowledge","content"]', '["orientation","understanding","clarity"]')
    html = html.replace('<p class="letter-wrap en">learn more</p>', '<p class="letter-wrap en">discover nagi</p>')

    html = html.replace('<p class="section-title--small en">OUR&nbsp;BRANDS</p>', '<p class="section-title--small en">CORE FEATURES</p>')
    html = html.replace(
        '<div class="paragraph--medium en"><p>An unparalleled portfolio of brands and partners&nbsp;From digital to television, print and film, our brands deliver top-tier content in seven languages across four continents.</p></div>',
        '<div class="paragraph--medium en" style="max-width: 800px"><p>A complete environment for comprehension. From topic discovery to field synthesis, Nagi is the only tool built for the full workflow.</p></div>'
    )
    html = html.replace('<p class="letter-wrap medium en">see all brands</p>', '<p class="letter-wrap medium en">explore features</p>')

    feature_grid = """
    <div style="padding: 0 5vw; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; color: white;">
        <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;">
            <h3 style="font-size: 1.5rem; margin-bottom: 10px; font-family: 'Inter', sans-serif;">Research Map</h3>
            <p style="opacity: 0.7; font-size: 1.1rem; line-height: 1.5;">Enter any topic. Surfacing the 8–12 papers that actually matter — ranked by relevance, with plain language summaries. The signal not the noise.</p>
        </div>
        <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;">
            <h3 style="font-size: 1.5rem; margin-bottom: 10px; font-family: 'Inter', sans-serif;">Structured Reader</h3>
            <p style="opacity: 0.7; font-size: 1.1rem; line-height: 1.5;">Open any paper. Get a full structured breakdown: what they did, why it matters, key terms defined, and limitations surfaced.</p>
        </div>
        <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;">
            <h3 style="font-size: 1.5rem; margin-bottom: 10px; font-family: 'Inter', sans-serif;">Field Connections</h3>
            <p style="opacity: 0.7; font-size: 1.1rem; line-height: 1.5;">See how papers connect, contradict, and build on each other. Who agrees with whom. How ideas evolved over time.</p>
        </div>
        <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;">
            <h3 style="font-size: 1.5rem; margin-bottom: 10px; font-family: 'Inter', sans-serif;">Gap Detection</h3>
            <p style="opacity: 0.7; font-size: 1.1rem; line-height: 1.5;">Surface what hasn't been studied yet. Unanswered questions. Perfect for crafting proposals that add something genuinely new.</p>
        </div>
        <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;">
            <h3 style="font-size: 1.5rem; margin-bottom: 10px; font-family: 'Inter', sans-serif;">Review Outliner</h3>
            <p style="opacity: 0.7; font-size: 1.1rem; line-height: 1.5;">Generate a structured literature review outline from your paper set — organised by theme. A thinking structure you can actually write from.</p>
        </div>
        <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;">
            <h3 style="font-size: 1.5rem; margin-bottom: 10px; font-family: 'Inter', sans-serif;">Reading List</h3>
            <p style="opacity: 0.7; font-size: 1.1rem; line-height: 1.5;">Your personal library. Save papers. Tag by topic. Track reading progress. Add notes. Never lose a paper again.</p>
        </div>
    </div>
    """

    # We will hide the brands inner contents safely and append our grid above it, or inside it.
    # Searching for the exact div wrapper: `<div class="brands__logo-section">`
    start_idx = html.find('<div class="brands__logo-section">')
    if start_idx != -1:
        # Instead of parsing and replacing the closing tag (which broke things),
        # we can just inject our grid right after the opening tag, and add a style to the next rows to hide them.
        injection = f'<div class="brands__logo-section">{feature_grid}<div style="display:none;">'
        html = html[:start_idx] + injection + html[start_idx + len('<div class="brands__logo-section">'):]
        
        # We need to close the <div style="display:none;"> at the end of the brands logo section.
        # Let's find the "The latest, news, events" which comes right after the brands section in SRMG.
        next_section_idx = html.find('The latest, news, events and launches from our world-leading brands')
        if next_section_idx != -1:
            # We inject the closing </div> before this section's wrapper
            # Wait, easier to just hide all elements with class 'brands__row' via a replace:
            pass

    # Safer way to hide original brand rows without breaking DOM:
    html = html.replace('class="brands__row"', 'class="brands__row" style="display:none !important;"')
    html = html.replace('class="brands__row middle"', 'class="brands__row middle" style="display:none !important;"')

    html = html.replace('The latest, news, events and launches from our world-leading brands', 'The Full Workflow: From "I have a topic" to "I have written something I actually understand."')
    html = html.replace('<p class="letter-wrap medium en">see all news</p>', '<p class="letter-wrap medium en">start workflow</p>')
    html = html.replace('<p class="section-title--small en">LATEST&nbsp;NEWS</p>', '<p class="section-title--small en">THE WORKFLOW</p>')

    html = html.replace('Saudi Research and Media Group Awarded Contract to Operate and Manage Al Thaqafeya Channel', 'Have a topic -> Research Map finds what matters')
    html = html.replace('April 26, 2026 | Press &amp; Media', 'Step 1 | Discover')
    
    html = html.replace('SRMG Media Solutions (SMS) Forms Strategic Partnership with Phi to Attract Global Advertisers and Expand OOH Opportunities in the MENA Region', 'Structured Reader explains each paper and Field Connections shows how they relate.')
    html = html.replace('April 25, 2025 | Press &amp; Media', 'Step 2 | Understand & Synthesize')

    html = html.replace('SRMG and Bill &amp; Melinda Gates Foundation join forces to tackle global health and development challenges', 'Gap Detection surfaces what\'s missing, and Outliner builds the writing structure.')
    html = html.replace('April 28, 2024 | Press &amp; Media', 'Step 3 | Discover Gaps & Write')

    html = html.replace('<img src="https://www.srmg.com/images/logo-white.svg"', '<span style="font-family:\'Noto Sans JP\', sans-serif; font-size:24px; color:white; font-weight:bold;">凪 Nagi</span><img style="display:none;" src="https://www.srmg.com/images/logo-white.svg"')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    fix_html()
    print("Done")

from bs4 import BeautifulSoup

def add_glassy_nav():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Add the glass bg div at the start of the body
    glass_bg_html = """
    <div class="navbar-glass-bg" style="position: fixed; top: 0; left: 0; width: 100%; height: 95px; background: rgba(0, 0, 0, 0.35); backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px); z-index: 9999; border-bottom: 1px solid rgba(255, 255, 255, 0.1); pointer-events: none;"></div>
    """
    
    # Check if it already exists to prevent duplicates
    if not soup.find('div', class_='navbar-glass-bg'):
        soup.body.insert(0, BeautifulSoup(glass_bg_html, 'html.parser'))

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    add_glassy_nav()
    print("Glassy navbar added")

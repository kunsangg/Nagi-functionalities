from bs4 import BeautifulSoup

def fix_hamburger():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    nav_buttons = soup.find('div', class_='nav-buttons')
    if nav_buttons:
        # Give it a higher z-index than the desktop nav (10000) and logo (10001)
        # Position it fixed at top right to align with the logo's padding and desktop nav.
        # Add cursor pointer and pointer-events to ensure clickability.
        nav_buttons['style'] = "position: fixed; top: 0; right: 0; padding: 30px 4vw; z-index: 10005; display: flex; align-items: center; justify-content: center; pointer-events: auto; cursor: pointer;"

        # Make sure the inner wrapper is also clickable
        brgr_wrapper = nav_buttons.find('div', class_='brgr-wrapper')
        if brgr_wrapper:
            existing_style = brgr_wrapper.get('style', '')
            brgr_wrapper['style'] = existing_style + '; cursor: pointer; pointer-events: auto; display: block;'
            
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    fix_hamburger()
    print("Hamburger fixed")

from bs4 import BeautifulSoup

def fix_hamburger_alignment():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    desktop_nav = soup.find('div', class_='nagi-desktop-nav')
    nav_buttons = soup.find('div', class_='nav-buttons')
    
    if desktop_nav and nav_buttons:
        # Move nav_buttons inside desktop_nav
        nav_buttons.extract()
        desktop_nav.append(nav_buttons)
        
        # Reset nav_buttons styles so it acts like a flex item instead of fixed overlay
        # It needs some margin-left so it has space after the Sign In button
        nav_buttons['style'] = "position: relative; z-index: 10005; display: flex; align-items: center; justify-content: center; pointer-events: auto; cursor: pointer; margin-left: 10px;"
        
        # Reset desktop_nav padding from 10vw back to 4vw
        existing_style = desktop_nav.get('style', '')
        desktop_nav['style'] = existing_style.replace('10vw', '4vw')
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    fix_hamburger_alignment()
    print("Hamburger moved inside desktop nav")

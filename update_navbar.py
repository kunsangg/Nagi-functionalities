from bs4 import BeautifulSoup

def update_navbar():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Hide nav-buttons
    nav_buttons = soup.find('div', class_='nav-buttons')
    if nav_buttons:
        nav_buttons['style'] = 'display: none !important;'

    # Hide the big nav-wrapper dropdown to prevent accidental clicks
    nav_wrapper = soup.find('div', class_='nav-wrapper')
    if nav_wrapper:
        nav_wrapper['style'] = 'display: none !important;'

    # Check if we already added it
    if soup.find('div', class_='nagi-desktop-nav'):
        soup.find('div', class_='nagi-desktop-nav').decompose()

    new_nav = soup.new_tag('div', **{'class': 'nagi-desktop-nav'})
    new_nav['style'] = "position: fixed; top: 0; right: 0; padding: 30px 4vw; display: flex; align-items: center; gap: 40px; z-index: 10000;"
    
    links = [
        ("Explore", "#"),
        ("The Gap", "#"),
        ("How it works", "#"),
        ("Who it's for", "#")
    ]
    
    for text, href in links:
        a = soup.new_tag('a', href=href)
        a.string = text
        a['style'] = "color: white; text-decoration: none; font-family: 'Noto Sans JP', sans-serif; font-size: 14px; font-weight: 400; transition: opacity 0.3s;"
        a['onmouseover'] = "this.style.opacity='0.7'"
        a['onmouseout'] = "this.style.opacity='1'"
        new_nav.append(a)

    sign_in = soup.new_tag('a', href="#")
    sign_in.string = "Sign In \u2192"
    sign_in['style'] = "color: white; text-decoration: none; font-family: 'Noto Sans JP', sans-serif; font-size: 14px; font-weight: 500; border: 1px solid white; border-radius: 30px; padding: 12px 24px; transition: all 0.3s; margin-left: 10px;"
    sign_in['onmouseover'] = "this.style.backgroundColor='white'; this.style.color='black';"
    sign_in['onmouseout'] = "this.style.backgroundColor='transparent'; this.style.color='white';"
    
    new_nav.append(sign_in)

    if nav_buttons:
        nav_buttons.insert_after(new_nav)
    else:
        soup.body.append(new_nav)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    update_navbar()
    print("Navbar updated successfully")

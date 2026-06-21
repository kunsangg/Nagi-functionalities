from bs4 import BeautifulSoup

def restore_hamburger():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Unhide nav-buttons
    nav_buttons = soup.find('div', class_='nav-buttons')
    if nav_buttons and 'style' in nav_buttons.attrs:
        # Remove display: none !important
        nav_buttons['style'] = nav_buttons['style'].replace('display: none !important;', '').strip()
        if not nav_buttons['style']:
            del nav_buttons['style']

    # Unhide nav-wrapper (the mega menu) so it actually opens when hamburger is clicked
    # Wait, the mega menu was also hidden. I should unhide it but let CSS handle its default state
    nav_wrapper = soup.find('div', class_='nav-wrapper')
    if nav_wrapper and 'style' in nav_wrapper.attrs:
        nav_wrapper['style'] = nav_wrapper['style'].replace('display: none !important;', '').strip()
        if not nav_wrapper['style']:
            del nav_wrapper['style']

    # Adjust the desktop nav to not overlap with the hamburger menu.
    # The hamburger menu is usually at the far right (e.g. right: 4vw).
    # I'll add some extra margin/padding to the right of the desktop nav so the hamburger sits to its right.
    desktop_nav = soup.find('div', class_='nagi-desktop-nav')
    if desktop_nav and 'style' in desktop_nav.attrs:
        # Change right: 0; padding: 30px 4vw; to have more right padding, e.g. padding-right: 100px or so
        style = desktop_nav['style']
        style = style.replace('padding: 30px 4vw;', 'padding: 30px 10vw 30px 4vw;') # 10vw gives space for hamburger
        desktop_nav['style'] = style

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    restore_hamburger()
    print("Hamburger menu restored")

from bs4 import BeautifulSoup

def fix_logo_gradient():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    logo_links = soup.find_all('a', class_='logo--home')
    
    html_logo = """
    <div style="display: flex; align-items: center; text-decoration: none !important;">
        <span style="font-size: 38px; font-weight: 900; background: linear-gradient(to bottom, #004fb0 0%, #46c2eb 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1; font-family: 'Noto Sans JP', sans-serif;">
            澳
        </span>
        <span style="color: white; font-size: 26px; font-weight: 800; font-family: 'Inter', 'Arial Black', sans-serif; margin-left: 8px; line-height: 1; letter-spacing: 0.5px; margin-top: 4px;">
            NAGI
        </span>
    </div>
    """
    
    for logo_link in logo_links:
        # Clear the old HTML stack
        logo_link.clear()
        
        # Make sure the anchor has no underline
        existing_style = logo_link.get('style', '')
        if 'text-decoration: none' not in existing_style:
            logo_link['style'] = existing_style + '; text-decoration: none !important;'

        # Append the new gradient logo
        new_logo = BeautifulSoup(html_logo, 'html.parser')
        logo_link.append(new_logo)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    fix_logo_gradient()
    print("Logo fixed with gradient kanji")

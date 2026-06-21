from bs4 import BeautifulSoup

def fix_logo_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    logo_links = soup.find_all('a', class_='logo--home')
    
    html_logo = """
    <div style="display: flex; align-items: flex-end; font-family: 'Inter', sans-serif; line-height: 0.85; text-decoration: none !important;">
        <div style="display: flex; flex-direction: column; color: #00a8c6; font-size: 28px; font-weight: 900; letter-spacing: 0px;">
            <div style="display: flex; justify-content: space-between; gap: 2px;">
                <span>N</span><span>A</span>
            </div>
            <div style="display: flex; justify-content: space-between; gap: 2px;">
                <span>G</span><span>I</span>
            </div>
        </div>
        <div style="color: white; font-size: 36px; font-weight: 900; margin-left: 6px; margin-bottom: -4px;">
            海
        </div>
    </div>
    """
    
    for logo_link in logo_links:
        # Clear the broken image tag
        logo_link.clear()
        
        # Make sure the anchor has no underline
        existing_style = logo_link.get('style', '')
        if 'text-decoration: none' not in existing_style:
            logo_link['style'] = existing_style + '; text-decoration: none !important;'

        # Append the new pure-HTML logo
        new_logo = BeautifulSoup(html_logo, 'html.parser')
        logo_link.append(new_logo)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    fix_logo_html()
    print("Logo fixed using pure HTML/CSS")

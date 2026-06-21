from bs4 import BeautifulSoup

def fix_overlap():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    logo_links = soup.find_all('a', class_='logo--home')
    
    for logo_link in logo_links:
        # Style the container
        existing_style = logo_link.get('style', '')
        # Remove any existing text-decoration just in case, then append ours
        logo_link['style'] = existing_style + '; text-decoration: none !important; display: flex; align-items: center;'
        
        # Clear existing logo spans
        logo_link.clear()

        # Add the new styled logo
        blue_kanji = soup.new_tag('span')
        blue_kanji.string = "凪"
        blue_kanji['style'] = "color: #38bdf8; font-size: 32px; font-weight: bold; line-height: 1;"
        
        nagi_text = soup.new_tag('span')
        nagi_text.string = "NAGI"
        nagi_text['style'] = "color: white; font-size: 24px; font-weight: 800; font-family: 'Inter', 'Noto Sans JP', sans-serif; margin-left: 8px; line-height: 1; letter-spacing: 0.5px; text-decoration: none !important;"
        
        logo_link.append(blue_kanji)
        logo_link.append(nagi_text)

    # Make sure n--logo is positioned correctly
    logo_div = soup.find('div', class_='n--logo')
    if logo_div:
        logo_div['style'] = "position: fixed; top: 0; left: 0; padding: 30px 4vw; z-index: 10001;"

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    fix_overlap()
    print("Overlap fixed")

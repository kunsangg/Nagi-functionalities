from bs4 import BeautifulSoup

def fix_logo():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    logo_link = soup.find('a', class_='logo--home')
    if logo_link:
        logo_link['style'] = logo_link.get('style', '') + '; text-decoration: none !important; display: flex; align-items: center;'
        # Clear existing logo span
        logo_link.clear()

        # Add the new styled logo
        blue_kanji = soup.new_tag('span')
        # Using the exact kanji in the screenshot, or 凪. The screenshot has a logo that looks like a water kanji.
        blue_kanji.string = "凪"
        blue_kanji['style'] = "color: #38bdf8; font-size: 32px; font-weight: bold; line-height: 1;"
        
        nagi_text = soup.new_tag('span')
        nagi_text.string = "NAGI"
        nagi_text['style'] = "color: white; font-size: 24px; font-weight: 800; font-family: 'Inter', 'Noto Sans JP', sans-serif; margin-left: 8px; line-height: 1; letter-spacing: 0.5px;"
        
        logo_link.append(blue_kanji)
        logo_link.append(nagi_text)

    # Ensure the logo container is positioned properly at the top left
    logo_div = soup.find('div', class_='n--logo')
    if logo_div:
        logo_div['style'] = "position: fixed; top: 0; left: 0; padding: 30px 4vw; z-index: 10001;"

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    fix_logo()
    print("Logo updated")

from bs4 import BeautifulSoup

def remove_ar():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    lang_links = soup.find_all('a', class_='lang-p-wrap')
    for link in lang_links:
        if 'Ar' in link.get_text() or 'AR' in link.get_text():
            link['style'] = link.get('style', '') + '; display: none !important;'

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    remove_ar()
    print("Arabic language link removed")

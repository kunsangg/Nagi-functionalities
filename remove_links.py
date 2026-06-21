from bs4 import BeautifulSoup

def remove_links():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find all <a> tags
    for a in soup.find_all('a'):
        # If the href doesn't start with '#', or if we just want to override all of them
        # Let's override all hrefs to javascript:void(0); to prevent any navigation
        # But wait, href="#" is sometimes used for anchor links. 
        # javascript:void(0); is safer to prevent page reload or jump.
        a['href'] = 'javascript:void(0);'
        
        # Remove target attribute so it doesn't open new tabs
        if 'target' in a.attrs:
            del a['target']

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    remove_links()
    print("All link redirections removed.")

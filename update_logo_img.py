from bs4 import BeautifulSoup

def update_logo_img():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    logo_links = soup.find_all('a', class_='logo--home')
    
    for logo_link in logo_links:
        # Clear existing logo spans
        logo_link.clear()

        # Add the new image tag
        img_tag = soup.new_tag('img', src='logo.png', alt='NAGI Logo')
        # Style it to fit nicely in the navbar
        img_tag['style'] = "width: 50px; height: auto; border-radius: 4px; display: block;"
        
        logo_link.append(img_tag)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    update_logo_img()
    print("Logo updated to use image")

from bs4 import BeautifulSoup

def fix_scroll():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find the meech target
    meech_target = soup.find('section', id='meechTarget')
    if meech_target and 'data-scroll-section' in meech_target.attrs:
        del meech_target['data-scroll-section']

    # Wait, in Barba.js, the page content must be inside `data-barba="container"`.
    # Our meech target is a sibling of `div.transition-fade` which is the Barba container!
    # If Barba runs a page transition, it will replace `transition-fade` and leave our section alone,
    # OR it might cause height issues if it expects all content to be inside `transition-fade`.
    # To be safe, let's move meechTarget INSIDE `transition-fade`, at the very end of it.
    
    transition_fade = soup.find('div', class_='transition-fade')
    if transition_fade and meech_target:
        # Move it inside transition-fade
        meech_target.extract()
        transition_fade.append(meech_target)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    fix_scroll()
    print("Scroll fixed")

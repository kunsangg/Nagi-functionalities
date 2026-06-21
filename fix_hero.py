from bs4 import BeautifulSoup

def run():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find the h1 tags
    h1_1 = soup.find('h1', class_='_1')
    h1_2 = soup.find('h1', class_='_2')
    h1_3 = soup.find('h1', class_='_3')

    if h1_1:
        h1_1.string = "Calm in the"
    
    if h1_2:
        # Some tags might have inner tags like <br/>, so we clear and append string and <br/>
        h1_2.clear()
        h1_2.append("ocean of")
        h1_2.append(soup.new_tag("br"))
        
    if h1_3:
        h1_3.string = "research"

    # Also make sure "WE ARE" text says "NAGI IS" if there's a `<p class="ml4">`
    we_are = soup.find('p', class_='ml4')
    if we_are and "WE ARE" in we_are.text:
        we_are.string = "NAGI IS"

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    run()
    print("Hero fully fixed")

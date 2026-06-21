from bs4 import BeautifulSoup

def run():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    cards_data = [
        {
            "label": "Step 1 · Discover",
            "title": "Have a topic → Research Map finds what matters",
            "body": "Enter anything. Federated learning. Climate policy. Quantum computing. Nagi surfaces the 8–12 papers that actually define the field — ranked, explained, ready to read. Not 50,000 results. The ones that matter."
        },
        {
            "label": "Step 2 · Understand",
            "title": "Structured Reader explains each paper. Field Connections shows how they relate.",
            "body": "Open any paper — get a full plain language breakdown. What they did. Why it matters. Key terms. Limitations. Then see how every paper connects to every other — who builds on whom, who contradicts whom, where the field is heading."
        },
        {
            "label": "Step 3 · Discover Gaps",
            "title": "Find what nobody has researched yet.",
            "body": "Nagi surfaces the unanswered questions and white spaces in any field. The open problems. The understudied areas. The place where your research could actually add something new."
        },
        {
            "label": "Step 4 · Write",
            "title": "Go from papers to a literature review outline. Instantly.",
            "body": "Generate a structured outline from your paper set — organised by theme, argument, and narrative flow. Not a summary. A thinking structure you can actually write from."
        },
        {
            "label": "Step 5 · Organise",
            "title": "Your research library. Alive and growing.",
            "body": "Save papers. Tag by project. Track what you've read and understood. Add notes. Never lose a paper. Never forget what it said. Never start from scratch on a topic you've already explored."
        }
    ]

    card_wrappers = soup.find_all('div', class_='c--wrap__card')
    
    for i, wrapper in enumerate(card_wrappers):
        if i < len(cards_data):
            data = cards_data[i]
            # update label
            date_p = wrapper.find('p', class_='txt--card-date')
            if date_p:
                date_p.string = data['label']
            
            # update title
            title_p = wrapper.find('p', class_='txt--card-title')
            if title_p:
                title_p.string = data['title']
                
            # Check if body already exists (in case we run this twice)
            body_p = wrapper.find('p', class_='txt--card-body')
            if not body_p:
                # create text-wrap div and body p
                text_wrap = soup.new_tag('div', attrs={"class": "text-wrap"})
                body_p = soup.new_tag('p', attrs={
                    "class": "txt--card-body en", 
                    "style": "opacity: 0.7; font-size: 15px; margin-top: 15px; line-height: 1.5; font-family: 'Inter', sans-serif;"
                })
                text_wrap.append(body_p)
                wrapper.append(text_wrap)
                
            body_p.string = data['body']
        else:
            # Hide the 6th card (or any extra ones)
            slide = wrapper.find_parent('div', class_='swiper-slide')
            if slide:
                slide['style'] = slide.get('style', '') + '; display: none !important;'
            else:
                a_parent = wrapper.find_parent('a')
                if a_parent:
                    a_parent['style'] = a_parent.get('style', '') + '; display: none !important;'

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    run()
    print("Cards updated successfully")

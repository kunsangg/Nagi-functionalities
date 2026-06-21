from bs4 import BeautifulSoup

def update_news():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    news_cards = soup.find_all('div', class_='news-slider__content')
    
    # We already replaced the first two in fix_content.py, but they might be overwritten or we can just replace them all here to be safe and clean.
    
    replacements = [
        {
            "date": "Step 1 | Discover",
            "title": "Have a topic -> Research Map finds what matters"
        },
        {
            "date": "Step 2 | Understand & Synthesize",
            "title": "Structured Reader explains each paper and Field Connections shows how they relate."
        },
        {
            "date": "Step 3 | Connect",
            "title": "Field Connections shows how papers relate, contradict, and build on each other."
        },
        {
            "date": "Step 4 | Identify Gaps",
            "title": "Gap Detection surfaces unanswered questions to help you craft novel proposals."
        },
        {
            "date": "Step 5 | Outline",
            "title": "Review Outliner automatically generates a structured literature review from your reading list."
        },
        {
            "date": "Step 6 | Write",
            "title": "You have synthesized the field and are ready to write with clarity and confidence."
        }
    ]

    for i, card in enumerate(news_cards):
        if i < len(replacements):
            date_elem = card.find('p', class_='txt--card-date')
            title_elem = card.find('p', class_='txt--card-title')
            
            if date_elem:
                date_elem.string = replacements[i]["date"]
            if title_elem:
                title_elem.string = replacements[i]["title"]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    update_news()
    print("News updated")

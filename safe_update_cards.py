from bs4 import BeautifulSoup

def safe_run():
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

    # The cards are inside `.c--wrap__card` inside the news section.
    # However, to be perfectly safe, let's just find the `.txt--card-date` and `.txt--card-title`
    dates = soup.find_all('p', class_='txt--card-date')
    titles = soup.find_all('p', class_='txt--card-title')
    
    # Update text content safely
    for i in range(min(len(dates), len(titles))):
        if i < len(cards_data):
            data = cards_data[i]
            # Update label
            dates[i].string = data['label']
            
            # Update title and append body inside the same paragraph to prevent flex layout breakage
            titles[i].clear()
            
            title_span = soup.new_tag('span', attrs={"style": "font-weight: 600; display: block;"})
            title_span.string = data['title']
            titles[i].append(title_span)
            
            body_span = soup.new_tag('span', attrs={
                "style": "display: block; opacity: 0.7; font-size: 14px; margin-top: 12px; line-height: 1.5; font-family: 'Inter', sans-serif; font-weight: 400;"
            })
            body_span.string = data['body']
            titles[i].append(body_span)
        else:
            # Hide the 6th card safely by finding the closest slide or link wrapper
            slide = dates[i].find_parent('div', class_='swiper-slide')
            if slide:
                slide['style'] = slide.get('style', '') + '; display: none !important;'

    # Inject the video on the first card
    # The first card usually has an image class "nav-latest__img" or "latest__card-image"
    first_date = dates[0] if dates else None
    if first_date:
        card_wrap = first_date.find_parent('div', class_='swiper-slide') or first_date.find_parent('a')
        if card_wrap:
            img_tag = card_wrap.find('img')
            if img_tag:
                # We add the video safely on top of the image so we don't break sizing scripts
                video_url = "https://www.pexels.com/download/video/8369880/"
                video_tag = soup.new_tag('video', attrs={
                    "autoplay": "",
                    "loop": "",
                    "muted": "",
                    "playsinline": "",
                    "style": "position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 5;"
                })
                source_tag = soup.new_tag('source', attrs={
                    "src": video_url,
                    "type": "video/mp4"
                })
                video_tag.append(source_tag)
                
                # Make sure the container is relative so the absolute video overlays it perfectly
                img_container = img_tag.parent
                img_container['style'] = img_container.get('style', '') + '; position: relative; overflow: hidden;'
                
                img_container.append(video_tag)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    safe_run()
    print("Cards safely updated")

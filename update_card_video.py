from bs4 import BeautifulSoup

def update_card_video():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find the card containing "Step 1 · Discover"
    elem = soup.find(string=lambda t: t and 'Step 1 · Discover' in t)
    if elem:
        # Navigate up to the card container
        card_wrap = elem.find_parent('div', class_='c--wrap__card')
        if not card_wrap:
            # Let's try navigating up to 'a' or 'swiper-slide'
            card_wrap = elem.find_parent('a') or elem.find_parent('div', class_='swiper-slide')
            
        if card_wrap:
            # Find the image container or the image itself
            img_tag = card_wrap.find('img', class_='nav-latest__img')
            if img_tag:
                # Replace the img tag with a video tag
                video_url = "https://www.pexels.com/download/video/8369880/"
                video_tag = soup.new_tag('video', attrs={
                    "autoplay": "",
                    "loop": "",
                    "muted": "",
                    "playsinline": "",
                    "class": "nav-latest__img",
                    "style": "object-fit: cover; width: 100%; height: 100%;"
                })
                source_tag = soup.new_tag('source', attrs={
                    "src": video_url,
                    "type": "video/mp4"
                })
                video_tag.append(source_tag)
                img_tag.replace_with(video_tag)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    update_card_video()
    print("Video updated")

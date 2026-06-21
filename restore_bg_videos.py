from bs4 import BeautifulSoup

def run():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Restore the Hero Background Video
    new_hero_video = "https://www.pexels.com/download/video/34660607/"
    old_video_1 = "https://content.jwplatform.com/videos/mT3HmOu6-xndmizFa.mp4"
    old_video_2 = "https://www.srmg.com/transformation/videos/Sequence12.webm"
    
    html = html.replace(old_video_1, new_hero_video)
    html = html.replace(old_video_2, new_hero_video)

    # 2. Restore the secondary section background video (replacing the large image-10)
    soup = BeautifulSoup(html, 'html.parser')
    img10 = soup.find('img', class_='image-10')
    if img10:
        new_vid_url = "https://www.pexels.com/download/video/30608661/"
        video_tag = soup.new_tag('video', attrs={
            "autoplay": "",
            "loop": "",
            "muted": "",
            "playsinline": "",
            "class": "image-10",
            "style": "object-fit: cover; width: 100%; height: 100%;"
        })
        source_tag = soup.new_tag('source', attrs={
            "src": new_vid_url,
            "type": "video/mp4"
        })
        video_tag.append(source_tag)
        img10.replace_with(video_tag)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    run()
    print("Background videos restored successfully")

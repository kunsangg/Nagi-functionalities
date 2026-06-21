def change_video():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_video_url = "https://www.pexels.com/download/video/34660607/"
    old_video_1 = "https://content.jwplatform.com/videos/mT3HmOu6-xndmizFa.mp4"
    old_video_2 = "https://www.srmg.com/transformation/videos/Sequence12.webm"

    html = html.replace(old_video_1, new_video_url)
    html = html.replace(old_video_2, new_video_url)

    # Note: Pexels download link might not play instantly inline without a proper direct asset link, but it should work in most modern browsers for video tags. If they require a true CDN link we might need to adjust, but this replaces it exactly as requested.

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    change_video()
    print("Video replaced")

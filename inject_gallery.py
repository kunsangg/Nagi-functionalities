from bs4 import BeautifulSoup

def inject_gallery():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # HTML structure
    html_block = """
    <section class="meech-horizontal-scroll-container">
        <div class="meech-sticky-container">
            <div class="meech-gallery-track" id="meechTrack">
                <div class="meech-item item-1">
                    <img src="https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Fashion 1">
                </div>
                <div class="meech-item item-2">
                    <img src="https://images.pexels.com/photos/291762/pexels-photo-291762.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Fashion 2">
                </div>
                <div class="meech-item item-3">
                    <img src="https://images.pexels.com/photos/1536619/pexels-photo-1536619.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Fashion 3">
                </div>
                <div class="meech-item item-4">
                    <img src="https://images.pexels.com/photos/2043590/pexels-photo-2043590.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Fashion 4">
                </div>
                <div class="meech-item item-5">
                    <img src="https://images.pexels.com/photos/2787341/pexels-photo-2787341.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Fashion 5">
                </div>
                <div class="meech-item item-6">
                    <img src="https://images.pexels.com/photos/1858175/pexels-photo-1858175.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Fashion 6">
                </div>
                <div style="min-width: 20vw;"></div>
            </div>
            
            <div class="meech-bottom-menu">
                <div class="meech-menu-arc">
                    <a href="#" class="meech-menu-link">ABOUT</a>
                    <a href="#" class="meech-menu-link">VIDEO</a>
                    <a href="#" class="meech-menu-link">PHOTO</a>
                    <a href="#" class="meech-menu-link meech-active">HOME</a>
                    <a href="#" class="meech-menu-link">BOOK</a>
                </div>
                <div class="meech-line-container">
                    <div class="meech-diagonal-line"></div>
                </div>
            </div>
        </div>
    </section>
    """
    
    # CSS Styles
    css_block = """
    <style>
    .meech-horizontal-scroll-container {
        position: relative;
        width: 100%;
        height: 400vh;
        background-color: #f3f3f2;
        z-index: 100;
    }

    .meech-sticky-container {
        position: sticky;
        top: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        display: flex;
        align-items: center;
    }

    .meech-gallery-track {
        display: flex;
        align-items: center;
        gap: 12vw;
        padding-left: 10vw;
        will-change: transform;
        height: 100%;
        transform: translate3d(0, 0, 0);
    }

    .meech-item {
        flex-shrink: 0;
        transition: transform 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    .meech-item img {
        max-width: 35vw;
        max-height: 65vh;
        object-fit: contain;
        box-shadow: 10px 15px 40px rgba(0,0,0,0.2);
    }

    .item-1 { transform: rotate(-6deg) translateY(20px) scale(0.9); }
    .item-2 { transform: rotate(4deg) translateY(-40px) scale(1.1); }
    .item-3 { transform: rotate(-3deg) translateY(50px) scale(1.0); }
    .item-4 { transform: rotate(5deg) translateY(-20px) scale(0.85); }
    .item-5 { transform: rotate(-5deg) translateY(-60px) scale(1.15); }
    .item-6 { transform: rotate(2deg) translateY(40px) scale(0.95); }

    .meech-bottom-menu {
        position: absolute;
        bottom: 50px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: 'Times New Roman', Times, serif;
    }

    .meech-menu-arc {
        display: flex;
        gap: 40px;
        align-items: flex-end;
    }

    .meech-menu-link {
        color: rgba(0,0,0,0.2);
        text-decoration: none;
        font-size: 20px;
        letter-spacing: 2px;
        transition: color 0.3s, font-size 0.3s;
    }

    .meech-menu-link.meech-active {
        color: rgba(0,0,0,0.8);
        font-size: 26px;
    }

    .meech-menu-link:hover {
        color: rgba(0,0,0,0.8);
    }
    
    .meech-line-container {
        width: 100%;
        height: 60px;
        position: relative;
        margin-top: 10px;
    }

    .meech-diagonal-line {
        position: absolute;
        bottom: -20px;
        left: 50%;
        width: 150px;
        height: 1px;
        background-color: #000;
        transform-origin: left center;
        transform: rotate(-25deg);
    }
    
    .meech-diagonal-line::before {
        content: '';
        position: absolute;
        left: 0;
        top: -2px;
        width: 5px;
        height: 5px;
        border-radius: 50%;
        background-color: #000;
    }
    </style>
    """
    
    # JavaScript Logic
    js_block = """
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        const wrapper = document.querySelector('.meech-horizontal-scroll-container');
        const track = document.getElementById('meechTrack');
        
        if(!wrapper || !track) return;
        
        window.addEventListener('scroll', () => {
            const rect = wrapper.getBoundingClientRect();
            const scrollDistance = wrapper.offsetHeight - window.innerHeight;
            
            // Only translate if we are scrolling past the top of the wrapper
            if (rect.top <= 0 && scrollDistance > 0) {
                let scrollProgress = -rect.top / scrollDistance;
                scrollProgress = Math.max(0, Math.min(1, scrollProgress)); // clamp between 0 and 1
                
                // Maximum distance the track can be translated
                const maxTranslate = track.scrollWidth - window.innerWidth;
                
                // Add some easing using requestAnimationFrame (smooth scroll effect)
                const targetTranslateX = - (maxTranslate * scrollProgress);
                track.style.transform = `translate3d(${targetTranslateX}px, 0, 0)`;
            }
        });
    });
    </script>
    """

    # Check if we already injected it
    if soup.find('section', class_='meech-horizontal-scroll-container'):
        soup.find('section', class_='meech-horizontal-scroll-container').decompose()

    new_section = BeautifulSoup(html_block, 'html.parser')
    new_css = BeautifulSoup(css_block, 'html.parser')
    new_js = BeautifulSoup(js_block, 'html.parser')
    
    # Append to body
    soup.body.append(new_css)
    soup.body.append(new_section)
    soup.body.append(new_js)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    inject_gallery()
    print("Meech horizontal gallery injected successfully")

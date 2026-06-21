from bs4 import BeautifulSoup

def fix_gallery():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find the existing injected section and remove it
    old_section = soup.find('section', class_='meech-horizontal-scroll-container')
    if old_section:
        old_section.decompose()

    # Find the locomotive wrapper
    loco_wrap = soup.find('div', class_='locomotive-wrap')
    if not loco_wrap:
        print("No locomotive wrap found!")
        return

    # Add the section inside loco_wrap
    html_block = """
    <section class="meech-horizontal-scroll-container" id="meechTarget" data-scroll-section style="position: relative; width: 100%; height: 400vh; background-color: #f3f3f2; z-index: 100;">
        <div class="meech-sticky-container" data-scroll data-scroll-sticky data-scroll-target="#meechTarget" style="position: relative; width: 100vw; height: 100vh; overflow: hidden; display: flex; align-items: center;">
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
    
    new_section = BeautifulSoup(html_block, 'html.parser')
    loco_wrap.append(new_section)

    # We need a new JS script that uses requestAnimationFrame
    js_block = """
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        const wrapper = document.getElementById('meechTarget');
        const track = document.getElementById('meechTrack');
        
        if(!wrapper || !track) return;
        
        function updateScroll() {
            const rect = wrapper.getBoundingClientRect();
            // rect.top is the distance from the top of the viewport to the top of the wrapper.
            // Since it's inside Locomotive, rect.top changes as we scroll natively (via Loco transform).
            // scrollDistance is the total amount of vertical scroll available in the wrapper before the sticky breaks.
            const scrollDistance = wrapper.offsetHeight - window.innerHeight;
            
            if (scrollDistance > 0) {
                // Progress is 0 when rect.top == 0, and 1 when rect.top == -scrollDistance
                let scrollProgress = -rect.top / scrollDistance;
                scrollProgress = Math.max(0, Math.min(1, scrollProgress));
                
                const maxTranslate = track.scrollWidth - window.innerWidth;
                const targetTranslateX = - (maxTranslate * scrollProgress);
                
                track.style.transform = `translate3d(${targetTranslateX}px, 0, 0)`;
            }
            
            requestAnimationFrame(updateScroll);
        }
        
        requestAnimationFrame(updateScroll);
    });
    </script>
    """
    
    old_script = soup.find('script', text=lambda t: t and 'meechTrack' in t)
    if old_script:
        old_script.decompose()

    soup.body.append(BeautifulSoup(js_block, 'html.parser'))

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    fix_gallery()
    print("Meech gallery fixed for Locomotive Scroll")

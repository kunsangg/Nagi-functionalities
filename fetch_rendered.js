const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://antigravity.google/download', { waitUntil: 'networkidle2' });
    
    // Get the HTML content after rendering
    const content = await page.content();
    fs.writeFileSync('rendered_antigravity.html', content);
    
    // Also try to find all applied CSS rules on main elements
    const styles = await page.evaluate(() => {
        const getStyles = (selector) => {
            const el = document.querySelector(selector);
            if (!el) return null;
            const computed = window.getComputedStyle(el);
            return {
                selector,
                fontSize: computed.fontSize,
                fontWeight: computed.fontWeight,
                fontFamily: computed.fontFamily,
                margin: computed.margin,
                padding: computed.padding,
                color: computed.color,
                background: computed.background,
                display: computed.display,
                gridTemplateColumns: computed.gridTemplateColumns,
                gap: computed.gap
            };
        };
        return [
            getStyles('h1'),
            getStyles('.tabs-container, [role="tablist"], .tabs'),
            getStyles('.card, .os-card, [class*="card"]'),
            getStyles('main')
        ];
    });
    
    fs.writeFileSync('antigravity_styles.json', JSON.stringify(styles, null, 2));
    
    await browser.close();
    console.log("Done");
})();

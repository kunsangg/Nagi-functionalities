const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Some sites block headless browsers. Spoof user agent.
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36');
    
    await page.goto('https://antigravity.google/download', { waitUntil: 'networkidle0' });
    
    // Wait a bit to ensure rendering
    await new Promise(r => setTimeout(r, 5000));
    
    const content = await page.content();
    fs.writeFileSync('rendered_antigravity_full.html', content);
    
    await browser.close();
    console.log("Saved full rendered HTML");
})();

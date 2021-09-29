const puppeteer = require("puppeteer");

(async () => {
    const browser = await puppeteer.launch({
        "headless": false
    });

    const page = await browser.newPage();
    await page.goto("https://discord.com/login");

    await Promise.all([
        page.waitForSelector('[name="email"]'),
        page.waitForSelector('[name="password"]'),
      ]);
    
      // Enter username and password
    
      await page.type('[name="email"]', 'login here');
      await page.type('[name="password"]', 'password here');
    
      await Promise.all([
        page.click('[type="submit"]'),
        page.waitForNavigation({
          waitUntil: 'networkidle0',
        }),
      ]);

            // Join server

      await Promise.all([
        page.waitForSelector('[href="/channels/735810947175809045/735810947612016640"]'),
      ]);
    
    
    
      await Promise.all([
        page.click('[href="/channels/735810947175809045/735810947612016640"]'),
        page.waitForNavigation({
          waitUntil: 'networkidle0',
        }),
      ]);

    // Join VC

      await Promise.all([
        page.waitForSelector('[data-list-item-id="channels___735810947612016641"]'),
      ]);
    
    
    
      await Promise.all([
        page.click('[data-list-item-id="channels___735810947612016641"]'),
        page.waitForNavigation({
          waitUntil: 'networkidle0',
        }),
      ]);

    // Enable camera

      await Promise.all([
        page.waitForSelector('[aria-label="Turn on camera"]'),
      ]);
    
    
    
      await Promise.all([
        page.click('[aria-label="Turn on camera"]]'),
        page.waitForNavigation({
          waitUntil: 'networkidle0',
        }),
      ]);
    
    

})();
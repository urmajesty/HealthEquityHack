const puppeteer = require('puppeteer');
const jsdom = require("jsdom");

const init =async (site) => { 
    const browser = await puppeteer.launch();

    const page = await browser.newPage();
    await page.goto(site);

    const html =await page.content();
    const dom = await new jsdom(html);

    console.log(dom);
    await browser.close();
}

init('https://partnc.org');




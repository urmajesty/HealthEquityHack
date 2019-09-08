import { parse } from 'node-html-parser';
const puppeteer = require('puppeteer');

const init =async (site) => { 
    const browser = await puppeteer.launch();

    const page = await browser.newPage();
    await page.goto(site);

    const html =await page.content();
    const dom = await parse(html);

    console.log(dom.firstChild.structure);
    
    await browser.close();
}

init('https://partnc.org');




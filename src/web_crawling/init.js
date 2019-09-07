const puppeteer = require('puppeteer');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const init = async (site) => {
    try {
        const browser = await puppeteer.launch();

        const page = await browser.newPage();
        await page.goto(site);

        const results = await page.content();
        //console.log(results);
        /*for(line in results) {
            console.log(results[line]);
            // 
        }*/

        //global.DOMParser = new JSDOM().window.DOMParser
        console.log(new JSDOM().window.DOMParser)
        //const dom = (new JSDOM(results)).window.document.body;
        //const dom = new JSDOM(results);

        //console.log(dom);
        // loop through dom and get text content
        await browser.close();
    } catch (err) {
        console.log(err);
    }
}

init('https://blog.walterkjenkins.com/190826-Hosting-a-Static-Site-on-s3/');



} catch (err) {
    console.log(err);
}
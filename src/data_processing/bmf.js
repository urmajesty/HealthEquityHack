    const csv = require ('csv-parser')
    const fs = require('fs');
    const http = require ("https");
    const file = fs.createWriteStream("all.csv");
    require ('./bmf.js')


  http.get("https://slalom-hackathon.s3.us-east-2.amazonaws.com/MO+BMF+6.10.2019.csv", response => {
  response.pipe(file).on('data', (row) => {
    console.log(row); 
  })
  .on('end', () => {
    console.log('CSV file successfully processed');
    
  });
});

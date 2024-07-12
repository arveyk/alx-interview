#!/usr/bin/node
const process = require('process');
const https = require('https');
const argv = process.argv;

const endpoint = argv[2];
const url = 'https://swapi-api.alx-tools.com/api/' + 'films/' + endpoint + '/';

https.get(url, response => {
  let data = '';
  response.on('data', chunk => {
    data += chunk;
  });
  response.on('close', () => {
    const crew = JSON.parse(data);

    for (const actor of crew.characters) {
      https.get(actor, resp => {
        let actorResp = '';

        resp.on('data', (chunk) => {
          actorResp += chunk;
        });
        resp.on('close', () => {
          const individual = JSON.parse(actorResp);
          console.log(individual.name);
        });
      });
    }
  }).on('error', (err) => {
    console.error('Error:', err.message);
  });
});

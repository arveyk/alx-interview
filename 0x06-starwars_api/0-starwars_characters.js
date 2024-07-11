#!/usr/bin/node
const process = require('process');
const axios = require('axios');
const argv = process.argv;

const endpoint = argv[2];
const url = 'https://swapi-api.alx-tools.com/api/' + 'films/' + endpoint + '/';

axios.get(url).then(response => {
  const actors = response.data;
  const castArray = actors.characters;
  for (const actor of castArray) {
    axios.get(actor).then(resp => {
      const name = resp.data.name;
      console.log(name);
    }).catch(error => {
      console.error('Error:', error);
    });
  }
}).catch(error => {
  console.error('Error:', error);
});

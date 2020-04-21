const Twilio = require("twilio");

const client = new Twilio("Account SID goes here", "Auth Token Goes Here"); // DONT EVER PUT OUR KEYS JUST OUR THERE LIKE THIS. USE ENVIRONMENT VARIABLES.

client.messages.list()
    .then(messages =>
        console.log(`The most recent message is ${messages[0].body}`)
    ).catch(err => console.error(err));
    
    console.log('Gathering your message log.');
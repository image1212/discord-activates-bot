const Discord = require('discord.js');
const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });
const { DiscordTogether } = require('discord-together');


client.discordTogether = new DiscordTogether(client);

client.on('messageCreate', async message => {
    if (message.content === '!doodlecrew') {
        if(message.member.voice.channel) {
            client.discordTogether.createTogetherCode(message.member.voice.channel.id, 'doodlecrew').then(async invite => {
                return message.channel.send(`${invite.code}`);
            });
        };
    };
});

client.on('messageCreate', async message => {
    if (message.content === '!youtube') {
        if(message.member.voice.channel) {
            client.discordTogether.createTogetherCode(message.member.voice.channel.id, 'youtube').then(async invite => {
                return message.channel.send(`${invite.code}`);
            });
        };
    };
});

client.on('messageCreate', async message => {
    if (message.content === '!poker') {
        if(message.member.voice.channel) {
            client.discordTogether.createTogetherCode(message.member.voice.channel.id, 'poker').then(async invite => {
                return message.channel.send(`${invite.code}`);
            });
        };
    };
});

client.on('messageCreate', async message => {
    if (message.content === '!chess') {
        if(message.member.voice.channel) {
            client.discordTogether.createTogetherCode(message.member.voice.channel.id, 'chess').then(async invite => {
                return message.channel.send(`${invite.code}`);
            });
        };
    };
});

client.on('messageCreate', async message => {
    if (message.content === '!Betrayal') {
        if(message.member.voice.channel) {
            client.discordTogether.createTogetherCode(message.member.voice.channel.id, 'Betrayal').then(async invite => {
                return message.channel.send(`${invite.code}`);
            });
        };
    };
});

client.on('messageCreate', async message => {
    if (message.content === '!fishing') {
        if(message.member.voice.channel) {
            client.discordTogether.createTogetherCode(message.member.voice.channel.id, 'fishing').then(async invite => {
                return message.channel.send(`${invite.code}`);
            });
        };
    };
});

client.on('messageCreate', async message => {
    if (message.content === '!lettertile') {
        if(message.member.voice.channel) {
            client.discordTogether.createTogetherCode(message.member.voice.channel.id, 'lettertile').then(async invite => {
                return message.channel.send(`${invite.code}`);
            });
        };
    };
});

client.on('messageCreate', async message => {
    if (message.content === '!wordsnack') {
        if(message.member.voice.channel) {
            client.discordTogether.createTogetherCode(message.member.voice.channel.id, 'wordsnack').then(async invite => {
                return message.channel.send(`${invite.code}`);
            });
        };
    };
});

client.login("ㅌㅋ")

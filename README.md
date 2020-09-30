# Demo bot

This is a template, or rather a demonstration of a very basic discord bot for... educational purposes I guess?

Getting set up with discord.py is easy.
1. Follow [this link](https://www.python.org/downloads/) to install the latest version of python.
2. You may need to install [pip](https://pip.pypa.io/en/stable/installing/)
2. Read the [documentation](https://discordpy.readthedocs.io/en/latest/intro.html) to and how to install the discord ibrary.

---
Here are just some commands that are used for this particular bot:

### .hello
- Simply replies to command with "Hello World!"
- usage: ```.hello```

### .echo
- Simply repeats the user's input to echo.
- usage: ```.echo [Any message can go here]```

### .clear
- Purges the last 200 commands in the channel, and can only be used by users with manage message permissions.
- usage: ```.clear```

### .bubblewrap
- bubblewrap
- usage: ```.bubblewrap```

### .rickroll
- You know the rules, and so do I.
- Demonstrates how to use an embed.
- usage: ```.rickroll```

### .shutdown
- logs out the bot, and terminates the program
- can only be executed by the bot owner
- usage: ```.shutdown```

---

## Non-Commands

### On ready event
- The bot will print to the terminal "Bot is online"
- The bot will change its status to ```Playing a game```

### On message event
- Greets any user who says "hello"
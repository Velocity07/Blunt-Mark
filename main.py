#Run 'python -m pip install -U hikari' before you start
#Run 'pip install hikari-lightbulb' before you start

import hikari, lightbulb

bot = lightbulb.BotApp(token='YOUR_BOT_TOKEN',
#Required ^                    
    default_enabled_guilds=(YOUR_GUILD_ID))
#Too add more than one guild use: (YOUR_GUILD_ID, ANOTHER_GUILD_ID) (Used for loading commands faster in guilds)

#Load Commands
bot.load_extensions_from('./commands')
    
bot.run()

#Coded by Velocity7

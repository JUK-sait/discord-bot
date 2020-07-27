import discord
import secret
client = discord.Client()


@client.event
async def on_ready():
    print("-"*20)
    print(client.user.name)
    print(client.user.id)
    print("-"*20)


@client.event
async def on_message(message):
    if not message.author.bot:  # BOTの競合回避
        if message.content.startswith("!create"):
            secret.counter = secret.a[1]
            secret.a.clear()
            secret.a = message.content[8:].split("→")
            secret.bot_on = 1
            print(secret.a)

        elif message.content.startswith("!count"):
            await client.send_message("現在のカウント数{0}".format(str(secret.counter)))

        elif 1 == int(secret.bot_on):
            if message.content.startswith(""):
                    secret.counter += 1
                    if secret.counter == int(secret.a[0]):
                        msg = message.author.mention + "様　当選\n{0}".format(secret.a[1])
                        await client.send_message(message.channel, msg)
                        secret.counter - secret.a[1]


client.run(secret.token)

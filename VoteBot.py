import discord
from discord.ext import commands

with open("token", "r") as file:
    token = file.read().strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents = intents)

interacted_users_like = set()
interacted_users_dislike = set()
interacted_users_love = set()

interacted_users = {"like": interacted_users_like, "dislike": interacted_users_dislike, "love": interacted_users_love}

@bot.event
async def on_ready():
    print("Bot is online!")

class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Like", style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.message.id not in globals():
            globals()[interaction.message.id] = interacted_users
            globals()[interaction.message.id]["like"].clear()
            globals()[interaction.message.id]["dislike"].clear()
            globals()[interaction.message.id]["love"].clear()

            globals()[interaction.message.id]["like"].add(interaction.user.name)
        else:
            if interaction.user.name in globals()[interaction.message.id]["dislike"]:
                globals()[interaction.message.id]["dislike"].remove(interaction.user.name)

            if interaction.user.name in globals()[interaction.message.id]["love"]:
                globals()[interaction.message.id]["love"].remove(interaction.user.name)

            if interaction.user.name in globals()[interaction.message.id]["like"]:
                await interaction.response.send_message("You already like it!", ephemeral=True)
                return
            
        globals()[interaction.message.id]["like"].add(interaction.user.name)
        newEmbed = interaction.message.embeds[0]
        newEmbed.set_field_at(index=0,name="Like", value="\n".join(globals()[interaction.message.id]["like"]))
        newEmbed.set_field_at(index=1,name="Dislike", value="\n".join(globals()[interaction.message.id]["dislike"]))
        newEmbed.set_field_at(index=2,name="Love it", value="\n".join(globals()[interaction.message.id]["love"]))
        await interaction.response.edit_message(embed=newEmbed)


    @discord.ui.button(label="Dislike", style=discord.ButtonStyle.red)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.message.id not in globals():
            globals()[interaction.message.id] = interacted_users
            globals()[interaction.message.id]["like"].clear()
            globals()[interaction.message.id]["dislike"].clear()
            globals()[interaction.message.id]["love"].clear()

            globals()[interaction.message.id]["dislike"].add(interaction.user.name)
        else:
            if interaction.user.name in globals()[interaction.message.id]["like"]:
                globals()[interaction.message.id]["like"].remove(interaction.user.name)

            if interaction.user.name in globals()[interaction.message.id]["love"]:
                globals()[interaction.message.id]["love"].remove(interaction.user.name)

            if interaction.user.name in globals()[interaction.message.id]["dislike"]:
                await interaction.response.send_message("You already dislike it!", ephemeral=True)
                return
            
        globals()[interaction.message.id]["dislike"].add(interaction.user.name)
        newEmbed = interaction.message.embeds[0]
        newEmbed.set_field_at(index=0,name="Like", value="\n".join(globals()[interaction.message.id]["like"]))
        newEmbed.set_field_at(index=1,name="Dislike", value="\n".join(globals()[interaction.message.id]["dislike"]))
        newEmbed.set_field_at(index=2,name="Love it", value="\n".join(globals()[interaction.message.id]["love"]))
        await interaction.response.edit_message(embed=newEmbed)

    

    @discord.ui.button(label="Love it!", style=discord.ButtonStyle.blurple)
    async def opt3(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.message.id not in globals():
            globals()[interaction.message.id] = interacted_users
            globals()[interaction.message.id]["like"].clear()
            globals()[interaction.message.id]["dislike"].clear()
            globals()[interaction.message.id]["love"].clear()

            globals()[interaction.message.id]["love"].add(interaction.user.name)
        else:
            if interaction.user.name in globals()[interaction.message.id]["like"]:
                globals()[interaction.message.id]["like"].remove(interaction.user.name)

            if interaction.user.name in globals()[interaction.message.id]["dislike"]:
                globals()[interaction.message.id]["dislike"].remove(interaction.user.name)

            if interaction.user.name in globals()[interaction.message.id]["love"]:
                await interaction.response.send_message("You already love it!", ephemeral=True)
                return
            
        globals()[interaction.message.id]["love"].add(interaction.user.name)
        newEmbed = interaction.message.embeds[0]
        newEmbed.set_field_at(index=0,name="Like", value="\n".join(globals()[interaction.message.id]["like"]))
        newEmbed.set_field_at(index=1,name="Dislike", value="\n".join(globals()[interaction.message.id]["dislike"]))
        newEmbed.set_field_at(index=2,name="Love it", value="\n".join(globals()[interaction.message.id]["love"]))
        await interaction.response.edit_message(embed=newEmbed)


@bot.command()
async def poll(ctx, *,  message: str = ''):
    if (message == ''):
        await ctx.send("Your message can't be empty!")
        return

    view = Menu()
    
    await ctx.message.delete()

    embed = discord.Embed(title=f"{ctx.author.name} asks for your vote!", description=message, color=discord.Color.random())
    embed.add_field(name="Like:", value='', inline=True)
    embed.add_field(name="Dislike:", value='', inline=True)
    embed.add_field(name="Love It:", value='', inline=True)
    embed.set_footer(text="Your voice makes change!")
    await ctx.send(content= "@everyone", view = view, embed = embed)
    
   
bot.run(token)

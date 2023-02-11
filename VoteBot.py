# Import the necessary modules
import discord
from discord.ext import commands
from typing import Any

# Read the token from the file 'token'
with open("token", "r") as file:
    token = file.read().strip()

# Set the intents for the bot
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot with a command prefix '!' and the set intents
bot = commands.Bot(command_prefix='!', intents=intents)


# Define the class InteractedUsers
class InteractedUsers:
    def __init__(self):
        self.liked = set()
        self.disliked = set()
        self.loved = set()


# Create a dictionary to store all interacted users
interacted_users = {}


# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print("Bot is online!")


# Function to update the embed with the latest interaction data
def update_embed(embed: Any, msg_id: int):
    embed.set_field_at(index=0, name="Like", value="\n".join(interacted_users[msg_id].liked))
    embed.set_field_at(index=1, name="Dislike", value="\n".join(interacted_users[msg_id].disliked))
    embed.set_field_at(index=2, name="Love it", value="\n".join(interacted_users[msg_id].loved))
    return embed


# Define the class Menu
class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # Handler for the 'Like' option
    @discord.ui.button(label="Like", style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        msg_id = interaction.message.id
        usr_name = interaction.user.name

        # Check if the interaction message is not in the dictionary and create a new object if it's not
        if interaction.message.id not in interacted_users:
            interacted_users[msg_id] = InteractedUsers()

        # Check if the user already liked, loved, or disliked the message and remove the previous interaction if exists
        else:
            if usr_name in interacted_users[msg_id].disliked:
                interacted_users[msg_id].disliked.remove(usr_name)

            elif usr_name in interacted_users[msg_id].loved:
                interacted_users[msg_id].loved.remove(usr_name)

            elif usr_name in interacted_users[msg_id].liked:
                await interaction.response.send_message("You already like it!", ephemeral=True)
                return

        # Add the interacted user to the liked list
        interacted_users[msg_id].liked.add(usr_name)
        # call the update embed function and send the new embed to Discord
        await interaction.response.edit_message(embed=update_embed(interaction.message.embeds[0], msg_id))

    # Handler for the 'Dislike' option
    @discord.ui.button(label="Dislike", style=discord.ButtonStyle.red)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        msg_id = interaction.message.id
        usr_name = interaction.user.name

        # Check if the interaction message is not in the dictionary and create a new object if it's not
        if interaction.message.id not in interacted_users:
            interacted_users[msg_id] = InteractedUsers()

        # Check if the user already liked, loved, or disliked the message and remove the previous interaction if exists
        else:
            if usr_name in interacted_users[msg_id].liked:
                interacted_users[msg_id].liked.remove(usr_name)

            elif usr_name in interacted_users[msg_id].loved:
                interacted_users[msg_id].loved.remove(usr_name)

            elif usr_name in interacted_users[msg_id].disliked:
                await interaction.response.send_message("You already dislike it!", ephemeral=True)
                return

        # Add the interacted user to the disliked list
        interacted_users[msg_id].disliked.add(usr_name)
        # call the update embed function and send the new embed to Discord
        await interaction.response.edit_message(embed=update_embed(interaction.message.embeds[0], msg_id))

    # Handler for the 'Love it!' option
    @discord.ui.button(label="Love it!", style=discord.ButtonStyle.blurple)
    async def opt3(self, interaction: discord.Interaction, button: discord.ui.Button):
        msg_id = interaction.message.id
        usr_name = interaction.user.name

        # Check if the interaction message is not in the dictionary and create a new object if it's not
        if interaction.message.id not in interacted_users:
            interacted_users[msg_id] = InteractedUsers()

        # Check if the user already liked, loved, or disliked the message and remove the previous interaction if exists
        else:
            if usr_name in interacted_users[msg_id].liked:
                interacted_users[msg_id].liked.remove(usr_name)

            elif usr_name in interacted_users[msg_id].disliked:
                interacted_users[msg_id].disliked.remove(usr_name)

            elif usr_name in interacted_users[msg_id].loved:
                await interaction.response.send_message("You already love it!", ephemeral=True)
                return

        # Add the interacted user to the loved list
        interacted_users[msg_id].loved.add(usr_name)
        # call the update embed function and send the new embed to Discord
        await interaction.response.edit_message(embed=update_embed(interaction.message.embeds[0], msg_id))


@bot.command()
async def poll(ctx, *, message: str = ''):
    # Check if the message is empty and return an error message if so
    if message == '':
        await ctx.send("Your message can't be empty!")
        return

    # Create a Menu object
    view = Menu()

    # Delete the original message
    await ctx.message.delete()

    # Create an embed with the poll message, colors, fields and footer
    embed = discord.Embed(title=f"{ctx.author.name} asks for your vote!", description=message,
                          color=discord.Color.random())
    embed.add_field(name="Like:", value='', inline=True)
    embed.add_field(name="Dislike:", value='', inline=True)
    embed.add_field(name="Love It:", value='', inline=True)
    embed.set_footer(text="Your voice makes change!")
    # Send the embed to everyone in the channel with the "@everyone" mention
    await ctx.send(content="@everyone", view=view, embed=embed)

# Run the bot
bot.run(token)

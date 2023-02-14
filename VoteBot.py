# Import the necessary modules
import discord
from discord.ext import commands
from typing import Any
import random
import sys

# Try to open the token file for reading
try:
    with open("token", "r") as file:
        # If the file can be opened, read its contents and store it in the variable "token"
        token = file.read().strip()

# If a FileNotFoundError is raised (i.e., the file could not be found), catch the exception
except FileNotFoundError:
    # Print an error message indicating that the file could not be found
    print("The token file could not be found. Shutting down the bot...")
    # Exit the program with a return code of 1, indicating that an error occurred
    sys.exit(1)

# Titles to the polls
titles = [
    "Love it or leave it!",
    "Thumbs up or down?",
    "The ultimate choice: Love it, Like, or Dislike?",
    "How do you feel about this?",
    "Your chance to express your emotions!",
    "Share your love, like, or dislike!",
    "Emojis speak louder than words!",
    "Three options, one decision!",
    "Heart it, like it, or dislike it!",
    "Do you heart it, like it, or dislike it?",
    "Time to show your love, like, or dislike!",
    "Emote your reaction!",
    "Love, like, or dislike: which one wins?",
    "The power of emotions is in your hands!",
    "A simple choice: love, like, or dislike!",
    "Take a stand: Yay or Nay?",
    "The final call: Thumbs up or down?",
    "What's your choice?",
    "Ready to voice your opinion?",
    "Your opinion matters, share it now!",
    "Speak your mind.",
    "Weigh in on this.",
    "Express your thoughts.",
    "Share your thoughts with us.",
    "What's your take on this?"
]

# Footers to the polls
footers = [
    "Make your voice heard!",
    "Every vote counts!",
    "Have your say in this poll!",
    "Share your opinion with us!",
    "Join the discussion!",
    "Let's see what the community thinks!",
    "Your participation matters!",
    "Your choice counts!",
    "Make a difference with your vote!",
    "Get involved and cast your vote!",
    "We want to hear from you!",
    "Your vote could decide the outcome!",
    "Your input is valuable to us!",
    "Don't miss this chance to have your say!",
    "Let your voice be heard!",
    "Take part in shaping the future!",
    "Your voice matters, speak up!",
    "Make your mark with your vote!",
    "Be a part of the decision making!",
    "We're counting on you to weigh in!",
    "Have your say and make a difference!",
    "Join the conversation and have your say!",
    "Add your voice to the mix!",
    "Your thoughts are important to us!",
    "Your vote can help shape the future!",
    "Let's hear what you have to say!",
    "Have your voice heard loud and clear!",
    "Make your vote count and have your say!"
]

# Fields names
fields = {
    "like": "Liked",
    "dislike": "Disliked",
    "love": "Loved it"
}

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
    embed.set_field_at(index=0, name=fields["like"], value="\n".join(interacted_users[msg_id].liked))
    embed.set_field_at(index=1, name=fields["dislike"], value="\n".join(interacted_users[msg_id].disliked))
    embed.set_field_at(index=2, name=fields["love"], value="\n".join(interacted_users[msg_id].loved))
    return embed


# Define the class Menu
class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # Handler for the 'Like' option
    @discord.ui.button(label="Like", style=discord.ButtonStyle.green, emoji="👍🏼")
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
    @discord.ui.button(label="Dislike", style=discord.ButtonStyle.red, emoji="👎🏼")
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
    @discord.ui.button(label="Love it!", style=discord.ButtonStyle.blurple, emoji="❤️")
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
    # check if message and attachments are not empty
    if len(message) == 0 and len(ctx.message.attachments) == 0:
        await ctx.send("Your message can't be empty!", )
        return

    # create a view with Menu object
    view = Menu()

    # Delete the original message
    await ctx.message.delete()

    # create embed object with its fields
    embed = discord.Embed(description=message, color=discord.Color.random())
    embed.add_field(name=fields["like"], value='', inline=True)
    embed.add_field(name=fields["dislike"], value='', inline=True)
    embed.add_field(name=fields["love"], value='', inline=True)

    # check if there's any attachments
    if len(ctx.message.attachments) > 0:
        # create a poll for each attachment
        for img in ctx.message.attachments:
            embed.title = random.choice(titles)
            embed.set_footer(text=random.choice(footers))
            embed.set_image(url=img)
            await ctx.send(content="@everyone", view=view, embed=embed)
    else:
        # create a poll without attachments
        embed.title = random.choice(titles)
        embed.set_footer(text=random.choice(footers))
        await ctx.send(content="@everyone", view=view, embed=embed)


# Run the bot
bot.run(token)

# VoteBot

VoteBot is a Discord bot that allows users to react to messages with "Like," "Dislike," or "Love it" and keeps track of the users who have reacted to the messages.

## Features:

    - Users can interact with messages in the Discord channel by either liking, disliking, or loving a message.
    - The bot tracks the number of likes, dislikes, and loves for each message and displays them in a format that is easy to understand.
    - Users can only like, dislike, or love a message once, and the bot will inform them if they have already interacted with a message.

## Usage:

The bot uses the following prefix to recognize commands: `!`

To like a message, users can simply click on the green "Like" button. To dislike a message, users can click on the red "Dislike" button. To love a message, users can click on the purple "Love it" button. The bot will then update the number of likes, dislikes, and loves for that message and display the results in an embedded message.

## Technical Details:

The bot is built using the `discord.py` library and utilizes the `discord.ext.commands` and `discord.Intents` classes to handle interactions within the Discord channel. The bot stores information about the messages and user interactions in a global dictionary that is stored in memory. The bot updates this information every time a user interacts with a message.
Deployment

To deploy the bot, you will need to create a Discord Bot account and obtain a token that will be used to connect the bot to your Discord server. You will also need to have Python and the `discord.py` library installed on your machine. Once you have these requirements set up, you can run the bot code on your local machine or deploy it to a hosting service such as Heroku.

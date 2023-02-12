# VoteBot

VoteBot is a Discord bot that allows users to react to messages with "Like," "Dislike," or "Love it" and keeps track of
the users who have reacted to the messages.

## Features:

    - Users can interact with messages in the Discord channel by either liking, disliking, or loving a message.
    - The bot tracks the number of likes, dislikes, and loves for each message and displays them in a format that is easy to understand.
    - Users can only like, dislike, or love a message once, and the bot will inform them if they have already interacted with a message.

## Technical Details:

The bot is built using the `discord.py` library and utilizes the `discord.ext.commands` and `discord.Intents` classes to
handle interactions within the Discord channel. The bot stores information about the messages and user interactions in a
global dictionary that is stored in memory. The bot updates this information every time a user interacts with a message.
Deployment

To deploy the bot, you will need to create a Discord Bot account and obtain a token that will be used to connect the bot
to your Discord server. You will also need to have Python and the `discord.py` library installed on your machine if you want to run the bot on your local machine.
Once you have these requirements set up, you can run the bot code on your local machine, or alternatively you can use `Docker Container` to deploy it to a hosting service.

## Usage:

The bot uses the following prefix to recognize commands: `!`

### Text based poll:

To create a simple text based poll, you can type `!poll <TEXT>`

<img src="https://media.giphy.com/media/PSXfiZanRfcJeMCkFs/giphy.gif" alt="Create text based poll"/>

### Image based poll:

To create an image based poll, select the image you want to create poll about then type `!poll`.

optionally you can write a text to be shared with the image `!poll <TEXT>`. 

> **Note:** If you put multiple images in one poll command, the text will be displayed on all images.

<img src="https://media.giphy.com/media/QD8vTv3WVi9SiUmtZY/giphy.gif" alt="Create single image poll" style="margin-right: 10px"/>
<img src="https://media.giphy.com/media/qrmg54BAJePYwrDzpl/giphy.gif" alt="Create multiple images polls" style="margin-left: 10px"/>



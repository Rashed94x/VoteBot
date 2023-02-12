# VoteBot

<div style="width:100px; height:100px; border-radius:50%; overflow:hidden; display:inline-block;">
  <img src="./assets/logo.png" alt="Your Image" style="width:100%; height:auto;">
</div>

VoteBot is a Discord bot that allows users to react to messages with "Like," "Dislike," or "Love it" and keeps track of
the users who have reacted to the messages.

## Features:

    - Users can interact with messages in the Discord channel by either liking, disliking, or loving a message.
    - The bot tracks the number of likes, dislikes, and loves for each message and displays them in a format that is easy to understand.
    - Users can only like, dislike, or love a message once, and the bot will inform them if they have already interacted with a message.

## Technical Details:

The bot is built using the `discord.py` library and utilizes the `discord.ext.commands` classe to handle interactions
within the Discord channel.
The bot stores information about the messages and user interactions in a global dictionary that is stored in memory. The
bot updates this information every time a user interacts with a message.
Deployment

## Usage:

The bot uses the following prefix to recognize commands: `!`
And has currently only one command `poll`

> **NOTE:** The bot sends `@everyone` mention for all polls!

<img src="./assets/poll_1.png" alt="poll interface">

### Text based poll:

To create a simple text based poll, you can type `!poll <TEXT>`

<img src="./assets/basic_text.gif" alt="Create text based poll"/>

### Image based poll:

To create an image based poll, select the image you want to create poll about then type `!poll`.

optionally you can write a text to be shared with the image `!poll <TEXT>`.

> **Note:** If you put multiple images in one poll command, the text will be displayed on all images.

<img src="./assets/single_image.gif" alt="Create single image poll" style="margin-right: 10px"/>
<img src="./assets/multiple_images.gif" alt="Create multiple images polls" style="margin-left: 10px"/>



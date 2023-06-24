# Rocket League Tournament Discord Bot

A Discord bot designed to facilitate Rocket League tournaments with question-answering capabilities powered by OpenAI API. The bot is also equipped with Discord slash commands and email verification for enhanced user experience.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- Conduct Rocket League tournaments within a Discord server.
- OpenAI-powered question-answering capability based on trained datasets of frequently asked questions and the RLCS rulebook.
- Utilizes Discord slash commands for seamless and intuitive interaction.
- Email verification system to ensure secure and authentic participation.
- Easily customizable and extendable.

## Requirements

- [Python](https://www.python.org/) 3.7 or higher
- [Discord.py](https://discordpy.readthedocs.io/) library
- [OpenAI API](https://openai.com/) access and API key

## Installation

1. Clone this repository to your local machine or server.
```shell
git clone https://github.com/raaasin/rlcsdiscordbot
```

2. Install the required Python dependencies using pip.
```shell
pip install -r requirements.txt
```

3. Obtain an OpenAI API key by signing up at the [OpenAI website](https://openai.com/). Follow the API documentation to set up and obtain the necessary credentials.

4. Set up a MongoDB database or any other database of your choice to store user information and authentication data.

5. Configure the bot by creating a `creds.py` file in the project's root directory and fill in the following details:
```dotenv
TOKEN=<your_discord_bot_token>
open=<your_openai_api_key>
application_id=<your_discord_bot_application_id>
```

6. Run the bot by executing the main script.
```shell
python bot.py
```

## Usage

Once the bot is up and running, invite it to your Discord server using the OAuth2 URL generated for your bot. Ensure that the necessary permissions are granted to the bot for seamless functionality.

Use the provided slash commands to interact with the bot. For example, you can use the `/start_tournament` command to initiate a new Rocket League tournament or use the `/ask_question` command to ask a question about the tournament rules.




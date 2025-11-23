
# ✨ Motivational Quote Bot

A simple Telegram bot built with Python that sends a motivational quote every time a user prompts it with a specific command. Perfect for a quick pick-me-up\!

## 🌟 Features

  * **Simple Command Handling:** Responds to the `/start` and `/motivate` commands.
  * **Motivational Quotes:** Delivers an uplifting quote on demand.
  * **Easy Setup:** Minimal dependencies, easy to deploy.

## ⚙️ Setup and Installation

### Prerequisites

1.  **Python 3.8+**
2.  A **Telegram Bot Token** (Get one by talking to the official [@BotFather](https://t.me/BotFather)).
3.  A **Ninja api key** (Get one freely from [website](https://api-ninjas.com/api),

### 1\. Clone the Repository

```bash
mkdir motivational-quote-bot
cd motivational-quote-bot
git clone https://www.github.com/baboshi02/telegram_motivation/
cd motivational-quote-bot
```

### 2\. Set up the Environment

It's best practice to use a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows
```

### 3\. Install Dependencies


```bash
pip install -r requirements.txt
```

-----

## 🚀 Usage

### 1\. Configure the Bot Token

You need to tell the script your bot's secret token. You can do this by setting an environment variable  (though environment variables are more secure).


Set the `BOT_TOKEN` environment variable before running the script:

```bash
export TELEGRAM_API_KEY="YOUR_TELEGRAM_BOT_TOKEN_HERE"
export NINJA_API_KEY="YOUR_NINJA_API_KEY"
```

### 2\. Run the Bot

Execute your main bot script :

```bash
python main.py
# or
python3 main.py
```

Your bot is now running and listening for commands\!

### Bot Commands

  * **`/start`**: Sends a welcome message and introduction.
  * **`/motivate`**: Sends a random motivational quote.



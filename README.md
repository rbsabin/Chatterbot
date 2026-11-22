# Chatterbot

This project implements a simple terminal-based chatbot using Python, Django, and ChatterBot. The chatbot is trained using ChatterBot's English conversation corpus and allows the user to interact with it through the terminal.

## Technologies Used

- Python 3.12
- Django 6.1.3
- ChatterBot 1.2.17
- ChatterBot Corpus 1.3.3
- spaCy 3.8.18
- PyYAML 6.0.4

## Project Structure

```text
Chatterbot/
├── chatbot/
├── chatbot_project/
├── manage.py
├── terminal_client.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Install the English spaCy language model required by ChatterBot:

```bash
python -m spacy download en_core_web_sm
```

Run the Django system check:

```bash
python manage.py check
```

## Running the Chatbot

Start the terminal client with:

```bash
python terminal_client.py
```

The chatbot will train using the English conversation corpus when it starts.

Example:

```text
Chatbot started. Type 'exit' to quit.

user: Good morning! How are you doing?
bot: I am doing well, how about you?

user: What is your name?
bot: I am in the chat robot business.

user: exit
bot: Goodbye!
```

The user can type `exit` or `quit` to end the conversation.

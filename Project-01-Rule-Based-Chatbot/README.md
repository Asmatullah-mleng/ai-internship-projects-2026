# Rule-Based Chatbot

A lightweight, conversational chatbot built with Python that utilizes a rule-based knowledge base to provide intelligent responses to user queries.

## Overview

This project implements a simple yet effective rule-based chatbot that processes user input and returns predefined responses from a knowledge base. The chatbot is designed to handle common conversational patterns such as greetings, farewells, and casual inquiries.

## Features

- **Knowledge Base System**: Predefined responses for a variety of user inputs
- **Case-Insensitive Input**: Normalizes user input for consistent matching
- **Interactive Conversation**: Real-time chat interface with continuous conversation support
- **Graceful Exit**: Multiple exit commands (`bye`, `goodbye`, `exit`, `quit`) to terminate the chatbot

## Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies required

### Installation

1. Clone or download the repository to your local machine
2. Navigate to the project directory:
   ```bash
   cd Project-01-Rule-Based-Chatbot
   ```

### Usage

Run the chatbot from the command line:

```bash
python main.py
```

Once launched, interact with the chatbot by typing your messages. The chatbot will respond based on its knowledge base:

```
==========Hello! I'm a simple rulebase chatbot.==================================================
You: hello
Bot: Hello! How can I help you?
You: how are you
Bot: I'm doing great! Thanks for asking.
You: bye
Bot: Goodbye! Have a great day!
```

## Supported Interactions

The chatbot recognizes the following inputs and provides corresponding responses:

| User Input | Bot Response |
|-----------|-----------|
| hello, hi | Greeting responses |
| good morning/afternoon/evening | Time-based greetings |
| how are you | Status inquiry responses |
| nice to meet you | Friendly reply |
| who are you | Chatbot identification |
| bye, goodbye, exit, quit | Farewell messages |

## Project Structure

```
Project-01-Rule-Based-Chatbot/
├── main.py          # Main chatbot implementation
└── README.md        # Project documentation
```

## How It Works

1. The chatbot maintains a `knowledge_base` dictionary with key-value pairs
2. User input is converted to lowercase and stripped of whitespace
3. The chatbot looks up the input in the knowledge base
4. If a match is found, the corresponding response is displayed
5. If no match is found, a default message ("Sorry, I don't   understand that.") is shown
6. The conversation continues until the user enters an exit command


## Author

Developed as part of the AI Internship Projects 2026


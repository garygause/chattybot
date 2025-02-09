# chattybot

LangChain chatbot with memory.

## Installation

Clone the repo.

```bash
git clone https://github.com/garygause/chattybot
```

Install python 3.11.10 (optional):

```bash
pyenv install 3.11.10
```

Install dependencies and load env:

```bash
cd chattybot
poetry install
poetry env activate
```

Add your api keys to .env file.

## Running

```bash
poetry env activate
poetry run python chattybot/cli.py
```

## Example Output

```bash
ChattyBot - an ai chat bot. Type 'exit' to quit.
chatty >> what is my name
I'm sorry, I can't remember your name. I must have been too busy memorizing cat videos and pizza recipes. What's your name again?
chatty >> my name is gary
Nice to meet you, Gary! How can I assist you today?
chatty >> my favorite color is red
Red, the color of passion, love, and stop signs. A classic choice, Gary! Anything else you'd like to share about your favorite things?
chatty >> my fav city is seattle
Ah, Seattle - known for its coffee, rain, and the Space Needle. A great choice, Gary! Have you visited Seattle before, or are you dreaming of sipping coffee in the Emerald City?
chatty >> i love cats
Ah, a fellow cat lover! Cats truly rule the internet, don't they? What is it about our feline friends that captivates you, Gary?
chatty >> say my name
Gary, Gary, bo-bary, banana-fana fo-fary, fee-fi-mo-mary, Gary! How was that, Gary?
chatty >> exit
```

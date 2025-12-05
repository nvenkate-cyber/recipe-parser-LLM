from dotenv import load_dotenv
import os
from google import genai

from google.genai.types import Part, UserContent

import time
import json
import sys

try:
    import recipe_scraper
except ImportError as e:
    print(f"CRITICAL ERROR: Could not import necessary modules. {e}")
    sys.exit(1)


_DELAY_MULTIPLIER = 1.0  # Set to 0.0 to skip delays during testing

def slow_print(*args, delay=0.02):
    """Prints text character-by-character for a 'typing' effect."""
    text = ''.join(str(arg) for arg in args)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(_DELAY_MULTIPLIER * delay)
    print()

def word_print(*args, delay=0.15):
    """Prints word-by-word."""
    text = ' '.join(str(arg) for arg in args)
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(_DELAY_MULTIPLIER * delay)
    print() 

def tactical_pause(seconds=0.35):
    time.sleep(_DELAY_MULTIPLIER * seconds)

def load_recipe_data():
    """Safely loads recipe.json"""
    path = "recipe.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def scrape_and_parse(url: str):
    recipe_scraper.main(url)
    slow_print("Scraping complete!")

def startup_base():
    """Initial setup: URL input, Scraping, Parsing, Display Summary"""
    slow_print("What recipe would you like to cook today?")
    url = input("\nEnter recipe url (or press Enter to use existing recipe.json): ").strip()
    
    if url:
        slow_print("\nGreat! Let's scrape and parse this delicious recipe!")
        tactical_pause()
        scrape_and_parse(url)
        tactical_pause(3)
    
    # Reload data here to ensure we have the fresh scrape results
    recipe_data = load_recipe_data()
    
    if not recipe_data:
        slow_print("Error: No recipe.json found. Please provide a URL first.")
        return None

    slow_print("Let's see what we have!")
    word_print("\nRecipe Details:\n", delay=0.3)
    word_print("Title:", recipe_data.get("title", "Unknown"))
    word_print("Total time:", recipe_data.get("total_time", "Unknown"))
    word_print("Yield:", recipe_data.get("yield", "Unknown"))
    
    word_print("\nIngredients List:")
    for ingredient in recipe_data.get("ingredients", []):
        # Handle cases where ingredient might be a string or a dict
        if isinstance(ingredient, dict):
            # Combine qty, unit, name
            line = f"- {ingredient.get('qty', '')} {ingredient.get('unit', '')} {ingredient.get('name', '')}"
            print(line)
        else:
            print(f"- {ingredient}")
        time.sleep(0.05)
        
    print("\n")
    return recipe_data

recipe_data = startup_base()
recipe_json_snippet = json.dumps(recipe_data, ensure_ascii=False, indent=2)

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Load system prompt
system_prompt = open("unified_system_prompt.txt").read()

# Create an ongoing chat
chat = client.chats.create(
    model="gemini-2.5-flash",
    history=[
        UserContent(parts=[Part(text=f"Here is the recipe data I am cooking with:\n{recipe_json_snippet}")]),
        {"role": "model", "parts": [{"text": system_prompt}]}
    ]
)

print("Gemini assistant initialized. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        break

    # Print the model's response text
    response = chat.send_message(user_input)
    print("Assistant: ", response.text)
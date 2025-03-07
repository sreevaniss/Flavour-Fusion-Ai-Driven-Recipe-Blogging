import streamlit as st
import google.generativeai as genai
from google.generativeai import GenerativeModel
import random

# Configure your Google Generative AI API key
api_key = "AIzaSyBd7bw7tdrnf0xqh-RyQl8XC9oTcecEsr8"  
genai.configure(api_key=api_key)
# List available models for troubleshooting
print("Available models:")
for m in genai.list_models():
    print(m)

# Configure the model generation settings
generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the Gemini Pro model
model = GenerativeModel('gemini-1.5-pro-latest', generation_config=generation_config) #or gemini-1.5-pro, or a gemini 2.0 model.
# Function to generate a joke
def get_joke():
    jokes = [
        "Why Don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why don't programmers like nature? It has too many bugs!",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do python programmers prefer using snake_case? Because it is easier to read!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why do the developer go broke? Because he used up all his cache.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
        "Why did the programmer get kicked out of the beach? Because he kept using 'C' language!",
        "Why was the computer cold? It left its windows open."
    ]
    return random.choice(jokes)

def recipe_generation(user_input, word_count):
    """
    Function to generate a recipe based on user input and word count.
    Parameters:
    user_input(str): The topic for the recipe.
    word_count(int): The desired number of words for the recipe.
    Returns:
    str: The generated recipe content.
    """
    # Display a message while the recipe is being generated
    st.write("### Generating your recipe...")
    st.write(f"While I work on creating your recipe, here's a little joke to keep you entertained:\n\n**{get_joke()}**")

    # Build the prompt based on user input and word count
    prompt = f"Create a recipe for {user_input} with a word count of {word_count} words."

    try:
        # Use Google Generative AI API to generate the response
        response = model.generate_content(prompt)

        # Check if the response is valid
        if response and response.text:
            st.success("Your recipe is ready!")
            return response.text
        else:
            st.error("Error generating recipe.")
            return None
    except Exception as e:
        st.error(f"Error generating recipe: {e}")
        return None

# Streamlit interface to get user input
st.title("Recipe Generator")
user_input = st.text_input("Enter the topic for the recipe:", "Pasta")
word_count = st.slider("Select the word count:", min_value=100, max_value=1000, value=300)

# Generate the recipe based on user input
if st.button("Generate Recipe"):
    recipe = recipe_generation(user_input, word_count)
    if recipe:
        st.write(recipe)
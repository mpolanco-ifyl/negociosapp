import streamlit as st
import openai
import pandas as pd

# Authenticate OpenAI API key
openai.api_key = "your_api_key"

# Define function to generate startup idea
def generate_idea(wish):
    prompt = f"I wish there's a {wish}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    idea = response.choices[0].text.strip()
    return idea

# Define Streamlit app
def app():
    st.title("Digital Startup Idea Generator")

    # Ask for user input
    user_wish = st.text_input("What do you wish for?")

    if st.button("Generate Idea"):
        # Generate startup idea using GPT
        startup_idea = generate_idea(user_wish)

        # Format startup idea as a dataframe
        idea_df = pd.DataFrame({
            "Idea Name": [startup_idea],
            "Short Description": ["A digital startup that solves the user's pain points."],
            "Target User Persona": ["[insert target user persona]"],
            "User's Pain Points": ["[insert user's pain points to solve]"],
            "Main Value Propositions": ["[insert main value propositions]"],
            "Sales & Marketing Channels": ["[insert sales & marketing channels]"],
            "Revenue Stream Sources": ["[insert revenue stream sources]"],
            "Cost Structures": ["[insert cost structures]"],
            "Key Activities": ["[insert key activities]"],
            "Key Resources": ["[insert key resources]"],
            "Key Partners": ["[insert key partners]"],
            "Idea Validation Steps": ["[insert idea validation steps]"],
            "Estimated 1st Year Cost of Operation": ["[insert estimated 1st year cost of operation]"],
            "Potential Business Challenges": ["[insert potential business challenges to look for]"]
        })

        # Display startup idea as a markdown table
        st.write(idea_df.to_markdown(index=False), unsafe_allow_html=True)

# Run Streamlit app
if __name__ == '__main__':
    app()

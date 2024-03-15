""" This code runs a full debate between the OpenAI and Google
AIs on a specified debate topic. 

The debate transcript is passed back and forth during the 
debate as context for the response by each AI.

To run this code, you must have OpenAI and Google accounts
with authentication keys to use APIs for GPT 4 Turbo, 
OpenAI text-to-speech, Gemini Pro, and Google Cloud 
Text-to-Speech.

In the current version, debate is conducted without 
pause, and the different responses are output to 
mp3 files.
"""

from pathlib import Path
from random import choice
import google.generativeai as genai
from openai import OpenAI

# Local imports
from text_to_speech import text_to_speech

client = OpenAI

debate_topic = "Standardized testing should be abolished."

# In seconds!
time_limits = {
    'opening_statement': 180,
    'arguments': 180,
    'rebuttal': 120,
    'closing_statement': 120
}

def get_response_from_openai(client, context, prompt):
    full_prompt = context + "\n" + prompt

    try:
        response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are a master debater with encyclopedic knowledge of facts and history and extraordinary communication skills."},
                {"role": "user", "content": full_prompt}
            ] 
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_response_from_gemini(client, context, prompt):
    full_prompt = context + "\n" + prompt

    try:
        response = client.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

class DebateManager:
    def __init__(self, topic, time_limits):
        self.topic = topic
        self.time_limits = time_limits
        self.context = ""  # Initialize the debate context
        self.openai_client = OpenAI()  # Initialize OpenAI client
        self.gemini_client = genai.GenerativeModel('gemini-pro')
        self.affirmative_debator = None
        self.negative_debator = None

    def start_debate(self):
        # Start the debate process

        intro_text_part1 = f"""Welcome to the very first of the Great AI Debates. 
        
        This debate will be conducted by me - your human host, Alex Leeds - 
        and feature two of the latest Artificial Intelligences: Open AI's GPT 4 
        Turbo arguing against Google's Gemini Pro. 
        
        Our debate topic for tonight is the following resolution: 

        {self.topic}
        
        This debate will consist of four rounds. Each debater will take turns
        presenting an opening statement, a round of arguments, a rebuttal,
        and a closing statement.

        We will flip a digital coin to determine which AI takes each side. Doing that right now…\n 
        """

        # Randomly determine affirmative and negative debators
        opponents = ["GPT 4", "Gemini Pro"]
        self.affirmative_debator = choice(opponents)
        opponents.remove(self.affirmative_debator)
        self.negative_debator = opponents[0]

        intro_text_part2 = f"""{self.affirmative_debator} will be taking the affirmative position. 
        
        {self.negative_debator} will be taking the negative position.
        
        Without further ado, let's begin the debate."""

        full_intro = intro_text_part1 + intro_text_part2

        self.context += full_intro
        print(full_intro)
    
    def run_debate_speech(self, round_title, round_prompt, speaker, affirmative):

        # affirmative round title for transcript
        if affirmative:
            speech_title = f"{speaker}'s {round_title} (Affirmative)" 
        else:
            speech_title = f"{speaker}'s {round_title} (Negative)"
       
        # Prompt that looks like this f"{speaker}, you have 3 minutes to present your opening statement:"
        prompt = f"{speaker}, {round_prompt}"
        self.context += ("\n" + prompt)
        
        # get response from AI
        if speaker == "GPT 4":
            response = get_response_from_openai(self.openai_client, self.context, prompt)
            text_to_speech(response, speech_title, provider="openai")
        else:
            response = get_response_from_gemini(self.gemini_client, self.context, prompt)
            text_to_speech(response, speech_title, provider="google")

        # add response to transcript
        self.context += f"{speech_title}:\n {response}\n"
        
        print(f"{speech_title}:\n {response}\n")

        return None
    
    def conduct_opening_statements(self):

        round_title = "Opening Statement"
        opening_prompt = f"you have {time_limits['opening_statement']/60} minutes to present your opening statement:"
        
        # Affirmative opening statement
        self.run_debate_speech(round_title, opening_prompt, self.affirmative_debator, affirmative=True)

        # Negative opening statement
        self.run_debate_speech(round_title, opening_prompt, self.negative_debator, affirmative=False)

        return None
        
    def conduct_arguments(self):
        # Manage the argument rounds
        # Implement argument rounds

        argument_introduction = """That concludes our opening statements. We will now have one
        round of arguments by each side followed by a round of rebuttals by each side."""

        self.context += argument_introduction
        print(argument_introduction)

        round_title = "Arguments"
        arguments_prompt = f"you have {time_limits['arguments']/60} minutes to present your arguments:"
        
        # Affirmative arguments
        self.run_debate_speech(round_title, arguments_prompt, self.affirmative_debator, affirmative=True)

        # Negative arguments
        self.run_debate_speech(round_title, arguments_prompt, self.negative_debator, affirmative=False)

        return None

    def conduct_rebuttals(self):
        # Implement rebuttal rounds

        rebuttal_introduction = """Each side now has an opportunity for rebuttal."""

        round_title = "Rebuttal"
        rebuttal_prompt = f"you have {time_limits['rebuttal']/60} minutes to present your rebuttal:"
        
        # Affirmative rebuttal
        self.run_debate_speech(round_title, rebuttal_prompt, self.affirmative_debator, affirmative=True)

        # Negative rebuttal
        self.run_debate_speech(round_title, rebuttal_prompt, self.negative_debator, affirmative=False)

        return None

    def conduct_closing_statements(self):

        closing_introduction = """Each side may now conduct their closing statements."""

        print(closing_introduction)
        self.context += closing_introduction

        round_title = "Closing Statements"
        closing_prompt = f"you have {time_limits['rebuttal']/60} minutes to present your closing statement:"
        
        # Affirmative closing statement
        self.run_debate_speech(round_title, closing_prompt, self.affirmative_debator, affirmative=True)

        # Negative closing statement
        self.run_debate_speech(round_title, closing_prompt, self.negative_debator, affirmative=False)

        return None

if __name__ == '__main__':
    debate_manager = DebateManager(debate_topic, time_limits)
    debate_manager.start_debate()
    debate_manager.conduct_opening_statements()
    debate_manager.conduct_arguments()
    debate_manager.conduct_rebuttals()
    debate_manager.conduct_closing_statements()
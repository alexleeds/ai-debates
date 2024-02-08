import google.generativeai as genai
from openai import OpenAI
from random import choice

# openai.api_key = 'your_openai_api_key'
# gemini.api_key = 'your_gemini_api_key'

debate_topic = "All Americans should be required to vote."

time_limits = {
    'opening_statement': 180,
    'argument': 180,
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

        intro_text_part1 = """Welcome to the very first of the Great AI Debates. 
        
        This debate will be conducted by me - your human host, Alex Leeds - 
        and feature two of the latest Artificial Intelligences: Open AI's GPT 4 
        Turbo arguing against Google's Gemini Pro. 
        
        Our debate topic for tonight is the following resolution: 

        “All Americans should be required to vote.” 
        
        This debate will consist of four rounds. Each debater will take turns
        presenting an opening statement, a round of arguments, a round of rebuttals,
        and a closing statement.

        We will flip a digital coin to determine which AI takes each side. Doing that right now…\n 
        """

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
    
    def get_response(self, speaker, prompt):
        # Get response based on which AI is the speaker
        if speaker == "GPT 4":
            return get_response_from_openai(self.openai_client, self.context, prompt)
        else:
            return get_response_from_gemini(self.gemini_client, self.context, prompt)
    
    def conduct_opening_statements(self):

        # Affirmative opening statement
        affirm_opening_prompt = f"{self.affirmative_debator}, you have 3 minutes to present your opening statement:"
        affirmative_response = self.get_response(self.affirmative_debator, affirm_opening_prompt)
        self.context += affirm_opening_prompt
        print(f"{self.affirmative_debator}'s Opening Statement (Affirmative):")
        print(affirmative_response + "\n")
        self.context += f"{self.affirmative_debator}'s Opening Statement (Affirmative): {affirmative_response}\n"

        # Print and store opening statements for the negative debator
        negative_opening_prompt = f"{self.negative_debator}, you have 3 minutes to present your opening statement:"
        negative_response = self.get_response(self.negative_debator, negative_opening_prompt)
        self.context += negative_opening_prompt
        print(f"{self.negative_debator}'s Opening Statement (Negative):")
        print(negative_response + "\n")
        self.context += f"{self.negative_debator}'s Opening Statement (Negative): {negative_response}\n"

    def conduct_arguments(self):
        # Manage the argument rounds
        # Implement argument rounds

        argument_introduction = """That concludes our opening statements. We will now have one
        round of arguments by each side followed by a round of rebuttals by each side."""

        print(argument_introduction)
        self.context += argument_introduction

        # Affirmative Argument
        affirm_argument_prompt = f"{self.affirmative_debator}, you have 3 minutes to present your arguments:"
        affirmative_argument = self.get_response(self.affirmative_debator, affirm_argument_prompt)
        self.context += affirm_argument_prompt
        print(f"{self.affirmative_debator}'s Affirmative Arguments:")
        print(affirmative_argument + "\n")
        self.context += f"{self.affirmative_debator}'s Affirmative Arguments: {affirmative_argument}\n"
        
        # Negative Argument
        negative_argument_prompt = f"{self.negative_debator}, you have 3 minutes to present your arguments:"
        negative_argument = self.get_response(self.negative_debator, negative_argument_prompt)
        self.context += negative_argument_prompt
        print(f"{self.negative_debator}'s Negative Arguments:")
        print(negative_argument + "\n")
        self.context += f"{self.negative_debator}'s Negative Arguments: {negative_argument}\n"

    def conduct_rebuttals(self):
        # Implement rebuttal rounds

        rebuttal_introduction = """Each side now has an opportunity for rebuttal."""

        print(rebuttal_introduction)
        self.context += rebuttal_introduction
            
        # Affirmative Rebuttal
        affirm_rebuttal_prompt = f"{self.affirmative_debator}, you have 2 minutes for your rebuttal:"
        affirmative_rebuttal = self.get_response(self.affirmative_debator, affirm_rebuttal_prompt)
        self.context += affirm_rebuttal_prompt
        print(f"{self.affirmative_debator}'s Rebuttal:")
        print(affirmative_rebuttal + "\n")
        self.context += f"{self.affirmative_debator}'s Rebuttal: {affirmative_rebuttal}\n"
        
        # Negative Rebuttal
        neg_rebuttal_prompt = f"{self.negative_debator}, you have 2 minutes for your rebuttal:"
        negative_rebuttal = self.get_response(self.negative_debator, neg_rebuttal_prompt)
        self.context += neg_rebuttal_prompt
        print(f"{self.negative_debator}'s Rebuttal:")
        print(negative_rebuttal + "\n")
        self.context += f"{self.negative_debator}'s Rebuttal: {negative_rebuttal}\n"

    def conduct_closing_statements(self):

        closing_introduction = """Each side may now conduct their closing statements."""

        print(closing_introduction)
        self.context += closing_introduction

        # Affirmative Closing Statement
        affirm_closing_prompt = f"{self.affirmative_debator}, you have 2 minutes for your closing statements:"
        affirmative_closing_statement = self.get_response(self.affirmative_debator, affirm_closing_prompt)
        print(f"{self.affirmative_debator}'s Closing Statement:")
        print(affirmative_closing_statement + "\n")
        self.context += f"{self.affirmative_debator}'s Closing Statement: {affirmative_closing_statement}\n"
            
        # Negative Closing Statement
        neg_closing_prompt = f"{self.negative_debator}, you have 2 minutes for your closing statements:"
        negative_closing_statement = self.get_response(self.negative_debator, neg_closing_prompt)
        print(f"{self.negative_debator}'s Closing Statement:")
        print(negative_closing_statement + "\n")
        self.context += f"{self.negative_debator}'s Closing Statement: {negative_closing_statement}\n"

if __name__ == '__main__':
    debate_manager = DebateManager(debate_topic, time_limits)
    debate_manager.start_debate()
    debate_manager.conduct_opening_statements()
    debate_manager.conduct_arguments()
    debate_manager.conduct_rebuttals()
    debate_manager.conduct_closing_statements()
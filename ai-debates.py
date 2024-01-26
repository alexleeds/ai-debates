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

def get_response_from_openai(client, prompt):
    try:
        response = client.Completion.create(
            engine="gpt-4-0125-preview", 
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_response_from_gemini(client, prompt):
    try:
        response = model.generate_content("What is the meaning of life?")
    pass

class DebateManager:
    def __init__(self, topic, time_limits):
        self.topic = topic
        self.time_limits = time_limits
        self.debate_context = ""  # Initialize the debate context
        self.openai_client = OpenAI()  # Initialize OpenAI client
        self.gemini_client = genai.GenerativeModel('gemini-pro')

    def conduct_opening_statements(self):
        print("Starting the opening statements...\n")

        # OpenAI's opening statement
        openai_prompt = f"Provide an opening statement for a debate on the topic: '{self.topic}'"
        openai_opening_statement = get_response_from_openai(self.openai_client, openai_prompt)
        print("OpenAI's Opening Statement:")
        print(openai_opening_statement + "\n")
        self.debate_context += f"OpenAI: {openai_opening_statement}\n"

        # Gemini's opening statement
        gemini_prompt = f"Provide an opening statement for a debate on the topic: '{self.topic}'"
        gemini_opening_statement = get_response_from_gemini(self.gemini_client, gemini_prompt)
        print("Gemini's Opening Statement:")
        print(gemini_opening_statement + "\n")
        self.debate_context += f"Gemini: {gemini_opening_statement}\n"


    def conduct_argument_rounds(self):
        # Manage the argument and rebuttal rounds
        pass

    def conduct_closing_statements(self):
        # Manage the closing statements
        pass

    def start_debate(self):
        # Start the debate process
        pass

    def debate_opening(self):
        intro_text_part1 = """Welcome to the very first of the Great AI Debates. 
        This debate will be conducted by me - your human host, Alex Leeds - 
        and feature two of the latest Artificial Intelligences: Open AI's GPT 4 
        Turbo debating against Google's Gemini Pro. 
        
        Our debate topic for tonight is the following resolution: 

        “All Americans should be required to vote.” 
        
        We will flip an artificial coin to determine the sides. Doing that right now…\n 
        """

        opponents = ["GPT 4", "Gemini Pro"]
        affirmative_debator = choice(opponents)
        opponents.remove(affirmative_debator)
        negative_debator = opponents[0]

        intro_text_part2 = f"""{affirmative_debator} will be arguing this topic in the affirmative. 
        {negative_debator} will be arguing the negative.
        """

if __name__ == '__main__':
    debate_manager = DebateManager(debate_topic, time_limits)
    debate_manager.start_debate()
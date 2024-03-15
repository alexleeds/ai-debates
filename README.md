# The Great AI Debates

This project runs a full spoken debate between AIs. Each AI in the debate provides an opening statement, arguments, rebuttal, and closing statement. The debate can, of course, be run on chosen topic. 

The goal of this project is to run real, entertaining debates in front of a live (human!) audience. The first of these debates will be conducted on March 19, 2024 at [Astronomer's](https://www.astronomer.io/) headquarters in NYC.

## Description

You have probably seen fascinating responses written by GPT-4, Gemini, and other AI models. But you may never heard these AIs speak in a context where they are conversing with each other.

This project explores the boundaries of an eerie and magical moment when [AI seems human](https://www.youtube.com/watch?v=uCWKZWieMSY).

This project also tests the limit of AIs in a format where they tend to do extremely well: Short arguments to support a general question. At the same time, the simple debate structure allows for some fascinating and important experiments:

1. How well does text-to-speech to produce natural-sounding debate speech? This is a demanding test because formal debate includes long expositions. Using correct intonation requires the speaker to "understand" the meaning of the text. This is a different generative AI problem from producing text itself.
2. How well can automatic video generation produces realistic or animated figures to speak during the debate? This is also likely to be a generative AI problem, and it is the focus of many applications including [Synthesia](https://www.synthesia.io/) to [NVIDIA audio2face](https://www.nvidia.com/en-us/omniverse/apps/audio2face/).
3. How much can we improve AI debate performance by allowing AIs to either search libraries of prepared material or conduct research and debate preparation before speaking. This is a slightly different problem from the standard use case of [RAGs](https://aws.amazon.com/what-is/retrieval-augmented-generation/) but is a fairly common problem in organizational contexts where arguments are constructed from many sub-arguments that may each be deep and demanding.

The current code only explores this first topic, but we are excited to explore these other challenges as we conduct AI debates.

## Getting Started

### Dependencies

The Great AI Debates are run using Python to interface with OpenAI and Google Cloud.

- `pip install -r requirements.txt` to install dependencies
- The main requirements to run an AI debate are the OpenAI `openai` and Google Cloud `generativeai` and `texttospeech` libraries.

This code has only been tested on recent Mac operating systems with Python version 3.12.1. Adjustments may have to be made for other operating systems, but the OpenAI and Google Cloud libraries should have minimal OS dependencies.

This version of the code conducts a debate between Open AI's GPT 4 Turbo and Google Gemini Pro. The choice of which AI argues the "affirmative" position in the debate and which AI argues the "negative" position is randomly decided in the `start_debate()` function.

For fun and authenticity, OpenAI's text-to-speech API is used to create the voice (audio) for GPT 4 and Google Cloud's text-to-speech API is used to create the voice for Gemini.

If you have any trouble using the APIs provided by Google or OpenAI, it would be possible to modify the code to have either OpenAI's GPT 4 or Google's Gemini debate with itself (or to only use one source for text-to-speech). For instance, the function `run_debate_speech()` could be changed to use only `get_response_from_openai()` for the text of the response or `text_to_speech(response, speech_title, provider="openai")` to use only OpenAI for text-to-speech.

### Executing program

#### Running a debate

- Run `python ai-debates.py` at the command line in the main project directory to conduct the debate.

- If it does not already exist, an `audio_files` folder will be created in the main project directory to store the AI's speeches for all rounds of the debate.

- `start_debate()` contains a debate introduction that is provided to the AIs as the prompt to start the debate and also printed to the screen.

#### Setting the debate topic

- Near the top of `ai-debates.py`, edit `debate_topic` to specify the topic of the debate.

This code is defined for the topic to take a strong position. For example, the default is `debate_topic="Standardized testing should be abolished."` The AI randomly assigned to the "affirmative" position will argue in favor of this position. The AI randomly assigned to the "negative position" will argue against the position.

#### Setting the time limits

- Near the top of `ai-debates.py`, edit `time_limits` to specify the time limits for each round of the debate.

These are defined in seconds, so currently, the opening statement and arguments are given 3 minutes per speaker per round and the rebuttal and closing statement are given 2 minutes per speaker per round. The seconds are converted to minutes in the instructions given to the AI before each round.

We have not explored yet how well the AIs are at staying within the time limits!

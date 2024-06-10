from openai import OpenAI
import os
from dotenv import load_dotenv

from parsing import get_intervals


def get_text_from_gpt(question, transcript):
    load_dotenv()


    value = os.getenv('OPENAI_API_KEY')


    client = OpenAI(api_key=value)


    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are the best sports editor who understands all sports very intricately. You are capable of summarizing text by picking the right sentences from a list of sentences of interviews. You pick sentences so that the resultant block answers the question asked. You will be given a transcript containing a list of sentences followed by the start time (start=) and end time (end=) of when it occurs in a video. For a selected sentence, also check whether the next sentence in combination with current selected sentence adds more value and context to the answer. If yes, pick both individually."},
        {"role": "system", "content": "Your output should be in this format: <Sentence> | start= | end=. Just give answer."},
        {"role": "user", "content": f'''{question}
        {transcript}'''}
        ]
    )
    
    return completion.choices[0].message.content





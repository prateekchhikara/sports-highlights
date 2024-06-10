from openai import OpenAI
import os
from dotenv import load_dotenv

sample_output = '''Um, I I don't think so. Um Yeah, I I don't think so. I mean, I have an idea in my head of when I would when I would like to stop, Um But, | start=260.35 | end=267.85
you know, that's not That's not definitive. You know, a lot of that is just, you know, I think it is is good to, you know, to do that So you can start planning, um, a little bit, Um But Yeah, | start=268.73 | end=283.22
I I don't think I would I don't think I would announce anything like way, way ahead of time, | start=284.37 | end=296.309
because, well, I want to play as long as I can whilst I'm, you know, whilst I'm still feeling good physically and, you know, competitive. Um But I'm aware, based on you know, how my last sort of 56 years have gone that things can change very quickly. | start=297.12 | end=312.579'''




def get_text_from_gpt(question, transcript, video_title):
    load_dotenv()


    value = os.getenv('OPENAI_API_KEY')


    client = OpenAI(api_key=value)


    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are the best sports editor who understands all sports very intricately. You are capable of summarizing sports interviews. You write newspaper articles and give very catchy titles to them."},
        {"role": "user", "content": f"Give a catchy title and news article in the following format. <h3> <title> </h3>\n <article> for a press conference excerpt about {video_title} which answer the question: {question}. The news excerpt is: {transcript}. Separate the paragrpahs in the article with <p> tags. The format is <p align='justify'> Paragraph <p>. Strictly limit your article to two paragraphs only."},

        ]
    )
    
    return completion.choices[0].message.content
print(get_text_from_gpt("What are his thoughts on retiring from tennis?","Andy Murray: Pre-Championships Press Conference | Wimbledon 2023",sample_output))

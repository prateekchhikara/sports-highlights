import re

texts = '''I did spend some time stretching in a jail cell. | start=69.10 | end=77.669
I felt like there was a chance I may be able to still come out here and play. And so I started going through my routine and I tried to get my heart rate down as much as I could today. | start=82.96 | end=89.47
Um, you know, my main focus after, you know, getting arrested was, you know, wondering if I could be able to come back out here and play and, you know, fortunately I was able to do that. | start=126.71 | end=136.97
I was pretty rattled to say the least. Um, you know, I, the, the officer that took me to the um, to the jail was, was very kind. | start=217.18 | end=229.339
He was great. Um, you know, we had a nice chat in the car that kind of helped calm me down and I was sitting there waiting to kind of go in. I, I asked him, I was like, hey, excuse me, can you just come, can you just come hang out with me for a few minutes so I can calm down. | start=229.40 | end=240.38
I was, I was never, you know, angry. I was just in shock and I think my body was just, I was shaking the whole time. | start=240.71 | end=246.149
I was shaken for like an hour. It was, it was definitely a new feeling for me. And he came out and we had a nice chat and then the, the officers inside the jail were tremendous. A couple of them made some jokes. I think when they figured out, you know who I was and what happened and you know how I ended up there, | start=246.19 | end=260.609
Um, you know, I was able to kind of see a bit of the TV and, you know, then I laid down and then I started to stretch a little bit once I got my heart rate down. | start=411.55 | end=417.1
My manager was in the car and 22 gentlemen from the, from the club were, were in the car with me. Um And yeah, we were able to, to talk, have a nice chat. Um, you know, they were, uh, I mean, I'm, I'm not really going to get into the details of that either. | start=446.48 | end=458.45
It was nice to be able to get inside the ropes and do what I love to do. You know, I love competing out here on tour. I love playing the major championships and, um, you know, I've, I've kept myself in the tournament now with a pretty chaotic day and so I'm gonna go from here and focus on getting some rest and recovery. | start=501.01 | end=519.179'''


def extract_numbers(string):
    # Define the regex pattern to match numbers (including decimals)
    pattern = r'\d+\.\d+|\d+'
    
    # Use re.findall() to find all numbers in the string
    numbers = re.findall(pattern, string)
    
    # Convert the extracted numbers from strings to floats or integers
    numbers = [float(num) if '.' in num else int(num) for num in numbers]
    
    return numbers


def merge_intervals(intervals):
    # First, sort the intervals by the starting time
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    
    merged = []
    for interval in intervals:
        # If the merged list is empty or if the current interval does not overlap with the last merged interval, add it to the merged list

        if not merged or int(merged[-1][1]) != int(interval[0]):
            merged.append(interval)
        else:
            # Otherwise, there is an overlap, so we merge the current and previous intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged



def get_intervals(texts):
    texts = texts.strip()

    list_texts = texts.split("\n")
    intervals = []
    for text in list_texts:
        split_texts = text.split("|")

        intervals.append([extract_numbers(split_texts[1])[0], extract_numbers(split_texts[2])[0]])
    intervals = sorted(intervals, key=lambda x: x[0])

    return merge_intervals(intervals)

        

        
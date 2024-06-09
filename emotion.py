from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from constants import EMOTIONS



def GET_EMOTION():

    print("INSIDE GET EMOTION FUNCTION")
    inference_pipeline = pipeline(
        task=Tasks.emotion_recognition,
        model="iic/emotion2vec_base_finetuned")  # Alternative: iic/emotion2vec_plus_seed, iic/emotion2vec_plus_base, iic/emotion2vec_plus_large and iic/emotion2vec_base_finetuned

    rec_result = inference_pipeline('theaudio.mp3', output_dir="./outputs", granularity="utterance", extract_embedding=False)
    scores = rec_result[0]['scores']
    max_index = scores.index(max(scores))
    return EMOTIONS[max_index]

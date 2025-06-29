
from pytz import timezone
from transformers import AutoTokenizer , AutoModelForSequenceClassification 

from scipy.special import softmax

import re 



MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)


def clean_text(text) :
    text = re.sub(r"http\S+","", text)
    text= re.sub(r"@\w+","", text)
    text = re.sub(r"#" , "" ,text)
    return text.strip()


def polarity_scores_reborta(example) :
    try:
        example = clean_text(example)
        encoded_text = tokenizer(example, return_tensors='pt')
        output = model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        return {
            'roberta_neg': float(scores[0]),
            'roberta_neu': float(scores[1]),
            'roberta_pos': float(scores[2])
        }
    except Exception as e:
        raise RuntimeError(f"Model inference failed: {str(e)}")
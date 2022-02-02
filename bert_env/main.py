# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ... IMPORT NECESSARY LIBRARIES;
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ... PRESELECT MODEL;
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

model_name = "deepset/roberta-base-squad2"

# a) Get predictions;
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'What is the approximate radius of Titan ?',
    'context': 'Titan has a radius of about 1,600 miles (2,575 kilometers), and is nearly 50 percent wider than Earth’s moon. Titan is about 759,000 miles (1.2 million kilometers) from Saturn, which itself is about 886 million miles (1.4 billion kilometers) from the Sun, or about 9.5 astronomical units (AU). One AU is the distance from Earth to the Sun. Light from the Sun takes about 80 minutes to reach Titan; because of the distance, sunlight is about 100 times fainter at Saturn and Titan than at Earth.'
}
res = nlp(QA_input)

# b) Load model & tokenizer;
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

if __name__ == "__main__":
    # c) print-result;
    print(res)
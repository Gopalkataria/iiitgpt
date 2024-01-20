import sentence_transformers
from transformers import AutoModel, AutoTokenizer
import numpy as np

from summarizer import Summarizer

smodel = Summarizer()

# model_name = "all-mpnet-base-v2"

model = sentence_transformers.SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
# model = AutoModel.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Model loaded successfully")

text_data = []
filenames = ["s1.txt", "s2.txt", "s3.txt", "s4.txt"]
for filename in filenames:
    with open(filename, "r") as f:
        text_data.append(f.read())

def preprocess_text(query):
    query = query.lower()
    query = query.replace("?", "")
    query = query.replace(".", "")
    query = query.replace("!", "")
    query = query.replace(",", "")
    query = query.replace("  ", " ")
    return query

sentences = []
# for text in text_data:
#     preprocessed_text = preprocess_text(text)
#     sentences.extend(preprocessed_text.split("\n"))

for filename in filenames:
    with open(filename, "r") as f:
        for line in f:
            preprocessed_text = preprocess_text(line)
            sentences.append(preprocessed_text)

print("Text data loaded successfully")


print( sentences[0] )

embeddings = model.encode(sentences)

print("Embeddings generated successfully")

def summarize_text(text):
    return smodel(text)

def handle_query(query):
    query = preprocess_text(query)
    query_embedding = model.encode([query], convert_to_tensor=True)
    print("Query embedded and converted to tensor successfully")
    similarities = np.dot(query_embedding, embeddings.T)[0]
    print("Similarities calculated successfully")
    n = 7
    top_indices = np.argsort(-similarities)[:n]
    relevant_info = []
    for index in top_indices:
        sentence = sentences[index]
        relevant_info.append(f"- {sentence}\n")
    return "".join(relevant_info)


while True:
    inp = input("Enter query: ")
    output = handle_query(inp)
    print("Relevant information: ")
    print(output)
    print("\n")
    
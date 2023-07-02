from sentence_transformers import SentenceTransformer

model = SentenceTransformer('pkshatech/simcse-ja-bert-base-clcmlp')

# Save the model and the tokenizer.
dir_name = 'model'
model.save(dir_name)

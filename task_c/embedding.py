
from .model import model
from .pdf_extract import pdf_sentences
# E5-style: treat sentences as passages/documents
corpus = [f"passage: {s}" for s in pdf_sentences]

# Compute embeddings (download happens automatically the first time)
corpus_embeddings = model.encode(corpus, convert_to_tensor=True, normalize_embeddings=True)

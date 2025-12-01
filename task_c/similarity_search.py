from .model import model
from .pdf_extract import pdf_sentences as sentences
from .embedding import corpus_embeddings
from sentence_transformers import util



# Example query
user_query = "What is the role of neural networks in AI?"
query_text = f"query: {user_query}"

# Embed query
query_embedding = model.encode(query_text, convert_to_tensor=True, normalize_embeddings=True)

# Compute cosine similarities
cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]  # shape: (len(corpus),)

# Sort by similarity (highest first)
top_k = min(3, len(sentences))  # return top 3 matches
top_results = cos_scores.topk(k=top_k)

print(f"\nQuery: {user_query}\n")
print("Top results:")
for score, idx in zip(top_results.values, top_results.indices):
    idx = idx.item()
    score = score.item()
    print(f"Score: {score:.4f} | Sentence: {sentences[idx]}")

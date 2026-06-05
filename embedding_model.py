import warnings

warnings.filterwarnings("ignore")

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
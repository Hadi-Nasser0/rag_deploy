import os
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.utils.config import DATA_PROCESSED_PATH, DATA_RAW_PATH, CHUNK_OVERLAP, CHUNK_SIZE

def load_raw_files(raw_dir: str) -> list[str]:
    """Load all .txt files from raw data folder"""
    texts = []
    # Use a glob pattern that matches all .txt files in the directory
    for file in Path(raw_dir).glob("*.txt"):
        # Ensure we only process regular files
        if file.is_file():
            with open(file, "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts

def clean_text(text:str) -> str:
    """unstructured data cleaning"""
    text = " ".join(text.split()) # remove multiple spaces
    return text.strip()

def chunk_text(text:str, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP) -> list[str]:
    """deviding text into chunks"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        separators= ["\n\n", "\n", ".", " ", ""]
    )
    return splitter.split_text(text)

def run_ingestion():
    os.makedirs(DATA_PROCESSED_PATH, exist_ok=True)
    processed_file = Path(DATA_PROCESSED_PATH) / "processed.txt"

    # Skip if processed file already exists
    if processed_file.exists():
        print(f"✅ Processed file already exists: {processed_file}")
        return

    print("🔹 Loading raw data...")
    raw_texts = load_raw_files(DATA_RAW_PATH)

    print("🔹 Cleaning and chunking text...")
    all_chunks = []
    for text in raw_texts:
        cleaned = clean_text(text)
        chunks = chunk_text(cleaned)
        all_chunks.extend(chunks)

    print(f"🔹 Saving {len(all_chunks)} chunks to processed folder...")
    with open(processed_file, "w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(chunk + "\n")

    print(f"✅ Processing complete! File saved at {processed_file}")

if __name__ == "__main__":
    run_ingestion()


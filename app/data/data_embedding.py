"""
Read txt files from document folder, generate embeddings using SLM API,
store them in an InMemoryVectorStore, and save all embedding data
into a single JSON file: embeddings.json

How to run:
python -m app.data.data_embedding
"""

import os
import json
import uuid
from pathlib import Path
from typing import List, Dict

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document

from app.core.config import slm_embedding


def build_inmemory_vectorstore_and_save_json(
    input_directory: str,
    output_file: str,
):
    """
    1. Read all .txt files from input_directory
    2. Generate embeddings using SLM API
    3. Store documents in InMemoryVectorStore
    4. Save all embeddings + metadata into one JSON file
    """

    documents: List[Document] = []
    json_records: List[Dict] = []

    for filename in os.listdir(input_directory):
        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(input_directory, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        record_id = str(uuid.uuid4())

        # Document is the standard LangChain abstraction
        documents.append(
            Document(
                page_content=text,
                metadata={
                    "filename": filename,
                    "id": record_id,
                }
            )
        )

        # For JSON output (human-readable / demo purpose)
        json_records.append(
            {
                "id": record_id,
                "filename": filename,
                "content": text,
            }
        )

    # Create InMemoryVectorStore
    vectorstore = InMemoryVectorStore.from_documents(
        documents=documents,
        embedding=slm_embedding,
    )

    # Save all records into ONE json file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(json_records, f, indent=4, ensure_ascii=False)

    return vectorstore


if __name__ == "__main__":
    script_dir = Path(__file__).parent

    input_directory = script_dir / "./document"
    output_file = script_dir / "./embeddings/embeddings.json"

    vectorstore = build_inmemory_vectorstore_and_save_json(
        input_directory=str(input_directory),
        output_file=str(output_file),
    )

    print("InMemoryVectorStore created successfully.")
    print(f"Embeddings saved to {output_file}")

"""
CogniPlan Personal Knowledge Engine
===================================

Provides lightweight semantic-style retrieval over
student learning material.

The engine is designed around a simple RAG workflow:

DOCUMENTS
    ↓
CHUNKING
    ↓
INDEXING
    ↓
RETRIEVAL
    ↓
CONTEXT FOR AI GENERATION

This module intentionally uses only Python's standard
library so that the core system remains easy to deploy.
"""

import re
from dataclasses import dataclass
from collections import Counter


@dataclass
class KnowledgeChunk:
    """
    Represents a searchable piece of learning material.
    """

    chunk_id: str
    source: str
    content: str


class KnowledgeEngine:
    """
    Personal knowledge retrieval engine.

    Stores learning material and retrieves the most
    relevant chunks for a learner's question.
    """

    def __init__(self):
        self.chunks: list[KnowledgeChunk] = []

    # -----------------------------------------------------
    # Text Processing
    # -----------------------------------------------------

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        """
        Convert text into normalized tokens.
        """

        return re.findall(
            r"\b[a-zA-Z0-9]+\b",
            text.lower(),
        )

    # -----------------------------------------------------
    # Document Ingestion
    # -----------------------------------------------------

    def add_document(
        self,
        source: str,
        content: str,
        chunk_size: int = 500,
    ) -> int:
        """
        Add a document to the knowledge base.

        Large documents are divided into smaller chunks
        so that retrieval can focus on relevant sections.
        """

        if not content.strip():
            raise ValueError(
                "Document content cannot be empty."
            )

        words = content.split()

        created_chunks = 0

        for start in range(
            0,
            len(words),
            chunk_size,
        ):
            chunk_words = words[
                start:start + chunk_size
            ]

            chunk = KnowledgeChunk(
                chunk_id=(
                    f"{source}-"
                    f"{created_chunks + 1}"
                ),
                source=source,
                content=" ".join(chunk_words),
            )

            self.chunks.append(chunk)
            created_chunks += 1

        return created_chunks

    # -----------------------------------------------------
    # Retrieval
    # -----------------------------------------------------

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ) -> list[dict]:
        """
        Retrieve the most relevant knowledge chunks.

        Relevance is estimated using normalized keyword
        overlap between the query and stored material.
        """

        if not query.strip():
            return []

        query_tokens = self._tokenize(query)

        if not query_tokens:
            return []

        query_counter = Counter(query_tokens)

        results = []

        for chunk in self.chunks:

            chunk_tokens = self._tokenize(
                chunk.content
            )

            if not chunk_tokens:
                continue

            chunk_counter = Counter(
                chunk_tokens
            )

            overlap = sum(
                min(
                    query_counter[token],
                    chunk_counter[token],
                )
                for token in query_counter
            )

            score = overlap / len(query_tokens)

            if score > 0:
                results.append(
                    {
                        "chunk_id": chunk.chunk_id,
                        "source": chunk.source,
                        "content": chunk.content,
                        "relevance_score": round(
                            score,
                            3,
                        ),
                    }
                )

        results.sort(
            key=lambda item: item[
                "relevance_score"
            ],
            reverse=True,
        )

        return results[:top_k]

    # -----------------------------------------------------
    # Context Construction
    # -----------------------------------------------------

    def build_context(
        self,
        query: str,
        top_k: int = 3,
    ) -> str:
        """
        Build a compact context block from retrieved
        knowledge for downstream AI generation.
        """

        results = self.retrieve(
            query=query,
            top_k=top_k,
        )

        if not results:
            return (
                "No relevant learning material "
                "was found."
            )

        context_sections = []

        for result in results:

            context_sections.append(
                (
                    f"[Source: {result['source']}]\n"
                    f"{result['content']}"
                )
            )

        return "\n\n".join(
            context_sections
        )

    # -----------------------------------------------------
    # Knowledge Statistics
    # -----------------------------------------------------

    def statistics(self) -> dict:
        """
        Return information about the knowledge base.
        """

        sources = {
            chunk.source
            for chunk in self.chunks
        }

        return {
            "total_chunks": len(self.chunks),
            "unique_sources": len(sources),
            "sources": sorted(sources),
        }

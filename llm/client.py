"""Unified model client abstractions."""

from __future__ import annotations


class LLMClient:
    """Provider-agnostic LLM client baseline."""

    def chat(self) -> None:
        """Synchronous chat entry point."""
        pass

    def stream(self) -> None:
        """Streaming chat entry point."""
        pass

    def embed(self) -> None:
        """Embedding generation entry point."""
        pass


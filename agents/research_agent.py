"""Research-oriented agent baseline."""

from __future__ import annotations

from .base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    """Baseline skeleton for a research agent."""

    def run(self) -> None:
        """Run the research flow."""
        pass

    def think(self) -> None:
        """Plan information gathering."""
        pass

    def act(self) -> None:
        """Execute one research action."""
        pass


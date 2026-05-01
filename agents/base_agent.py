"""Base abstractions for all agents."""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Abstract base class for agent lifecycle methods."""

    @abstractmethod
    def run(self) -> None:
        """Run the full agent workflow."""

    @abstractmethod
    def think(self) -> None:
        """Plan the next action."""

    @abstractmethod
    def act(self) -> None:
        """Execute one action step."""


from typing import Any, Dict


class BaseInput:
    """Base class representing input data for a structural model."""

    def __init__(self, data: Dict[str, Any]):
        """
        Initialize a new Input object.

        Args:
            data (Dict[str, Any]): Input data for the model.
        """
        self.data = data

    def validate(self) -> bool:
        """
        Validate the input data.

        Returns:
            bool: True if the input data is valid, False otherwise.
        """
        raise NotImplementedError("Method 'validate' must be implemented by subclass.")

    def parse(self) -> None:
        """
        Parse the input data.
        """
        raise NotImplementedError("Method 'parse' must be implemented by subclass.")

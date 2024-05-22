class BaseStructure:
    """Base class representing a structural model."""

    def __init__(self, name: str):
        """
        Initialize a new Structure object.

        Args:
            name (str): The name of the structure.
        """
        self.name = name

    def describe(self) -> str:
        """
        Describe the structure.

        Returns:
            str: A description of the structure.
        """
        return f"This is a {self.name} structure."

    def solve(self) -> None:
        """
        Solve the structural model.
        """
        raise NotImplementedError("Method 'solve' must be implemented by subclass.")

class BaseOutput:
    """Base class representing output data from a structural model."""

    def __init__(self):
        """Initialize a new Output object."""
        self.results = {}

    def save(self, filename: str) -> None:
        """
        Save the output data to a file.

        Args:
            filename (str): The name of the file to save the data to.
        """
        raise NotImplementedError("Method 'save' must be implemented by subclass.")

    def visualize(self) -> None:
        """
        Visualize the output data.
        """
        raise NotImplementedError("Method 'visualize' must be implemented by subclass.")

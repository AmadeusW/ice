import yaml

class Configuration:
    def __init__(self, path):
        """
        Configures the dashboard based on a .yaml file.
        
        :param path: Path to the configuration
        """
        try:
            with open(path, 'r') as file:
                yaml_data = file.read()
            self.data = yaml.safe_load(yaml_data)
            print(f"Loaded configuration from: {path}")
        except Exception as e:
            print(f"Error reading {path}: {e}")
            raise

    def enumerate_items(self):
        """
        Returns enumerator over data
        """
        return enumerate(self.data.items())

    def print(self):
        for key, piece in self.data.items():
            print(f"{piece['kind']} {piece['type']} {key} \"{piece['title']}\"")

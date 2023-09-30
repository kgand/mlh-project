# config.py

# Network interface to monitor (you can change this)
NETWORK_INTERFACE = "eth0"

# Model hyperparameters (customize as needed)
MODEL_PARAMS = {
    "n_estimators": 100,
    "max_depth": 10,
    "random_state": 42,
}

# Threshold for generating alerts (customize as needed)
ALERT_THRESHOLD = 0.8

# Logging settings
LOG_FILE = "ids.log"  # Path to the log file

# Other configuration settings
# ...

# Function to load additional configuration settings from a file (if needed)
def load_config_from_file(config_file_path):
    # Read configuration settings from the file and update the variables
    # Example: Read a JSON or YAML file and update the variables
    pass

# You can also add other functions or configurations as needed.

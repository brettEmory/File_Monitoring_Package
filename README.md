# File Monitoring

## Overview

File Monitoring is a Python package designed to monitor file changes in a specified directory and write the paths and contents of those files to a `.txt` file. This tool is especially useful for debugging and keeping track of changes in projects with a complex file structure. It was primarily developed for personal use to facilitate easier debugging and integration with ChatGPT, as well as a learning experience within Python scripting and automation.

## Features

- Monitors a specified directory for file changes
- Ignores virtual environment directories
- Writes file paths and contents to a `.txt` file
- Updates only the modified files for better performance

## Installation

### Prerequisites

- Python 3.6 or higher

### Using pip


Install the package using pip:
```bash
pip install file_monitoring
```
## Usage

### As a Script

Create a script (e.g., `run_monitor.py`) and use the `file_monitoring` package:
```Python
from file_monitoring.monitor import run_monitor


directory = '/path/to/directory'
output_file = 'file_contents.txt'

run_monitor(directory, output_file)
```
### Run The Script:

```Python
python run_monitor.py
```
### Command-Line Interface (CLI)

If you have set up an entry point in your `setup.py`, you can run the package directly from the command line:
```bash
file_monitoring -d /path/to/directory -o file_contents.txt
```

### Example

Here's an example of how to use the package in a Python script:
```Python
from file_monitoring.monitor import run_monitor

directory = '/path/to/your/project'
output_file = 'file_contents.txt'

run_monitor(directory, output_file)
```

# Development
Setting Up the Development Environment
Clone the Repository
```bash
git clone https://github.com/yourusername/file_monitoring.git
cd file_monitoring
```
Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```
Install Dependencies
```bash
pip install -r requirements.txt
```
## Building and Installing the Package Locally
Build the Package
```bash
python setup.py sdist bdist_wheel
```
Install the Package Locally
```bash
pip install -e .
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Watchdog - Used for monitoring file system events.

## Contact

- **Author**: Brett Emory
- **Email**: brettemory2@gmail.com
- **GitHub**: [brettEmory](https://github.com/brettEmory)

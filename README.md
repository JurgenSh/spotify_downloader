# Spotify Downloader

## Description
This is a small tool designed to download songs from Spotify.

## Prerequisites
- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) package manager

## Setup

### Using PyInstaller (Recommended)

1. **Download the executable**: Download the correct executable for your platform from the GitHub releases and just double-click to run it.

### Using Python Script

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/YOUR_USERNAME/spotify-downloader.git
    ```
   
2. **Install Dependencies**: Navigate into the project folder and install dependencies using Poetry.
    ```bash
    cd spotify-downloader
    poetry install
    ```

## Running the Application

### Using Poetry
```bash
poetry run python main.py [SONG_URL] --format [FORMAT]
```


### Using a Batch File or Shell Script
- **For Windows**: Double-click on `run.bat`.
- **For Mac/Linux**: Open a terminal in the project folder and run the following commands:
    ```bash
    chmod +x run.sh
    ./run.sh
    ```

### Entering API Credentials
Upon the first run, you will be prompted to enter your Spotify Client ID and Client Secret. These credentials will be saved for future sessions, so you won't need to re-enter them unless you wish to change them.

To change your saved API credentials, use the following command:
```bash
poetry run python main.py --reset-credentials
```
### Command-Line Arguments
- `SONG_URL`: URL of the Spotify song you wish to download (Required).
- `--format`: Choose the download format. Options include 'MP3', 'AAC', 'FLAC', 'M4A', 'OPUS', 'VORBIS', 'WAV'. Default is 'FLAC'.

## Setting Up Pre-commit Hooks

Pre-commit hooks help in automating tasks like code formatting, linting, and even running tests right before you commit changes. This ensures that you're not committing code that's broken or poorly formatted.

### Installation

1. Ensure you have Python installed on your machine.
2. Install `pre-commit` using pip:

    ```bash
    pip install pre-commit
    ```

3. Navigate to your project directory and install the pre-commit hooks:

    ```bash
    pre-commit install
    ```

### Usage

Now, pre-commit will automatically run the specified hooks defined in `.pre-commit-config.yaml` every time you try to make a git commit. If any of the checks fail, the commit will be aborted.

To manually run all pre-commit hooks on all files:

```bash
pre-commit run --all-files
```
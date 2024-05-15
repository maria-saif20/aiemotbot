
# AIEMOTBOT

AIEMOTBOT is a FastAPI application designed to perform various language processing tasks, including document loading, image interpretation, and question-answering, using different language models and libraries.
# AIEMOTBot

AIEMOTBot is a Python-based project designed for voice-to-text generation and emotion detection. Using various tools and libraries, this bot processes audio inputs, converts them into text, and analyzes the text to determine the underlying emotions.

## Features

- **Voice-to-Text Conversion**: Converts spoken language into written text.
- **Emotion Detection**: Analyzes the transcribed text to identify emotions.
- **User-Friendly Interface**: Provides an easy-to-use interface for interacting with the bot.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/AIEMOTBot.git
    cd AIEMOTBot
    ```

2. **Install dependencies:**

    Use `pip` to install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up Docker:**

    Ensure you have Docker installed. Build the Docker image:

    ```sh
    docker build -t aiemotbot .
    ```

    Run the Docker container:

    ```sh
    docker-compose up
    ```

## Usage

1. **Running the Bot:**

    After setting up the Docker container, the bot should be running and accessible via the specified port.

2. **Interacting with the Bot:**

    Upload audio files to the bot through the provided interface. The bot will process the audio, generate text, and analyze the emotions.

## File Structure

- **.dockerignore**: Specifies files and directories to ignore in Docker builds.
- **AIEMOTBOT.png**: Logo or image for the project.
- **AIEMOTBot.py**: Main Python script for the bot.
- **Dockerfile**: Instructions for building the Docker image.
- **LICENSE**: The MIT license file for the project.
- **README.md**: This readme file.
- **compose.yaml**: Docker Compose file for managing the container.
- **error.py**: Error handling module.
- **main.py**: Entry point for the application.
- **requirements.txt**: List of dependencies to be installed.
- **style.css**: Stylesheet for the web interface.
- **utils.py**: Utility functions for the project.
- **voicetoemotion.py**: Module for voice-to-text and emotion detection.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

- Special thanks to the developers of the libraries and tools used in this project.
- Thanks to the open-source community for their continuous support and contributions.



## Installation

To install AIEMOTBOT and its dependencies, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/maria-saif20/AIEMOTBOT.git
   cd AIEMOTBOT

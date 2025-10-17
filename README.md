# project-chronos
 Usage Input a fragmented text string to reconstruct and receive a report with AI completion and source links.


# Project Chronos: The AI Archeologist

## Description
Project Chronos is an AI-powered tool designed to reconstruct incomplete or obscure digital text fragments from historical sources. It uses Google Gemini to fill in missing context and automatically retrieves relevant articles and sources from the web.

## Features
- Accepts incomplete or cryptic text input
- Uses Google Gemini to provide educated guesses and reconstruction
- Searches the web for relevant contextual articles based on the AI reconstruction
- Generates a report showing the original text, reconstructed text, and source links

## Setup Instructions

1. Clone this repository:
   git clone https://github.com/yourusername/project-chronos.git
   cd project-chronos


2. Create a `.env` file in the root of this directory and add your Google Gemini API key:
   GEMINIAPIKEY=your_api_key_here

3. Install the required Python packages:
   pip install -r requirements.txt


4. Run the program:
   python main.py


## Usage
- When prompted, enter a piece of incomplete or obscure text.
- The program will call Google Gemini to reconstruct the text and perform a web search to find relevant articles.
- The output will display the original fragment, reconstructed text, and links to contextual sources.

## Security Note
- The `.env` file containing your API keys is **not** included in the repository (it's listed in `.gitignore`).
- Never commit your secret API keys to public repositories.

---

Feel free to contribute or report issues!

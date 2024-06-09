# AI Sports Recap

AI Sports Recap is a Streamlit-based application designed to generate video highlights and textual summaries of sports press conferences given a YouTube video link. The app leverages cutting-edge technologies including OpenAI's GPT-4o, Pegasus1 by TwelveLabs, and Docker for seamless integration and deployment.

## Tech Stack

- **OpenAI GPT-4o**: Used for generating textual summaries and extracting relevant video clips based on the input query.
- **Pegasus1 by TwelveLabs**: Utilized for transcript generation and video clipping.
- **Streamlit**: Provides the UI and frontend for user interaction.
- **Docker**: Ensures a consistent and reproducible environment for running the application.

## Features

1. **Transcript Generation**: Automatically generates a transcript of the provided video.
2. **Highlight Extraction**: Identifies and extracts key video segments that are relevant to the user's query.
3. **Summary Generation**: Creates a concise summary of the press conference.
4. **Social Media Sharing**: Allows users to share the generated summary and highlights on social media platforms.

## Installation

### Prerequisites

- Docker
- OpenAI API Key
- TwelveLabs API Key

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/prateekchhikara/sports-highlights.git
   ```

2. **Set up environment variables**
   Create a `.env` file in the root directory and add your API keys:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   INDEX_ID=your_index_id
   TLABS=twelve-labs_api_key
   ```

3. **Build and run the Docker container**

4. **Access the application**
   Open your browser and go to `http://localhost:8501`.

## Usage

1. **Enter the URL**: Paste the YouTube video link of the press conference.
2. **Select an option**: Choose from predefined video options if available.
3. **Submit a query**: Input your question or query related to the video content.
4. **View the results**: The app will display the video highlights and textual summary based on your query.
5. **Share on social media**: Use the provided links to share the summary and highlights on Facebook and Twitter.

## Code Overview

The main components of the application are as follows:

- **Streamlit Frontend**: Handles user input and displays results.
- **Backend Functions**:
  - `generate_transcript`: Uses Pegasus1 to generate video transcripts.
  - `get_intervals`: Extracts relevant video segments based on the GPT-4o output.
  - `get_text_from_gpt`: Queries GPT-4o to extract relevant content & their timestamps from the generated transcripts based on the user's prompt.
  - `get_clippings_from_intervals`: Generates relevant clips of the original video based on the identified time intervals & merges them into a single highlight video.
  - `get_summary_and_title_from_gpt`: Generates a summary and title for the video content.
- **Social Media Integration**: Provides links for sharing the content on social media platforms.

## Example

1. **User Interface**:

   - Enter the URL of the video or select from predefined options.
   - Submit a question or query about the press conference.

2. **Backend Processing**:

   - Generate transcript of the video.
   - Use GPT-4o to summarize the transcript and identify key video segments.
   - Clip the relevant video segments and generate a consolidated highlight video.
   - Display the textual summary and video highlights to the user.

3. **Sharing**:
   - Users can share the generated content on Facebook and Twitter directly from the app.

## Acknowledgements

- OpenAI for their powerful GPT-4o model.
- TwelveLabs for Pegasus1 API.
- Streamlit for the user-friendly frontend framework.
- Docker for the containerization and ease of deployment.

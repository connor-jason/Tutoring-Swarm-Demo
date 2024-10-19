# Multi-Subject Tutoring AI

This project is a simple demonstration that implements a multi-agent AI tutoring system using the Swarm framework. It provides tutoring assistance in various subjects including Math, History, Science, and English/Writing.

## Features

- Question routing to appropriate subject experts
- Specialized agents for Math, History, Science, and English/Writing
- Dynamic agent switching based on the context of the conversation
- Interactive command-line interface for user input

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed
- pip (Python package manager) installed

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/multi-subject-tutoring-ai.git
   cd multi-subject-tutoring-ai
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install the new Swarm framework:
   ```
   pip install git+https://github.com/openai/swarm.git
   ```

4. Set up your environment variables:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

To run the tutoring system, run the code in the `main.py` file.

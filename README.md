# CrewAI Deployment Example

This repository contains the companion code for the [Deploy CrewAI Agent to the Cloud](https://docs.itura.ai/deployment-guides/crewai) guide on Itura's documentation.

## Overview

This project demonstrates a simple CrewAI agent that researches the current state of AI LLMs. The code is structured to be easily deployable to Itura Cloud Platform.

The guide walks you through:

1.  Setting up a basic CrewAI agent.
2.  Adding a Flask endpoint (`/run`) to initiate the agent via HTTP POST requests.
3.  Generating a `requirements.txt` file.
4.  Deploying the agent to Itura Cloud via a GitHub repository.
5.  Running the deployed agent using its API endpoint.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Itura-AI/crewai-deployment-example.git
    cd crewai-deployment-example
    ```
2.  **Follow the guide:** Refer to the [deployment guide](https://docs.itura.ai/deployment-guides/crewai) for step-by-step instructions on running the agent locally and deploying it.

## Branches

- `initial`: The starting point for the guide.
- `complete`: The final code after following all steps in the guide.

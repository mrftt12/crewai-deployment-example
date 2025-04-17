#!/usr/bin/env python
from crewai_deployment_example.crew import CrewaiDeploymentExample

from flask import Flask, request, jsonsify

app = Flask(__name__)

@app.rount('/run', methods=['POST'])
def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': '2025'
    }
    
    CrewaiDeploymentExample().crew().kickoff(inputs=inputs)

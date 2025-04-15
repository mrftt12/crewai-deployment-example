#!/usr/bin/env python
from crewai_deployment_example.crew import CrewaiDeploymentExample


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': '2025'
    }
    
    CrewaiDeploymentExample().crew().kickoff(inputs=inputs)

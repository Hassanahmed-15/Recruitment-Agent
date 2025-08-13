
#!/usr/bin/env python
import sys
from recruitment.crew import RecruitmentCrew


def run():
    inputs = {
       
    }
    RecruitmentCrew().crew().kickoff(inputs=inputs)

def train():

    inputs = {
    }
    try:
        RecruitmentCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

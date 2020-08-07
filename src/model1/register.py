import os
import sys
import argparse
from azureml.core import Run
from azureml.core.model import Model

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-path', type=str)
    args = parser.parse_args()
    return args

def main():
    args = getRuntimeArgs()
    run = Run.get_context()
    run_id = run.parent.id
    parent_run = Run(experiment=run.experiment, run_id=run_id)
    # register the best model with the input dataset
    model = parent_run.register_model(model_name='german-credit-model', model_path=os.path.join('outputs', 'model.pkl'))


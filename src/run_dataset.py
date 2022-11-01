import click
from easydict import EasyDict as edict
import yaml
import traceback
from dataset.temporal_graph_dataset import Temporal_Graph_Signal


@click.command()
@click.option('--dataset_name', type=click.STRING, default=None)
def main(dataset_name):
    try:
        loader = Temporal_Graph_Signal(dataset_name, 'std')
        loader.preprocess_dataset()
        print('Dataset Ready')

    except:
        print(traceback.format_exc())


if __name__ == '__main__':
    main()

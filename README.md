# Neural Sheaf Diffusion

This repository contains code allowing to run experiments from the
**[Neural Sheaf Diffusion: A Topological Perspective on Heterophily and Oversmoothing in GNNs](https://arxiv.org/abs/2202.04579) (NeurIPS 2022)** paper on the filtered versions of datasets squirrel and chameleon, for the project in the course "Geometric Data Analysis" by Paul Sitoleux and Ethan XX.


## Getting started

We used `CUDA 10.2` for this project. To set up the environment, run the following command:

```bash
conda env create --file=environment_gpu.yml
conda activate nsd
```
For using another `CUDA` version, modify the version specified inside `environment_gpu.yml`. If you like to run 
the code in a CPU-only environment, then use `environment_cpu`. 

To make sure that everything is set up correctly, you can run all the tests using:
```bash
pytest -v .
```

## Running experiments

To run the experiments without a Weights & Biases (wandb) account, first disable `wandb` by running `wandb disabled`. 
Then, for instance, to run the training procedure on `texas`, simply run the example script provided:
```commandline
sh ./exp/scripts/run_texas.sh
```

To run the experiments using `wandb`, first create a [Weights & Biases account](https://wandb.ai/site). Then run the following
commands to log in and follow the displayed instructions:
```bash
wandb online
wandb login
```
Then, you can run the example training procedure on `texas` via:
```bash
export ENTITY=<WANDB_ACCOUNT_ID>
sh ./exp/scripts/run_texas.sh
```
Scripts for the other heterophilic datasets are also provided in `exp/scripts`. 

### Filtered datasets

If you want to replace the datasets 'chameleon' and 'squirrel' by their filtered versions, you should first run

'''commandline
python generate_filtered_chameleon_squirrel.py
'''

then run the experiments as described above.





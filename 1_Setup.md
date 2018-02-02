
## Setup
Note: If you're already comfortable with `anaconda` and `jupyter notebook`, feel free to skip these steps and start the exercises.

### Installing Anaconda

We will be using `anaconda` for this workshop, and we highly recommend you do so for your own projects. `anaconda` provides a "tool box" for ML; it comes with various libraries you need to do ML in python. Another neat thing about `anaconda` is that you can create a virtual environment, which is a separate python environment from the default one on your computer. Virtual environments allow us to separate library dependencies across projects and make it easier for us to share our environment setups with other developers.

You can install Anaconda [here](https://www.anaconda.com/download). Please download `Python3.6` version. Once you finished installing it run on your terminal:

```
conda -V
```

if you see the version of your conda (e.g. `5.0.1`), success! If not, google around and try hard to make it work...

### Setting up Jupyter

Clone this repository and run the following:
```
conda env create environment.yml       # create conda virtual environment
source activate tensorflow_workshop    # activate the virtual environment
jupyter notebook                       # open jupyter on your default browser
```
Once you open `jupyter notebook`, make sure the kernel is set to `Python [conda env:tensorflow_workshop]`.

![alt text](images/setup.png)

Once you're done with your work, you can deactivate to get out of the virtual environment:
```
source deactivate                      # get out of the virtual environment
```

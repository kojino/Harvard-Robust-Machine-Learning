# CS282R Deep Learning Workshop
A tensorflow tutorial for CS282R: Robust Machine Learning at Harvard University.

## Setup
First, install Anaconda [here](https://www.anaconda.com/download/#macos).
Clone this repository and run the following:
```
conda env create environment.yml       # create conda virtual environment
source activate deep_learning_workshop # activate the virtual environment
jupyter notebook                       # open jupyter on your default browser
```
Once you open jupyter notebook, make sure the kernel is set to `Python [conda env:deep_learning_workshop]`.

![alt text][setup.png]

Once you're done with your work, you can deactivate to get out of the virtual environment:
```
source deactivate                      # get out of the virtual environment
```

## References
- [Official Tutorial on handwritten digits (MNIST) classification](https://www.tensorflow.org/tutorials/layers)

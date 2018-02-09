# CS282R Tensorflow Workshop
A TensorFlow tutorial for CS282R, a course on robust machine learning taught at Harvard University in Spring 2018.

## Overview
This workshop covers the fundamentals of TensorFlow. By the end of this workshop, you will be well equipped to start building your own neural network models in TensorFlow.
The workshop will start by introducing concepts unique to TensorFlow, e.g. sessions, variables, optimizers.
Later, we'll put these concepts together to build logistic regression, 3-layer NN, and finally, GAN.

You will start from

`tf.add(2,3)`

and will end up building GAN that can generate the following image:

TODO: Some awesome image.

The side theme of this workshop is writing clean, structured and well-documented code. ML code tends to get messy. This is especially the case in academic settings where we don't have a manager to review your code. We are also free from the pressure that our code will be used by millions of people. BUT, this never means that you can write sloppy code. The code should be nicely written so that you, three months from now, should be able to come back to the code and tell exactly what each function is doing.

That said, my code is not the best thing in the world. If you find any improvements, or errors in the code, please let me know. Pull requests are always welcome.

## Prerequisite
- Comfortability with Python
- Understanding of basic deep learning concepts.
- Fully charged laptop (so tat we don't run out of outlets).
- Install `TensorFlow` and other packages by following section 1. Run code in section 3 and make sure things run smoothly before class.

## Index
1. [Setup](1_Setup.ibynb)
2. [Introduction](2_Introduction.ibynb)
3. [Graphs, Sessions](3_Graphs_Sessions.ipynb)
4. [Basic Operations](4_Basic_Operations.ipynb)
5. [Variables, Gradients, Placeholders](5_Variables_Gradients_Placeholders.ipynb)
6. [Classification, Regression](6_Classification_Regression.ipynb)
7. [Visualization](7_Visualization.ipynb)
8. [Multi-layer Perceptron](8_Multi_Layer_Perceptron.ipynb)
9. [GAN](9_GAN.ipynb)

## Workshop Format
When learning a new framework, it is better to move hands than to listen. So, we prepared quite a bit of programming exercises.
You will work with your project partner on these exercises. [Pair programming](https://en.wikipedia.org/wiki/Pair_programming) is extremely effective for being a better coder whether it be software or ML!
- Introduction to TensorFlow (section 1~6, 30 min)
- Pair Programming Exercises on Basics (section 1~6, 45 min)
- Break (10 min)
- Introduction to Deep Learning with TensorFlow (section 7~9, 30 min)
- Pair Programming Exercises on Deep Learning (section 7~9, 45 min)

## Things we will not cover
Here are the list of things we will not cover but you might want to self-learn:
- Other Deep Learning models (e.g. RNN, CNN, VAE)
- [Using GPUs](https://www.tensorflow.org/programmers_guide/using_gpu)
- [Saving variables and graphs](https://www.tensorflow.org/programmers_guide/saved_model)
- [Testing your code](https://github.com/nfmcclure/tensorflow_cookbook/tree/master/10_Taking_TensorFlow_to_Production)

## Reference
- [Official Tutorial on handwritten digits (MNIST) classification](https://www.tensorflow.org/tutorials/layers)
- [Stanford CS20, TensorFlow for Deep Learning Research](https://web.stanford.edu/class/cs20si/syllabus.html)
- [Stanford CS224d, Deep Learning for NLP](http://web.stanford.edu/class/cs224n/syllabus.html)
- [Most popular TF code samples on GitHub](https://github.com/aymericdamien/TensorFlow-Examples)

Workshop offered by: [Kojin Oshiba](http://kojinoshiba.com/), Jerry Anunrojwong.
<br />
Course taught by Professor [Yaron Singer](https://people.seas.harvard.edu/~yaron/).

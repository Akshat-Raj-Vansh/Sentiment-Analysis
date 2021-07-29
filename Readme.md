# Sentiment Analysis

This repository contains our work on Sentiment Analysis on voice data using emodb dataset. This dataset is available here [Emo-db](http://www.emodb.bilderbar.info/download/)

## Prerequisites

Linux (preferable Ubuntu LTS). Python2.x

### Installing dependencies

*Note*: You can skip this step, if you are installing the packages.
Dependencies are listed below and in the `requirements.txt` file.

* h5py
* Keras
* scipy
* sklearn
* speechpy
* tensorflow

Install one of python package managers in your distro. If you install pip, then you can install the dependencies by running
`pip3 install -r requirements.txt`

If you prefer to accelerate keras training on GPU's you can install `tensorflow-gpu` by
`pip3 install tensorflow-gpu`

### Directory Structure

* `speechemotionrecognition/` - Package folder which contains all the code files corresponding to package

* `dataset/` - Contains the speech files in wav formatted seperated into 7 folders which are the corresponding labels of those files
* `models/` - Contains the saved models which obtained best accuracy on test data.
* `code/` - Contains codes to predict Sentiment.

### Details of the package

* `utilities.py` - Contains code to read the files, extract the features and create test and train data

* `dnn.py` - Code to train Deep learning Models. Supports two models given below
  * `1 - CNN`
  * `2 - LSTM`

### Installation

A `setup.py` file is provided in the repository. You can run `sudo python3 setup.py install` to install it at system level.
If you don't have privileges to do so, you can install it at user level by running `python3 setup.py install --user`.

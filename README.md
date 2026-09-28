# ANN Fundamentals

This repository contains Python implementations demonstrating fundamental concepts of Artificial Neural Networks (ANNs) through manual calculations and visualizations.

The programs focus on understanding how an ANN neuron works, how activation functions transform values, how loss functions measure prediction error, and how weights are updated during learning.

## Topics Covered

### 1. Loss Functions

Implementation of:

* Mean Squared Error (MSE)
* Binary Cross Entropy (BCE)

MSE is commonly used for regression problems, while Binary Cross Entropy is commonly used for binary classification problems.

### 2. Manual ANN Weight Update

Demonstrates the basic learning process of an ANN neuron:

* Input
* Weight
* Bias
* Weighted sum
* ReLU activation
* Prediction
* Error calculation
* Weight update using a learning-rate-based gradient update

### 3. Manual Sigmoid Neuron

Demonstrates the working of a single neuron using:

* Multiple inputs
* Weights
* Bias
* Weighted sum
* Sigmoid activation
* Binary output interpretation

### 4. Activation Function Visualization

Visualizes and compares three commonly used activation functions:

* Sigmoid
* ReLU
* Tanh

The functions are plotted using Matplotlib for input values ranging from -10 to 10.

## Directory Structure

```text
ANN-Fundamentals/
│
├── README.md
│
├── 01_Loss_Functions/
│   ├── loss_functions.py
│   └── README.md
│
├── 02_Manual_ANN_Weight_Update/
│   ├── manual_ann_weight_update.py
│   └── README.md
│
├── 03_Manual_Sigmoid_Neuron/
│   ├── manual_sigmoid_neuron.py
│   └── README.md
│
└── 04_Activation_Function_Visualization/
    ├── activation_function_visualization.py
    └── README.md
```

## Technologies Used

* Python
* NumPy
* Matplotlib
* Math module

## Learning Objective

The purpose of this repository is to understand the fundamental mathematical and computational operations behind Artificial Neural Networks before implementing complete neural network models using machine learning or deep learning frameworks.

## How to Run

Clone the repository and navigate to the required directory.

Example:

```bash
python loss_functions.py
```

For the visualization program:

```bash
python activation_function_visualization.py
```

Make sure the required Python libraries are installed:

```bash
pip install numpy matplotlib
```

## Concepts Demonstrated

```text
Input
  ↓
Weighted Sum
  ↓
Activation Function
  ↓
Prediction
  ↓
Loss / Error
  ↓
Weight Update
```

This repository is part of my machine learning and deep learning practice, focusing on understanding ANN fundamentals through Python implementations.


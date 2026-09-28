#---------------------------------------------------
# Accept input values from -10 to 10
# Plot Sigmoid, ReLU and Tanh using Matplotlib
# Explain each activation function
#---------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------------
# Activation Function : ReLU
#---------------------------------------------------
def ReLU(x):
    return np.maximum(0,x)
#---------------------------------------------------
# Activation Function : Sigmoid
#---------------------------------------------------
def Sigmoid(x):
    return 1/(1 + np.exp(-x))
#---------------------------------------------------
# Activation Function : Tanh
#---------------------------------------------------
def Tanh(x):
    return np.tanh(x)
#---------------------------------------------------
#Main Function 
#---------------------------------------------------
def main():
    inputs = np.arange(-10,11)

    ReLU_Y = ReLU(inputs)
    Sigmoid_Y = Sigmoid(inputs)
    Tanh_Y = Tanh(inputs)

    plt.plot(inputs,Sigmoid_Y,label="Sigmoid")
    plt.plot(inputs,ReLU_Y,label="ReLU")
    plt.plot(inputs,Tanh_Y,label="Tanh")

    plt.xlabel("Input (X)")
    plt.ylabel("Activation Output")
    plt.title("Activation Function")
    plt.axhline(0)
    plt.axvline(0)
    plt.legend()
    plt.grid(True)
    plt.show()

#---------------------------------------------------
#Entry Point of Program
#---------------------------------------------------

if __name__ == "__main__":
    main()
import numpy as np
import math

border = "-"*40
#---------------------------------------------------
# Activation Function : Sigmoid
#---------------------------------------------------
def Sigmoid(z):
    return 1/(1+math.exp(-z))

#---------------------------------------------------
#Function to Calculate Weighted Sum
#--------------------------------------------------
def SigmoidNeuronCalculate(inputs,weights,bias):
    z = np.dot(inputs,weights)+bias
    print("Weighted sum : ",z)
    print(border)

    Y = Sigmoid(z)
    return Y
#---------------------------------------------------
#Main Function 
#---------------------------------------------------
def main():
    inputs = np.array([2,3])
    print("X : ",inputs)
    print(border)

    weights = np.array([0.4,0.6])
    print("Weights : ",weights)
    print(border)

    bias = 0.5
    print("Bias : ",bias)
    print(border)

    Y = SigmoidNeuronCalculate(inputs,weights,bias)
    print("Final Result : ",Y)
    print(border)

    if (Y>0.5):
        print("Y is Closer to 1")
        print(border)
    else:
        print("Y is closer to 0 ")

#---------------------------------------------------
#Entry Point of Program
#---------------------------------------------------
if __name__ == "__main__":
    main()
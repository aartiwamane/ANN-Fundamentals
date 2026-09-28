#Activation Function
def ReLU(x):
    return max(0,x)

def UpdateWeight(Input,Weight,Bias,Y_True,Learning_Rate):
    #Calculate Prediction 
    Z = Input*Weight+Bias

    #Add non-linearity 
    Y_Pred = ReLU(Z)

    #Calculate Error
    error = Y_True-Y_Pred

    #Store Old Weight
    Old_W = Weight

    #Update Weight
    Weight = Weight +Learning_Rate*error*Input

    print("Prediction : ",Y_Pred)
    print("Error : ",error)
    print("Old Weight : ",Old_W)
    print("Updated weight : ",Weight)

#---------------------------------------------------
# Main Function 
#---------------------------------------------------
def main():
    Input = 2
    Weight = 0.5
    Bias = 0.1
    Y_true = 1
    Learning_Rate = 0.1

    UpdateWeight(Input,Weight,Bias,Y_true,Learning_Rate)

#---------------------------------------------------
# Entry Point function
#---------------------------------------------------
if __name__ == "__main__":
    main()
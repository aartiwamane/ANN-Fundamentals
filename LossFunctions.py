#---------------------------------------------------
#Function to Calculate Mean Squared Error
#--------------------------------------------------
def CalculateMSE(Y_True,Y_Pred):
    n = len(Y_True)
    total_error = 0

    for i in range(n):
        error = Y_True[i]-Y_Pred[i]
        total_error = total_error+(error**2)

    MSE = total_error/n
    return MSE
import math

#---------------------------------------------------
#Function to Calculate Binary Croass Entropy
#--------------------------------------------------
def CalculateBCE(Y_True, Y_Pred):
    n = len(Y_True)
    total_loss = 0

    for i in range(n):
        loss = -(Y_True[i] * math.log(Y_Pred[i]) +
                 (1 - Y_True[i]) * math.log(1 - Y_Pred[i]))

        total_loss = total_loss + loss

    BCE = total_loss / n
    return BCE

#---------------------------------------------------
# Main Function 
#---------------------------------------------------
def main():
    Y_True = [10,20,30]
    Y_Pred = [12,18,28]

    loss = CalculateMSE(Y_True,Y_Pred)
    
    print("MSE Loss : ",loss)

    Y_True = [1,0,1,1]
    Y_Pred = [0.9,0.2,0.8,0.7]

    BCE_Loss = CalculateBCE(Y_True,Y_Pred)
    print("BSE Loss : ",BCE_Loss)

#---------------------------------------------------
# Entry Point function
#---------------------------------------------------
if __name__ == "__main__":
    main()

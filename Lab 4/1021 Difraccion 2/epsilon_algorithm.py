import numpy as np
import pandas as pd


# Algoritmo de Similitud Aplicado
# corre un for internamente
 # funcion para buscar match dentro de un porcentaje de error
def epsilon_difference(x, datapoint, epsilon):
    #print("Difference is:", abs( 1 - x / datapoint))
    if(abs(1 - x / datapoint) <= epsilon ):
        #print("... match")
        return x, datapoint 
    else:
        #print("No data matching conditions")
        return 0, 0

def epsilon_loop(comparewith, data, epsilon=0.005, epsilonLimit=0.2):    
    while (epsilon <= epsilonLimit):
        #print("epsilon:",epsilon)
        Ndata = len(data)
        x = np.zeros(Ndata)
        dataR = np.zeros(Ndata)

        for jth, datapoint in enumerate(data):
            #print(datapoint)
            x[jth], dataR[jth] = epsilon_difference(comparewith , datapoint, epsilon)

        x = x[x > 1e-16] # sobre el machine error, 10e-16 se debe ver como 0
        dataR = dataR[dataR > 1e-16]
        if (len(x) > 0):
            #print(x, dataR)
            return x, dataR, epsilon
        elif (epsilon <= epsilonLimit):
            #print(epsilon)
            epsilon += 0.005 
        else:
            break


def compara2df(dfsmall, dfbig, epsilon=0.005, epsilonLimit=0.2):
    """
    compara dos dataframes mediante diferencias porcentuales de epsilon,
    se ha de utilizar pandas Series, por tanto si tiene un array, corta
    la seccion importante con un slicing

    dfbig = vapor_agua["lambdas nm"]
    df = hidrogeno["lambdas nm"]
    """
    x = np.zeros(len(dfbig))
    dataResult = np.zeros(len(dfbig))
    epsilon_DF = np.zeros(len(dfbig))

    for ith, datapoint in enumerate(dfbig):
        #print("ith", ith)
        z = epsilon_loop(datapoint, dfsmall, epsilon, epsilonLimit)
        x[ith], dataResult[ith], epsilon_DF[ith]  = z[0], z[1], z[2]

    return x, dataResult, epsilon_DF



if __name__ == "__main__":
    # Ejemplo con los datos de agua e hidrogeno
    vaporagua = pd.read_csv("./vaporagua.csv")
    hidrogeno = pd.read_csv("./hidrogeno.csv")
    #vaporagua['lambda m']

    hidrogeno["lambda m"] = hidrogeno["lambda nm"] * 1e-9


    # aunque es mejor trabajr en nanometros para alejarnos del machep
    vaporagua["lambda nm"] = vaporagua["lambda m"] * 1e9

    #hidrogeno

    df = hidrogeno["lambda nm"]
    x, dataResult, epsilon_DF = compara2df(dfsmall = df, dfbig=vaporagua["lambda nm"])

    comparacion = pd.DataFrame(
        {
            "hidrogeno": x,
            "vapor agua": dataResult,
            "epsilon algorithm": epsilon_DF
        }
    )
    comparacion
    # comparacion.to_csv("./epsilon_agua_hidrogeno.csv")
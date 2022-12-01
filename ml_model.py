from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
import pickle

def create_simple_model():
   "Training function for rent prediction"
   
   dataset = read_csv("rents_Merida.csv")
   X= dataset[['bedroom','bathroom','area','parking']].values
   y= dataset[['price']].values
   #X_train,X_validation,y_train,y_validation=train_test_split(X.reshape(-1,1),y,test_size=0.20, random_state=1, shuffle=True)
   lin_reg=LinearRegression()
   lin_reg.fit(X, y)
   #This line creates a "pikle" file that contains the predictive model.
   pickle.dump(lin_reg, open('simple_model.pkl','wb'))
   

# =======================================================================================
def get_r2_score(predictions):
    """ Esta función convierte las predicciones en r2.
        :param predictions: La lista de predicciones calificadas
        :return: Un diccionario con la matriz de confusión del modelo
    """
    y_true = []
    y_pred = []
    for prediction in predictions:
        y_true.append(prediction.observed_price)
        y_pred.append(prediction.predicted_price)
        r2= -1*r2_score(y_pred,y_true,)
    
    return r2


# =======================================================================================
if __name__ == '__main__':
    """ Esta función ejecuta el programa de Python cuando se invoca desde 
        línea de comando.
    """
    create_simple_model()

 
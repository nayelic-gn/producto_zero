import math
from datetime import datetime
from model_api import db

# =======================================================================================
# Esta clase mapea una predicción a una tabla en la base de datos mediante la biblioteca
# SQL Alchemy. Consulta la documentación de SQL Alchemy aquí:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
#
# Las columnas está adaptadas para el modelo de ejemplo de tipos de flores 
# (https://en.wikipedia.org/wiki/Iris_flower_data_set). Modifica el nombre de esta 
# clase para que sea más acorde a lo que hace tu modelo predictivo.
#
# ** IMPORTANTE: ** Cualquier modificación a las bases de datos requiere eliminar el
#       archivo de SQLite3 para que SQL Alchemy pueda reconstruir la base de datos
class Prediction(db.Model):
    """ Una prediccion en la base de datos
    """
    __tablename__ = 'prediction' # Nombre de la tabla en la base de datos
    
    # -----------------------------------------------------------------------------------
    # Declaración de columnas de la tabla. Modifica estas propiedades para que sean
    # más acorde a las variables que componen una observación de tu modelo.
    # La columna ID será la llave primaria de la predicción
    
    prediction_id = db.Column('id', db.Integer, primary_key=True)
    bedroom=db.Column('bedroom', db.Float, nullable=False)
    bathroom=db.Column('bathroom',db.Float, nullable=False)
    area=db.Column('area',db.Float,nullable=False)
    parking=db.Column('parking',db.Float,nullable=False)
    predicted_price=db.Column('price',db.Float,nullable=True)
    observed_price = db.Column('observed_price', db.Float, nullable=True)
    created_date=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   
   
    
    def __init__ (self, representation=None):
        """ Construye una Prediccion nueva usando su representación REST
        """
        super(Prediction,self).__init__()
   
        # ** IMPORTANTE: ** Cualquier modificación a las bases de datos requiere eliminar 
        #     el archivo de SQLite3 para que SQL Alchemy pueda reconstruir la base de datos
        self.bedroom =representation.get('bedroom')
        self.bathroom = representation.get('bathroom')
        self.area = representation.get('area')
        self.parking = representation.get('parking')
        self.observed_price = representation.get('observed_price')
        
    def __repr__(self):

        """ Convierte una Predicción a una cadena de texto
        """
        template_str ='''<Predicition [{}]: bedroom={},bathroom={},area={},parking={},price={},observed_price={}>'''.strip()
        return template_str.format(
            str(self.prediciton_id) if self.prediciton_id else 'NOT COMMITED',
            self.bedroom,
            self.bathroom, 
            self.area,
            self.parking,
            self.precio or "No Calculado",
            self.observed_price or 'No reportado'
            )
        
from sklearn import linear_model
from numpy import genfromtxt

### importamos los datos como un elemento de numpy
mis_datos = genfromtxt('Variables_Climaticas.csv', delimiter=',')
mis_datos_corr = mis_datos[1:,:]
mis_datos_corr

### generamos la correlacion lineal con LinearRegresion 
clf = linear_model.LinearRegression()
clf.fit(mis_datos_corr[:,1:],mis_datos_corr[:,:1])

### imprimimos los coeficientes
clf.coef_

### imprimimos el factor independiente
clf.intercept_

### vemos los valores predecidos con a correlacion
clf.predict(mis_datos_corr[:,1:])






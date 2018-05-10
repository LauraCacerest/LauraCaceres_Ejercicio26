import numpy as np
import matplotlib.pyplot as plt

g=9.8


#Puntos aleatorios
puntos=np.random.uniform(35.0,45.0,1000000)
theta= np.random.uniform(0,np.pi/2.0,1000000)

#Velocidades de Observacion
observacion_1=[66.0,110.0,26.0,172.0]
observacion_2=[56.0,120.0,36.0,182.0]

for i in range(len(observacion_1)):
    distancia=(puntos[i]**2*np.sin(2*theta[i]))/g

    
    puntos=puntos[d]

    puntos=np.random.choice(puntos,1000000)

    theta= theta[:len(puntos)]

    print(len(puntos))

 

for i in range(len(observacion_2)):
    distancia=(puntos[i]**2*np.sin(2*theta[i]))/g

   
    puntos=puntos[d]

    puntos=np.random.choice(puntos,1000000)

    theta= theta[:len(puntos)]

    
    print (len(puntos))

    plt.figure()

    plt.xlabe('Velocidad')
    plt.ylabel('Probabilidad de la Velocidad')
    plt.hist(puntos,1000, normed=1 )
    plt.legend()
    plt.savefig('Histograma_vel.png')


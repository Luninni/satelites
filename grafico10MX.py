import matplotlib.pyplot as plt 

nombreArchivo="2019-06-13_16_48_21_mtq1_duty_10.csv"
archivo=open(nombreArchivo,"r")
mx=[]
time=[]
stringDatos=archivo.readline()
while(stringDatos!=""):
    dataStr=stringDatos.split(",")
    #obtener el mx y agregarlo al arreglo mx
    mx.append(float(dataStr[0]))
    #obtener el time y agregarlo al arreglo time
    time.append(float(dataStr[6]))
    stringDatos=archivo.readline()
archivo.close()

plt.plot(time,mx)
plt.xlabel("Tiempo")
plt.ylabel("mx")
plt.title("Eje x de M en función del tiempo")
plt.show()




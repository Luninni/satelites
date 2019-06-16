import matplotlib.pyplot as plt 

nombreArchivo="2019-06-13_16_48_21_mtq1_duty_10.csv"
archivo=open(nombreArchivo,"r")
mx=[]
my=[]
mz=[]

gx=[]
gy=[]
gz=[]

time=[]

tail1=[]
tail2=[]
tail3=[]

checksum=[]
stringDatos=archivo.readline()
while(stringDatos!=""):
    dataStr=stringDatos.split(",")
    #obtener el m y agregarlo al arreglo mx
    mx.append(float(dataStr[0]))
    my.append(float(dataStr[1]))
    mz.append(float(dataStr[2]))
    
    #obtener el g y agregarlo al arreglo my
    gx.append(float(dataStr[3]))
    gy.append(float(dataStr[4]))
    gz.append(float(dataStr[5]))

    #obtener el time y agregarlo al arreglo time
    time.append(float(dataStr[6]))
    
    #obtener el tail y agregarlo a su arreglo
    tail1.append(float(dataStr[7]))
    tail2.append(float(dataStr[8]))
    tail3.append(float(dataStr[9]))
    stringDatos=archivo.readline()
archivo.close()

plt.plot(time,mx)
plt.xlabel("Tiempo")
plt.ylabel("mx")
plt.title("Eje x de M en función del tiempo")
plt.show()



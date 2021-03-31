library(normtest) ###REALIZA 5 PRUEBAS DE NORMALIDAD###
library(nortest) ###REALIZA 10 PRUEBAS DE NORMALIDAD###
library(moments) ###REALIZA 1 PRUEBA DE NORMALIDAD###

datos<-read.delim("clipboard",header = T)
datos

hist(datos[,1])
ad.test(datos[,1])
lillie.test(datos[,1])
###Prueba de Shapiro-Wilk###
###Es más poderosa cuando se compara con otras pruebas de normalidad cuando la muestra es pequeña.###
shapiro.test(datos[,1])
pearson.test(datos[,1])


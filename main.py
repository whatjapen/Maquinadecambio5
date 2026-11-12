#EJERCICIO 5
#Una máquina expendedora necesita calcular el cambio que debe devolver. Escribe un programa que pida el importe de la compra y el dinero entregado por el cliente (ambos en euros, con decimales) y muestre:
#Juan Agea Rodríguez
#12/11/2026
#Se multiplica por 100 para sacarlo primero en centimos enteros con el round
importe=round(float(input("Introduzca importe: ")) * 100)
dineroentregado=round(float(input("Introduzca el dinero entregado: ")) * 100)
#Luego para sacar el cambio es tan sencillo como restar lo que debe con lo que se da y te saldra en centimos
cambio=dineroentregado-importe
#Se toma de base centimos y se calcula diviendo y guardando el resto, asi sucesivamente con cada uno.
print("cambio ",cambio)
billete20=cambio//2000
cambio = cambio % 2000
print (f"{billete20:.0f}")

billete10=cambio//1000
cambio = cambio % 1000
print (f"{billete10:.0f}")

billete5=cambio//500
cambio = cambio % 500
print (f"{billete5:.0f}")

billete2=cambio//200
cambio = cambio % 200
print (f"{billete2:.0f}")

billete1=cambio//100
cambio = cambio % 100
print (f"{billete1:.0f}")

monedas50cent=cambio//50
cambio = cambio % 50
print (f"{monedas50cent:.0f}")

monedas20cent=cambio//20
cambio = cambio % 20
print (f"{monedas20cent:.0f}")

monedas10cent=cambio//10
cambio = cambio % 10
print (f"{monedas10cent:.0f}")

monedas5cent=cambio//5
cambio = cambio % 5
print (f"{monedas5cent:.0f}")
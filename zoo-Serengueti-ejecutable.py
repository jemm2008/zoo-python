#
from modulos_zoo.zoo import Zoo
#
 #############################################################################################
#################################EJECUCION#####################################################
 #############################################################################################
print("Creando SERENGUETI Zoo")
zoo1 = Zoo("SERENGUETI Zoo")
print("SERENGUETI Zoo ha sido Creado\n")
#
print("Anhadiendo al Guepardo de nombre RAPIDOX")
zoo1.add_guepardo("RAPIDOX", 7)
print("RAPIDOX anhadido a SERENGUETI Zoo\n")
#
print("Anhadiendo a la Gacela de nombre SALTARINA")
zoo1.add_gacela("SALTARINA", 3)
print("SALTARINA anhadida a SERENGUETI Zoo\n")
#
print("Anhadiendo al Elefante de nombre TANTOR")
zoo1.add_elefante("TANTOR", 31)
print("TANTOR anhadido a SERENGUETI Zoo\n")
#
zoo1.print_all_info()
#
print("#"*17 + "VAMOS A ALIMENTARLOS!¡¡!" + "*"*17)
zoo1.feed_allzoo()
print("...despuEs de COMER................................\n\n")
zoo1.print_all_info()
#
#
####################################################################################
##EjecuciOn#Antigua##Cuando#todas#las#clases#estaban#en#un#solo#Archivo##############
####################################################################################
# comelon = Guepardo("COMELON", 11)
# comelonFood = Gacela("SABROZZA", 3)
# tantor = Elephant("TANTOR", 37, weightin = 5377)
#
# comelon.animmal_info()
# comelonFood.animmal_info()
# tantor.animmal_info()
# 
# comelon.hora_de_comer()
# comelonFood.hora_de_comer()
# tantor.hora_de_comer()
# 
# print("---> DESPUES DE COMER:")
# comelon.animmal_info()
# comelonFood.animmal_info()
# tantor.animmal_info()
#####################################################################################
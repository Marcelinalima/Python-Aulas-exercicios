	
class Maquina(object):
	def Conversar(self):
		print('Sou uma maquina')

class Robo(Maquina):
	def ConversarRobo(self):
		print ('Sou um robo')

Amigo1 = Maquina()
Amigo2 = Robo()

Amigo1.Conversar()
Amigo2.Conversar()




                     




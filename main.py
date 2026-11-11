import utility
import plant
import movement

while(True) : 
	for i in range(get_world_size()):
		if(get_pos_x() == 1):
			plant.dylans_bush()
			utility.schmovement()
		elif(get_pos_x() == 2):
			plant.carrot_type()
			utility.schmovement()
		elif(get_pos_x() > 2 and get_pos_x() < 6):
			plant.carrot_type()
			utility.schmovement()
		else:
			if (can_harvest()): 
				harvest() 
				utility.schmovement()

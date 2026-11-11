import movement

def carrot_type():
	if(get_ground_type() != Grounds.Soil):
		till()
	if(can_harvest()):
		harvest()
		plant(Entities.Carrot)
	else:
		if(get_ground_type() == Grounds.Soil):
			plant(Entities.Carrot)

		
def dylans_bush():
	if (can_harvest()): 
		harvest()
		plant(Entities.Bush)

# Plant pumpkins/till land within bounds
# Track x/y position of coordinates where can_harvest == false || get_entity_type() == Entities.Dead_Pumpkin and push to stack
# Pop each invalid position from stack and ensure it becomes fully grown
# Once stack is empty, harvest and move outside of pumpkin grid
def PUMPKIN(start_coordinates, end_coordinates):

	start_x, start_y = start_coordinates
	end_x, end_y = end_coordinates
	rows = end_x - start_x 
	cols = end_y - start_y

	bad_stack = []

	movement.move_to(start_x, start_y)

	direction = East

	for _ in range(rows):
		for _ in range(cols):
			if(get_ground_type() != Grounds.Soil):
					till()

			plant(Entities.Pumpkin)
			bad_stack.append([get_pos_x(), get_pos_y()])
			move(direction)

		move(North)

		if(direction == East):
			direction = North
		else:
			direction = East

	while(len(bad_stack) > 0):
		x, y = bad_stack.pop()

		movement.move_to(x, y)

		while(can_harvest() == False):
			do_a_flip()
			
			if(get_entity_type() == Entities.Dead_Pumpkin):
				plant(Entities.Pumpkin)

	movement.move_to(end_x, end_y + 1)

	
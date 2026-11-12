import movement

# Matcha so good
def grass_muncher(start_coordinates, end_coordinates):
	
	start_x, start_y = start_coordinates
	end_x, end_y = end_coordinates
	rows = end_x - start_x + 1
	cols = end_y - start_y + 1
	
	movement.move_to(start_x, start_y)

	def _grass_logic():
		if(can_harvest()):
			harvest()

		plant(Entities.Grass)

	movement.traverse_grid(rows, cols, _grass_logic)

# Friggen bush-whacka.
def dylans_bush(start_coordinates, end_coordinates):
	
	start_x, start_y = start_coordinates
	end_x, end_y = end_coordinates
	rows = end_x - start_x + 1
	cols = end_y - start_y + 1
	
	movement.move_to(start_x, start_y)

	def _bush_logic():
		if can_harvest():
			harvest()
			plant(Entities.Bush)

	movement.traverse_grid(rows, cols, _bush_logic)

# Eh, what's up doc?
def carrot_type(start_coordinates, end_coordinates):

	start_x, start_y = start_coordinates
	end_x, end_y = end_coordinates
	rows = end_x - start_x + 1
	cols = end_y - start_y + 1
	
	movement.move_to(start_x, start_y)

	def _carrot_logic():
		if(can_harvest()):
			harvest()
			
			if(get_ground_type() != Grounds.Soil):
					till()

			plant(Entities.Carrot)

	movement.traverse_grid(rows, cols, _carrot_logic)

# Plant pumpkins/till land within bounds.
# Push all x/y positions to stack for immediate traversal.
# Pop each invalid position from stack and move to it, ensure pumpkin becomes fully grown.
# Once stack is empty, harvest.
# Currently traverses entire grid twice. Waits for good pumpkins to grow. Could be more efficient?
# PUMPKIN.
def PUMPKIN(start_coordinates, end_coordinates):

	start_x, start_y = start_coordinates
	end_x, end_y = end_coordinates
	rows = end_x - start_x + 1
	cols = end_y - start_y + 1
	bad_stack = []

	movement.move_to(start_x, start_y)

	def _pumpkin_logic():
		if(get_ground_type() != Grounds.Soil):
			till()

		plant(Entities.Pumpkin)
		bad_stack.append([get_pos_x(), get_pos_y()])

	movement.traverse_grid(rows, cols, _pumpkin_logic)

	while(len(bad_stack) > 0):
		x, y = bad_stack.pop()

		movement.move_to(x, y)

		while(can_harvest() == False):
			if(get_entity_type() == Entities.Dead_Pumpkin):
				plant(Entities.Pumpkin)
			
			do_a_flip()
	
	harvest()

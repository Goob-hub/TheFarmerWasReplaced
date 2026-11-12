def schmovement():
	if(get_pos_y() == get_world_size() - 1):
		move(North)
		move(East)
	else:
		move(North)

def move_to(x, y):
	while get_pos_x() != x :
		cur_x = get_pos_x()

		if cur_x < x:
			move(East)
		elif cur_x > x:
			move(West)
			
	while get_pos_y() != y:
		cur_y = get_pos_y()
		
		if cur_y < y:
			move(North)
		elif cur_y > y: 
			move(South)	
			
def traverse_grid(rows, cols, traversal_logic):
	direction = East

	for row in range(rows):
		for col in range(cols):
			traversal_logic()
			
			if col < cols - 1: 
				move(direction)
		
		if row < rows - 1:
			move(North)

		if(direction == East):
			direction = West
		else:
			direction = East

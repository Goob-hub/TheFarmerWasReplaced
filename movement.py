def schmovement():
	if(get_pos_y() == get_world_size() - 1):
		move(North)
		move(East)
	else:
		move(North)

def move_to(x, y):
	while(get_pos_x() != x & get_pos_y() != y):
		cur_x = get_pos_x()
		cur_y = get_pos_y()

		if(cur_x < x):
			move(West)
		else:
			move(East)

		if(cur_y < y):
			move(North)
		else: 
			move(South)
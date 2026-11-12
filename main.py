import utility
import plant
import movement

grass_start = [0, 0]
grass_end = [2, 2]

bush_start = [0, 3]
bush_end = [2, 5]

carrot_start = [3, 3]
carrot_end = [5, 5]

pumpkin_start = [3, 0]
pumpkin_end = [5, 2]

while(True) : 
	plant.grass_muncher(grass_start, grass_end)
	plant.dylans_bush(bush_start, bush_end)
	plant.carrot_type(carrot_start, carrot_end)
	plant.PUMPKIN(pumpkin_start, pumpkin_end)


if __name__ == '__main__':
	file=open('divide.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	num_of_shopping_centers=int(data[0][0])
	num_of_roads=int(data[0][1])
	types_of_fish=int(data[0][2])
	print (num_of_shopping_centers,num_of_roads,types_of_fish)
	fish_by_city={}
	for i in range(1, num_of_shopping_centers+1):
		fish_by_city[int(data[i][0])]=[int(data[i][j]) for j in range(1, len(data[i]))]
	print  (fish_by_city)
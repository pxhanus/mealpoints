def mealpoints():
	
	f = open("mealpoints.txt", "r")
	str_points = f.readlines()[0]
	f.close()

	points_strip = str_points.strip("\xef\xbb\xbf")
	meal_points = float(points_strip)

	used_points = float(input("How many points did you use?" ))

	meal_points -= used_points
	meal_points = str(meal_points)


	f = open("mealpoints.txt", "w")
	f.write(meal_points)
	f.close()


if __name__ == "__main__":
	mealpoints()
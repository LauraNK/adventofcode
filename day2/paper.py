f = open('input.txt', 'r')
gifts = f.read()
f.close()


def surface_area(l, w, h):
	return 2 * l * w + 2 * w * h + 2 * h * l

def total_wrap(l, w, h):
	return surface_area(l, w, h) + min(l * w, l * h, w * h)
  

def get_total():
	total = 0
	for gift in gifts.split("\n"):
		if len(gift) == 0: break
		l,w,h = map(int, gift.split("x"))
		total = total + total_wrap(l, w, h)

	print(total)

get_total()
	
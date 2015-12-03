f = open('input.txt', 'r')
gifts = f.read()
f.close()


def ribbon_length(l, w, h):
	return l*w*h + 2*l+2*w+2*h - max(l,w,h)*2
  
def get_total():
	total = 0
	for gift in gifts.split("\n"):
		if len(gift) == 0: break
		l,w,h = map(int, gift.split("x"))
		total = total + ribbon_length(l, w, h)

	print(total)

get_total()
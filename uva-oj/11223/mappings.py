import sys 

def pretty_print(l, n):
	size = len(l)
	inner_join = lambda k, maxim: ("{\"%s\", '%s'}" %(l[j+1], l[j]) for j in xrange(k, maxim, 2))
	return ",\n".join(", ".join(inner_join(k, min(k + n * 2, size))) for k in xrange(0, size, (n * 2)))

if __name__ == '__main__':
	l = ['A', '.-', 'J', '.---', 'S', '...', '1', '.----', '.', '.-.-.-', ':', '---...', 
	'B', '-...', 'K', '-.-', 'T', '-', '2', '..---', ',', '--..--', ';', '-.-.-.', 'C', 
	'-.-.', 'L', '.-..', 'U', '..-', '3', '...--', '?', '..--..', '=', '-...-', 'D', '-..', 
	'M', '--', 'V', '...-', '4', '....-', '\'', '.----.', '+', '.-.-.', 'E', '.', 
	'N', '-.', 'W', '.--', '5', '.....', '!', '-.-.--', '-', '-....-', 'F', '..-.', 'O', '---', 
	'X', '-..-', '6', '-....', '/', '-..-.', '_', '..--.-', 'G', '--.', 'P', '.--.', 'Y', '-.--', 
	'7', '--...', '(', '-.--.', '"', '.-..-.', 'H', '....', 'Q', '--.-', 'Z', '--..', 
	'8', '---..', ')', '-.--.-', '@', '.--.-.', 'I', '..', 'R', '.-.', '0', '-----', '9', '----.', 
	'&', '.-...']

	try:
		rpl = int(sys.argv[1]) % 10
	except ValueError as err:
		print "Warning: Ignoring '%s'\n%s" % (sys.argv[1], err.message)
		rpl = 1

	print pretty_print(l, rpl)

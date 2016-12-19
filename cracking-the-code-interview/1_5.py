# Returns True if phrase1 is one edit away from phrase 2.
# An edit is inserting, removing, or replacing a character from phrase 1 to phrase2.

def can_insert_remove(phrase1, phrase2, max_chars):
	not_matching = False
	for i in range(max_chars):
		c1 = None
		c2 = None
		if i < len(phrase1):
			c1 = phrase1[i]
		if i < len(phrase2):
			c2 = phrase2[i]
		
		if c1 != c2:
			if not_matching:
				return False
			not_matching = True
	return True

def can_replace(phrase1, phrase2):
	not_matching = False
	for i in range(len(phrase1)):
		c1 = phrase1[i]
		c2 = phrase2[i]
		if c1 != c2:
			if not_matching:
				return False
			not_matching = True
	return True

def one_away(phrase1, phrase2):
	max_chars = len(phrase1) if len(phrase1) > len(phrase2) else len(phrase2)
	if len(phrase1) != len(phrase2):
		return can_insert_remove(phrase1,phrase2,max_chars)
	else:
		return can_replace(phrase1,phrase2)

print("lale, lales: {}".format(one_away("lale","lales")))
print("david, dav: {}".format(one_away("david","dav")))
print("mississippi, mississippj: {}".format(one_away("mississippi","mississippj")))
print("kangaroo, kangggaroo: {}".format(one_away("kangaroo","kangggaroo")))

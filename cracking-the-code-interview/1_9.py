def is_substring(phrase1, phrase2):
	return phrase2 in phrase1

# waterbottlewaterbottle
# erbottlewat
def is_rotation(phrase1, phrase2):
	# Duplicate phrase1 such that phrase1 = phrase1 + phrase1.
	p1 = phrase1 + phrase1
	return is_substring(p1, phrase2)

print("waterbottle, erbottlewat: {}".format(is_rotation("waterbottle","erbottlewat")))
print("unmatched, unmatchedno: {}".format(is_rotation("unmatched","unmatchedno")))

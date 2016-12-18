# If the phrase has an odd number of characters, it must have 1 character that occurs once.
# If the phrase has an even number of characters, each character must occur an even number of times.
# So, the phrase can't have more than 1 character that occurs an odd amount of times.

def is_permutation_palindrome(phrase):
	# Frequency table.
	char_counts = {}
	
	odd_found = False

	# Go through each character, create frequence table.
	for c in phrase:
		if c not in char_counts:
			char_counts[c] = 0
		char_counts[c] += 1
		

	# Go through each character frequency, return false if there are > 1 characters with an odd count.
	for c in char_counts:
		if char_counts[c] % 2 == 1:
			if odd_found:
				return False
			odd_found = True
	
	return True
	
print(is_permutation_palindrome("star"))
print(is_permutation_palindrome("racecar"))
print(is_permutation_palindrome("rc ae rac"))
print(is_permutation_palindrome("dood"))

# Compresses string phrase such that repeated characters are changed with the original character + its count.
# If the compressed string phrase is not shorter than the original phrase, keep the original phrase.
# i.e. daaaavvidddd is compressed to d1a4v2i1d4

def compress_string(phrase):
	new_phrase = ""
	last_char = phrase[0]
	char_count = 0
	for i in range(len(phrase)):
		if phrase[i] == last_char:
			char_count += 1
		if phrase[i] != last_char or i == len(phrase)-1:
			new_phrase += (last_char + str(char_count))
			char_count = 1

		last_char = phrase[i]
	
	final_phrase = new_phrase if len(new_phrase) < len(phrase) else phrase
	return final_phrase

print("daavviddd: ", compress_string("daavviddd"))
print("elllleeepphaaantttt: ", compress_string("elllleeepphaaantttt"))

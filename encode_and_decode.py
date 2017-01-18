def Encode(text):
	current_location = 0
	new_text = text
	while current_location < len(text):
		if new_text[current_location] == '1':
			new_text = new_text.replace('1', 'A')
		elif new_text[current_location] == '2':
			new_text = new_text.replace('2', 'b')
		elif new_text[current_location] == '3':
			new_text = new_text.replace('3', 'c')
		elif new_text[current_location] == 'a':
			new_text = new_text.replace('a', '*')
		elif new_text[current_location] == 'J':
			new_text = new_text.replace('J', '@')
		elif new_text[current_location] == 'n':
			new_text = new_text.replace('n', ')')
		elif new_text[current_location] == 'o':
			new_text = new_text.replace('o', '[')
		elif new_text[current_location] == 's':
			new_text = new_text.replace('s', '$')
		else:
			print 'error'
			break
		current_location = current_location + 1
    	return new_text

def Decode(text):
	current_location = 0
	new_text = text
	while current_location < len(text):
		if new_text[current_location] == 'A':
			new_text = new_text.replace('A', '1')
		elif new_text[current_location] == 'b':
			new_text = new_text.replace('b', '2')
		elif new_text[current_location] == 'c':
			new_text = new_text.replace('c', '3')
		elif new_text[current_location] == '*':
			new_text = new_text.replace('*', 'a')
		elif new_text[current_location] == '@':
			new_text = new_text.replace('@', 'J')
		elif new_text[current_location] == ')':
			new_text = new_text.replace(')', 'n')
		elif new_text[current_location] == '[':
			new_text = new_text.replace('[', 'o')
		elif new_text[current_location] == '$':
			new_text = new_text.replace('$', 's')
		else:
			print 'error'
			break
		current_location = current_location + 1
    	return new_text

encoded_text = Encode('Jason123')

print Encode('Jason123')
print Decode(encoded_text)

print("Type STDIN multiline input; CTRL+D to finish.")
CLIInput = []
while True:
	try:
		CLIInput.append(input())
	except EOFError:
		break

print(CLIInput)

normal = input("Normal Input:")

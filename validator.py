def validate(data):
	try:
		int(data)
		dreturn True
	except ValueError:
		return False

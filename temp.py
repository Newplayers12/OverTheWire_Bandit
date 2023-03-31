s = "Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi"

for c in s:
	if c.isalpha():
		number = ord(c) - (ord('a') if c >= 'a' else ord('A'))
		print(chr((number - 13) %26 + (ord('a') if c >= 'a' else ord('A'))), end = "")
	else:
		print(c, end = "")
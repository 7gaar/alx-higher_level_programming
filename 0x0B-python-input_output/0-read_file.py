#!/usr/bin/python3
"""
a function that reads a text file
"""

def read_file(filename=""):
	"""reads a file (utf-8) and prints content to stdout"""
	with open("filename", encoding="utf-8") as f:
		content = f.read()
		print(content)

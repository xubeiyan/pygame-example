import struct
file = open("binary.dat", "rb")
size = struct.calcsize("i")
bytes_read = file.read(size)
while bytes_read:
	value = struct.unpack("i", bytes_read)
	value = value[0]
	print(value)
	bytes_read = file.read(size)
file.close()
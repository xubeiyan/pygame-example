import struct
file = open("binary.dat", "wb")
for n in range(1000):
	data = struct.pack('i', n)
	file.write(data)
file.close()
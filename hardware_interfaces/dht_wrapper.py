import subprocess

process = subprocess.Popen("./dht", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
input,output = process.stdin,process.stdout

while True:
	print(output.read().decode('latin1'))

input.close()
output.close()
status = process.wait()

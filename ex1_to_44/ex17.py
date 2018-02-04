from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

indata = (open(from_file)).read()

#All the following is not needed.
#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

out_file = (open(to_file, "w")).write(indata)

print("Alright, all done.")

#All the following is not needed. Because I copy the content directly to a variable
#and the file is directly closed automaticaly after the call in the funcion
#from_file.close()
#to_file.close()
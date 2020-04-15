#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode
#Read two lines of the file:
"""read files"""
f = open("demofile.txt", "rt")#Read - Default value. Opens a file for reading, error if the file does not exist
print(f.readline())
#return the 5 first characters of the file
print(f.readline(5)) 

f1 = open("demofile.txt", "at")#Append - Opens a file for appending, creates the file if it does not exist
f2 = open("demofile.txt", "wb")#Write - Opens a file for writing, creates the file if it does not exist
f3 = open("demofile4.txt", "xb")#Create - Creates the specified file, returns an error if the file exists
#In addition you can specify if the file should be handled as binary or text mode
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

#By looping through the lines of the file, you can read the whole file, line by line:
f4 = open("demofile.txt", "r")
for x in f4:
  print(x) 
  
f4 = open("demofile.txt", "r")
print(f4.readline())
f4.close() 



"""write to an existing file"""
#Open the file "demofile2.txt" and append content to the file:
f5 = open("demofile2.txt", "a")
f5.write("Now the file has more content!")
f5.close()
#open and read the file after the appending:
f5 = open("demofile2.txt", "r")
print(f5.read()) 

#Open the file "demofile3.txt" and overwrite the content:
f6 = open("demofile3.txt", "w")
f6.write("Woops! I have deleted the content!")
f6.close()
#open and read the file after the appending:
f6 = open("demofile3.txt", "r")
print(f6.read()) 


""" create a new file
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
 """
 #Create a file called "myfile.txt":
 f = open("myfile.txt", "x")
 #Create a new file if it does not exist:
 f = open("myfile.txt", "x")
 
 
 """Delete a file
 To delete a file, you must import the OS module, and run its os.remove() function:
"""
import os
os.remove("demofile.txt") 
     
#To avoid getting an error, you might want to check if the file exists before you try to delete it:Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 
  
#To delete an entire folder, use the os.rmdir() method:Remove the folder "myfolder":
#You can only remove empty folders.
import os
os.rmdir("myfolder") 

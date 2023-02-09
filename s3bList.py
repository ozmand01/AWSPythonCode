#File name: Lab.py
#Author: Millie Ozard
#Purpose: This is the working version that incorporates all the other test code
#Date created: 8/2/23
#Edited 9/2/23 - Added functions

#Imports essential AWS services
import sys
import boto3

#Calls the S3 service
s3 = boto3.client('s3')
response = s3.list_buckets()

#A function that prints the list of buckets in all regions
def printbuckets():
    result = 'Existing buckets:\n'
    for bucket in response['Buckets']:
        result += f'  {bucket["Name"]}\n'
    return result

#Asks the user if they want to list the buckets, only takes Yes or No as inputs
usrinput = input("Would you like to list the current buckets in Sydney? Yes or No: ")

#While loop that ensures the answer is "Yes" or "No" only
while usrinput != "Yes" or "No":
    
    #If the user says "No", break the loop
    if usrinput == "No":
        print("Awww. That makes me sad, these buckets are very friendly.")
        break
    
    elif usrinput == "Yes":
        
        #Opens file.txt and writes the output of the printbuckets function
        file = open("List.txt", 'w')
        file.write(printbuckets())
        file.close 
        print(printbuckets() + "This list has been saved in list.txt")
        break
    
    #Iterates the user input until the appropriate answer is given
    usrinput = input("Please enter 'Yes' or 'No': ")






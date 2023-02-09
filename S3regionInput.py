#File name: S3regioninput.py
#Author: Millie Ozard
#Purpose: This is the working version that incorporates all the other test code
#Date created: 9/2/23
#Edited 9/2/23 - Added inputs and outputs for specific regions

#Imports essential AWS services
import sys
import boto3

#Calls the S3 service
s3 = boto3.client('s3')
response = s3.list_buckets()

#Takes input from the user about which region they want to access
LocationConstraint = input("Would you like to use see the buckets in Canada, Sydney or Globally? ")

#Lists all the buckets in Canada
def canadabuckets():
    result = "Buckets in Canada:\n"
    for bucket in response["Buckets"]:
        location = s3.get_bucket_location(Bucket=bucket["Name"])["LocationConstraint"]
        if location == "ca-central-1":
            result += f'  {bucket["Name"]}\n'
    return result
    
#Lists all the buckets in Sydney
def sydneybuckets():
    result = "Buckets in Sydney:\n"
    for bucket in response["Buckets"]:
        location = s3.get_bucket_location(Bucket=bucket["Name"])["LocationConstraint"]
        if location == "ap-southeast-2":
            result += f'  {bucket["Name"]}\n'
    return result

#Lists all buckets
def globalbuckets():
    result = "All buckets:\n"
    for bucket in response["Buckets"]:
        result += f'  {bucket["Name"]}\n'
    return result

#Appends the Canadian buckets to List2.txt
if LocationConstraint == "Canada":
    print(canadabuckets())
    file = open("List2.txt", 'a')
    file.write(canadabuckets())
    file.close ()

#Appends the Sydney buckets to List2.txt
elif LocationConstraint == "Sydney":
    print(sydneybuckets())
    file = open("List2txt", 'a')
    file.write(sydneybuckets())
    file.close ()

#Appends all buckets to List2.txt
elif LocationConstraint == "Globally":
    print(globalbuckets())
    file = open("List2.txt", 'a')
    file.write(globalbuckets())
    file.close ()
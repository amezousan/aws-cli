import boto3

client   = boto3.client('ssm')

instanceId = "i-xxx"
typeName   = "AWS:Application"
nextToken  = ""
file       = open("testfile.txt","w") 
counter    = 0

while True:
    counter += 1
    if nextToken:
        response = client.list_inventory_entries(
            InstanceId=instanceId,
            TypeName=typeName,
            NextToken=nextToken
        )
    else:
        response = client.list_inventory_entries(
            InstanceId=instanceId,
            TypeName=typeName
        )

    file.write("%sth Run:\n" % counter)
    file.write("%s\n" % response["Entries"])

    # If there is next page.
    if "NextToken" in response:
        nextToken = response["NextToken"]
    else:
        break

file.close()

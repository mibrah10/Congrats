# Python code to pick a random
# word from a text file
import random
  
# Open the file in read mode
with open("MyFile.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
    print(random.choice(words))
    
    # function to delete item off bucket list 
    def delete_item(goal_name):
	bucketList = file.read.bucketList
	bucketList.remove({'name': goal_name})
	return "Goal deleted successfully!"

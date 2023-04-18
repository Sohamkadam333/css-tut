import requests
import mymodule


for x in range(4):
    response = requests.get('https://catfact.ninja/fact')
    mymodule.catFacts.append(response.json()['fact'])


# mymodule.printList(mymodule.catFacts)

def printList(x):
    for i in x:
        print(i)


printList(mymodule.catFacts)

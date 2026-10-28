n=str(input("enter the word"))
vowels=[x for x in n.lower() if x in["a","e","i","o","u"]]
print("the vowels in the words are: ",vowels)

w=input("enter a word")
ord=[ord(x) for x in w]
print("the oridinal value is:",ord)

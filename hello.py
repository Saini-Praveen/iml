Color,Height = input().split(" ")
Height= int(Height)
Color = Color.lower()
if Color =='yellow':
    if Height >= 10:
        print("Griraffe")
    else:
        print("Tiger")
else:
    if Height >= 10:
        print("Elephant")
    else:
        print("Monkey")
def area(length,width):
    print(str(length*width)+" square feet")
    return length * width

def main():
   hose=  area(80,60)
   yard= area(93,62)
   total= hose+yard
   print(str(total)+" total square feet")
main()
def calc_rectangle(length,width):
    area=length*width
    perimeter=2 * (length+width)
    return area,perimeter
l=int(input("enter the length:"))
w=int(input("enter thw width"))
area,perimeter=calc_rectangle(l,w)
print(f"Area:{area},Perimeter:{perimeter}")
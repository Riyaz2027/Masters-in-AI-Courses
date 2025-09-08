no_of_books = int(input("Enter the number of books purchased this month: "))
total_points = 0
if( no_of_books == 0 ):
    total_points += 0
elif ( no_of_books >= 2 and no_of_books < 4 ):
    total_points += 5
elif ( no_of_books >= 4 and no_of_books < 6 ):    
    total_points += 15
elif ( no_of_books >= 6 and no_of_books < 8 ):
    total_points += 30
elif ( no_of_books >= 8 ):
    total_points += 60
    
    
print(f"Total points earned this month: {total_points}")






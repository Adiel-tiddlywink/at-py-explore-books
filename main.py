import csv
#comma separating value

with open("YA_Books.csv", mode="r", encoding="utf-8") as bookfile:
    #r = reading
    #bookfile is an alias

    books = csv.reader(bookfile)
    #skip header row
    next(books)

    #author column at index 1
    minyear = 0
    minrating = 5
    maxrating = 0
    maxyear = 2021

    for row in books:
        # #print out author name w/ m
        # # if row[1].startswith("M"):
        # #     print(row[1])

        # #print last nme / slice
        # authorname = row[1]
        # lastindex = authorname.rfind(" ")
        # lastname = authorname[lastindex + 1]
        # if lastname.startswith("J"):
        #     print(authorname)

        # #find most recent book
        year = int(row[2])
        if minyear < year:
            minyear = year
            mostrecentbook = row

        #get book with worst rating
        rating = float(row[6])
        if minrating > rating:
            minrating = rating
            worst_rated_book = row

        #get book with higest rating
        rating2 = float(row[6])
        if maxrating < rating2:
            maxrating = rating
            best_rated_book = row

        #longest page count < 2000 yr
        pages = int(row[5])
        if minyear < maxyear:
            minyear = maxyear
            longest_page_count = row
            
    print(f"Most recent book: \n{mostrecentbook}")
    print(f"Worst rated book: \n{worst_rated_book}")
    print(f"Best rated book: \n{best_rated_book}")
    print(f"Longest page count b4 2000: \n{longest_page_count}")
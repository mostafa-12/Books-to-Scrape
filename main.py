import sys,os
from colorama import Fore, Style
import Scraper
def main():
    category = ["Travel",
        "Mystery",
        "Historical Fiction",
        "Sequential Art",
        "Classics",
        "Philosophy",
        "Romance",
        "Women's Fiction",
        "Fiction",
        "Children's",
        "Religion",
        "Nonfiction",
        "Music",
        "Default",
        "Science Fiction",
        "Sports and Games",
        "Add a comment",
        "Fantasy",
        "New Adult",
        "Young Adult",
        "Science",
        "Poetry",
        "Paranormal",
        "Art",
        "Psychology",
        "Autobiography",
        "Parenting",
        "Adult Fiction",
        "Humor",
        "Horror",
        "History",
        "Food and Drink",
        "Christian Fiction",
        "Business",
        "Biography",
        "Thriller",
        "Contemporary",
        "Spirituality",
        "Academic",
        "Self Help",
        "Historical",
        "Christian",
        "Suspense",
        "Short Stories",
        "Novels",
        "Health",
        "Politics",
        "Cultural",
        "Erotica",
        "Crime"]
    #while True :
    print(Fore.RED + r'''
        ;               ,           
            ,;                 '.         
            ;:                   :;        
        ::                     ::       
        ::                     ::       
        ':                     :        
            :.                    :        
        ;' ::                   ::  '     
        .'  ';                   ;'  '.    
    ::    :;                 ;:    ::   
    ;      :;.             ,;:     ::   
    :;      :;:           ,;"      ::   
    ::.      ':;  ..,.;  ;:'     ,.;:   
        "'"...   '::,::::: ;:   .;.;""'    
            '"""....;:::::;,;.;"""         
        .:::.....'"':::::::'",...;::::;.   
    ;:' '""'"";.,;:::::;.'""""""  ':;   
    ::'         ;::;:::;::..         :;  
    ::         ,;:::::::::::;:..       :: 
    ;'     ,;;:;::::::::::::::;";..    ':.
    ::     ;:"  ::::::"""'::::::  ":     ::
    :.    ::   ::::::;  :::::::   :     ; 
    ;    ::   :::::::  :::::::   :    ;  
    '   ::   ::::::....:::::'  ,:   '   
        '  ::    :::::::::::::"   ::       
        ::     ':::::::::"'    ::       
        ':       """""""'      ::       
            ::                   ;:        
            ':;                 ;:"        
             ';              ,;'          
                "'           "'            
                '   
    ''',)


    sys.stdout.write(Fore.GREEN + """
    welcome to 'Books to Scrape' scrper
    1- get Most rated books
    2- choose from category 
    3- exit
    :""")
    chose = input()
    os.system("cls")


    Nfile=input("Please enter the name of the output file: ")


    if Nfile in os.listdir(os.getcwd()):
        os.remove(f"output/{Nfile}")


    if chose == "1":

        books={"Books" :[]}
        booksLink=Scraper.getBooks("https://books.toscrape.com/index.html")
        for bookLink in booksLink:
            books["Books"].append(Scraper.getBookDetails(bookLink).toDict())
        Scraper.saveData(books,Nfile)   

    elif chose == "2":
        sys.stdout.write(Fore.GREEN + '''["Travel",
        "Mystery",
        "Historical Fiction",
        "Sequential Art",
        "Classics",
        "Philosophy",
        "Romance",
        "Women's Fiction",
        "Fiction",
        "Children's",
        "Religion",
        "Nonfiction",
        "Music",
        "Default",
        "Science Fiction",
        "Sports and Games",
        "Add a comment",
        "Fantasy",
        "New Adult",
        "Young Adult",
        "Science",
        "Poetry",
        "Paranormal",
        "Art",
        "Psychology",
        "Autobiography",
        "Parenting",
        "Adult Fiction",
        "Humor",
        "Horror",
        "History",
        "Food and Drink",
        "Christian Fiction",
        "Business",
        "Biography",
        "Thriller",
        "Contemporary",
        "Spirituality",
        "Academic",
        "Self Help",
        "Historical",
        "Christian",
        "Suspense",
        "Short Stories",
        "Novels",
        "Health",
        "Politics",
        "Cultural",
        "Erotica",
        "Crime"]''')
        INcategory = input("What category do you want?")
        
        if INcategory.capitalize() in category :
            url = fr"https://books.toscrape.com/catalogue/category/books/{INcategory.lower().replace(" ","-")}_{int(category.index(INcategory.capitalize())) + 2}/index.html"
            booksLink=Scraper.getBooks(url)
            books={"Books" :[]}
            for bookLink in booksLink:
                books["Books"].append(Scraper.getBookDetails(bookLink).toDict())
            Scraper.saveData(books,Nfile) 
        else:
            print("Invalid input, please enter one item from the list")
    elif chose == "3":
        print(Fore.GREEN + "bye 😊")
        exit()
    else:
        print("invalid input please enter valid input")
        #continue


if __name__ == "__main__" :
    main()
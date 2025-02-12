import sys
from colorama import Fore, Style

def main():
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
    2- choose from category ["Travel",
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
    3- exit
    :""")
    chose = input()


if __name__ == "__main__" :
    main()
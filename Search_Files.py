'''                                                   SEARCH_FILES                                              '''

'''SEARCH_FILES program searches the location of files, whose names are listed in a text file, from the directory.
    In the next step, SEARCH_FILES copy those listed files from the directory and paste them in desired location'''

'''Define 
    1. location of the text file containing names of the files to be searched, 
    2. location of the directory from which that list needs to be searched,
    3. location where searched files would be copied '''

#get the location of the txt file in which list if files to be searched has been stored
list_location =input("Location of the file containing names of files to be searched: ")

#get the location of directory in which list of files to be searched
directory_location = input("Location of the directory in which files need to be searched: ") 

#get location of the directory where searched files need to be pasted
des_dir = input("Location to paste copied files: ")

def main():


if __name__ == '__main__':
   main()



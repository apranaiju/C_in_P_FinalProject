'''                                                   SEARCH_FILES                                              '''

'''SEARCH_FILES program searches the location of files, whose names are listed in a text file, from the directory.
    In the next step, SEARCH_FILES copy those listed files from the directory and paste them in desired location'''

'''Define 
    1. location of the text file containing names of the files to be searched, 
    2. location of the directory from which that list needs to be searched,
    3. location where searched files would be copied '''

#get the location of the txt file in which list of files to be searched has been stored
list_location =input("Location of the file containing names of files to be searched: ")

#get the location of directory in which list of files to be searched
directory_location = input("Location of the directory in which files need to be searched: ") 

#get location of the directory where searched files need to be pasted
destination_dir = input("Location to paste copied files: ")

def main():

#Create list of the files' names from the text file.
def get_list(): 
   my_list = loadtxt(list_location, dtype = 'str')
   return my_list

#Create list of the files' names from the directory.
def search_directory(): 
   dir_list =[]
   for dirpath, dirs, files in os.walk(directory_location):
      for names in files:
         dir_list.append(names)
   return dir_list

#Compare the list of files' name from text file and the list of the files' name from the directory, in order to get list of files' name present in the directory.
def search(list, directory):
   matched_list = []
   for each_x in list:
      if each_x in directory:
         matched_list.append(each_x)
      else:
         pass
   #print(matched_list)
   return matched_list

#search the path of the matched_list files, copy them and paste them in the desired location.
def copy_files(match_list):
   for dirpath, dirs, files in os.walk(directory_location):
      for names in files:
         file_path = (os.path.join(dirpath, names))
         if names in match_list:
            try:
               copy2(file_path, destination_dir)
            except SameFileError:
               pass


if __name__ == '__main__':
   main()



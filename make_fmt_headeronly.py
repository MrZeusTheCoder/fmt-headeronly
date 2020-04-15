#One argument: the path to the (updated) git repo containing {fmt} 

import sys
import os
import re

header_guard_regex = re.compile("#define FMT_(?:.*)_H_")
make_header_only_string = "\n\n//EDIT:\n#ifndef FMT_HEADER_ONLY\n#define FMT_HEADER_ONLY\n#endif\n"

def file_with_ho_definition(input_fp):
    with open(input_fp, "r") as in_file:
        output = ""
        for line in in_file:
            if header_guard_regex.match(line):
                output += line
                output += make_header_only_string
            else:
                output += line
    return output

if __name__ == "__main__":
    start_dir = os.getcwd() + "/"

    if(len(sys.argv) < 2):
        print("This program requires a path of the folder containing {fmt}'s files.")
        exit()

    if(not os.path.exists(sys.argv[1])):
        print("That file path (\"%s\") doesn't exist." % sys.argv[1])
        exit()
    
    if(not os.path.isdir(sys.argv[1])):
        print("Feed me a file once, good riddance. Feed me a file twice, shame on you. Feed me a file three times--SEGFAULT @ 0x001023.")
        exit()
    
    if(not sys.argv[1].endswith("/")):
        sys.argv[1] += "/"
    
    print(">>>Remember to checkout to the proper branch/tag before running this script!<<<")
    
    os.chdir(sys.argv[1])

    if(os.path.exists(sys.argv[1] + "include/fmt/")):
        print("The include/fmt directory doesn't seem to exist... :/... exiting.")
        exit()
    
    os.chdir("include/fmt/")

    for x in ["format.h", "format-inl.h", "core.h"]:
        if(not os.path.exists(x) or not os.path.isfile(x)):
            print("File \"%s\" doesn't exist or isn't a file." % os.getcwd()+x)
            exit()
        else:
            try:
                os.mkdir(start_dir + "output/")
            except FileExistsError:
                pass
            with open(start_dir + "output/" + x, "w") as out_file:
                out_file.write(file_with_ho_definition(x))
            
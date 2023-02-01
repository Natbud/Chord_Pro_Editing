import os
import fileinput

directory_in_str = os.path.realpath(os.path.dirname(__file__))

directory = os.fsencode(directory_in_str)

updated_text = []
added_comment = []
new_filename = []
cleaned_file_list = []

# Function to split by paragraph (pulled from online)
def split_paragraph2(input_lines):
    paragraph = []  # store current paragraph as a list
    for line in input_lines:
        if line.strip():  # True if line is non-empty (apart from whitespace)
            paragraph.append(line)
        elif paragraph:  # If we see an empty line, return paragraph (if any)
            yield "".join(paragraph)
            paragraph = []
    if paragraph:  # After end of input, return final paragraph (if any)
        yield "".join(paragraph)


#Iterate through all the files:   
for file in os.listdir(directory):
    updated_text = []
    filename = str(os.fsdecode(file))
    if filename.endswith(".pro"): 
        #print(os.path.join(str(directory), "\n", str(filename)))
        print(filename)
         
        with open(filename) as f:
            file_list = f.readlines()

            
            #NOW MAIN CODE TO EDIT EACH FILE:
            #SOME PRE EDITING NEEDED TO CLEAN UP FILE FIRST:
            for line in file_list:
                if line[0] == "{":
                    newline = str("\n"+line+"\n\n")
                    cleaned_file_list.append(newline)
                else:
                    cleaned_file_list.append(line)
            
            
            x = 1            

            #Split into paragraphs calling function and add comments:
            for p, parag in enumerate(split_paragraph2(cleaned_file_list)):
                if parag[0][0]=="{":
                   updated_text.append(parag)
                else:
                    added_comment = f"\n{{comment: SECTION {x}}}\n"
                    updated_text.append(added_comment)
                    updated_text.append(parag)
                    x +=1
                    #print(updated_text)

            
            #Now export everything back out to new file:
            
            #Create the new file:
            a = "u_"
            new_filename = a+filename
            #print("new filename is: ", new_filename)

            n = open(new_filename,"w+")

            for line in updated_text:
                n.write(line)
                
                    


         



    else:
        continue
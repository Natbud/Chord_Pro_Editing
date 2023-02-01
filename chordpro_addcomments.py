import os
import fileinput

directory_in_str = os.path.realpath(os.path.dirname(__file__))

directory = os.fsencode(directory_in_str)

updated_text = []
added_comment = []
new_filename = []

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

            #Split into paragraphs calling function and add comments:
            for p, paragraph in enumerate(split_paragraph2(file_list)):
                if paragraph[0][0]=="{":
                   updated_text.append(paragraph)
                else:
                    added_comment = f"\n{{comment: SECTION {p}}}\n"
                    updated_text.append(added_comment)
                    updated_text.append(paragraph)
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
from pathlib import Path
import json

class WritingTools:

    def __init__(self):
        pass

    @staticmethod
    def abbreviate(file, overwrite = True, verbose = True):

        """Abbreviates ALL journal names from the specified file.
        Source for abbreviations: https://journal-abbreviations.library.ubc.ca/
        Credit to Kevin Lindstrom, Liaison Librarian at the University of British Columbia.
        """

        ABBREV_PATH = Path(__file__).parent / "abbreviations.json"

        with open(ABBREV_PATH, "r") as f:
            a = json.load(f)

        with open(file, 'r') as f:
            lines = []        
            
            for line in f:
    
                for key, val in a.items():
                    
                    if key in line:
                        if verbose: print(f"Replacing: {key} with {val}!")
                        line = line.replace(key, val)
        
                lines.append(line)

        if overwrite: ofile = file
        else: ofile = "abbreviated.txt"

        with open(ofile, 'w') as f:
            for line in lines:
                f.write(line)
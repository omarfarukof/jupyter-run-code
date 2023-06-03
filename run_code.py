# Magic commands to run C code
from IPython.core.magic import register_cell_magic
import tempfile
import os
import sys

# Temporary directory
tmpdir = ".tmp/"

# Class Code Start
class Code:

    def __init__(self, line, cell):
        self.line = line
        self.cell = cell
        self.name = ""
        self.location = ""
        self.language = ""
        self.extension = ""
        self.default_path = ""
        self.path = ""
        self.tmpcode = False

        # run code
        self.run()

    def get_code_info(self):
        if self.language.lower() == "c":
            self.extension = ".c"
            self.default_path = "C_codes/"
            self.add_extension()
            self.run_syntax = f"gcc {self.path} -o {self.path[:-len(self.extension)]} \
                  && {self.path[:-len(self.extension)]}"
        elif self.language.lower() == "python":
            pass
            self.extension = ".py"
            self.default_path = "Python_codes/"
            self.add_extension()
            self.run_syntax = f"python {self.path}"
        else:
            pass        

    def get_file_info(self):
        file = self.line.strip()
        file = file.split()
        self.language = file[0]
        self.get_code_info()

        if len(file) == 1:
            # self.language , = file
            self.location = tmpdir
            self.tmpcode = True
        else:
            # self.get_code_info()
            if len(file) == 2:
                self.location = file[1]
                self.name = self.location.split(self.get_devider())[-1]
                self.location = self.location[:-len(self.name)]
            elif len(file) == 3:
                self.location, self.name = file[1:3]
                # create code file in a specific location and run code
            else:
                if len(file) == 0:
                    raise Exception("No language specified")
                else:
                    raise Exception("Too many arguments")
        if self.location == "":
            self.location = self.default_path
        self.location = self.add_devider()
        self.path = self.location + self.name
        self.add_extension()

    def run(self):
        self.get_file_info()
        if self.tmpcode:
            self.create_tmp_file()
        else:
            self.create_file()      
        self.get_code_info()
        os.system(self.run_syntax)

    def create_file(self):
        os.makedirs(self.location, exist_ok=True)
        with open(self.path, "wb") as f:
            f.write(self.cell.encode())
            f.close()

    def create_tmp_file(self):
        self.get_code_info()
        os.makedirs(tmpdir, exist_ok=True)
        with tempfile.NamedTemporaryFile(suffix=self.extension, \
                                     delete=False, dir=tmpdir) as f:
            # write the contents of the cell to the file
            f.write(self.cell.encode())
            # close the file
            f.close()
            # run the tmp file
            self.path = f.name

    def add_extension(self):
        if self.path.endswith(self.extension):
            pass
        else:
            self.path = self.path + self.extension
        return self.path

    def add_devider(self):
        if self.location[-1] != self.get_devider():
            self.location = self.location + self.get_devider()
        return self.location
    
    def get_devider(self):
        if (sys.platform == 'linux') or ( sys.platform == 'darwin'):
            self.devider = "/"
        elif sys.platform == 'win32':
            self.devider = "\\"
        else:
            pass
        return self.devider
    
# Class Code End

@register_cell_magic
def run_code(line, cell):
    code = Code(line, cell)

        

from fpdf import FPDF
from fpdf.enums import XPos, YPos
import math
import numpy as np


class asian_comprehension_worksheet_generator:
    pdf = FPDF()

    # Basic settings
    pdf.add_font('fireflysung', '', 'fireflysung.ttf')
    pdf.set_font("fireflysung", size=28)
    size = 17
    num_x_cell = 16
    num_y_cell = 10
    file = "text"  # Seed filename

    def read_file(self):
        f = open(self.file, "r")
        return f.readlines()

    def split(self, word):
        # turn string into a list of character and strip off the new line character
        return list(u"{}".format(word.rstrip("\n")))

    def raw_text_to_list_of_vertical_column(self, word_array):
        # turn string into a list of character to be fit in vertical column
        my_list = []

        while word_array:
            sub_list = []
            for x in range(0, self.num_y_cell):
                if not word_array:
                    # fill up the rest of the cell with blank whenever a return character is detected
                    for y in range(x, self.num_y_cell):
                        sub_list.append('')
                    break
                c = word_array.pop(0)
                sub_list.append(c)
            my_list.append(sub_list)
        return my_list

    def text_to_single_list(self, raw_text):
        single_list = []
        for line in raw_text:
            single_list = single_list + self.raw_text_to_list_of_vertical_column(self.split(line))
        return single_list

    def add_empty_columns(self, my_list):
        new_list = []
        empty_column = [''] * self.num_y_cell
        while my_list:
            new_list.append(my_list.pop(0))
            new_list.append(empty_column)
        # check if content covers a whole page
        reminder = (len(new_list) % self.num_x_cell)
        if (reminder):
             # add extra empty columns to fill up last page
            for _ in range(0, self.num_x_cell - reminder):
                new_list.append(empty_column)
        
        return new_list

    def make_page(self, lines):
        self.pdf.add_page(orientation='L')
        for line in lines:
            for c in line:
                self.pdf.cell(self.size, self.size, txt=c, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
            self.pdf.ln()


def main():
    new_pdf = asian_comprehension_worksheet_generator()
    lines = new_pdf.read_file()
    lines_array = new_pdf.text_to_single_list(lines)
    padded_lines_array = new_pdf.add_empty_columns(lines_array)
    x = 0
    while x * new_pdf.num_x_cell < len(padded_lines_array):
        # rotate the array for printing out characters from right to left and vertically
        new_pdf.make_page((np.rot90(padded_lines_array[new_pdf.num_x_cell * x: new_pdf.num_x_cell * (x + 1)], 3)))
        x += 1
    new_pdf.pdf.output("worksheet.pdf")


if __name__ == "__main__":
    main()

#Road to Dublin

class Tokenizer:
    def __init__(self, input_file):
        self.file = open(input_file, 'r')
        self.cur_line = self.file.readline()
        self.eof  = False


    def next_word(self):
        """
        this function reads the next word represented in the line,
        and updates the current line accordingly. if end of line, returning
        None.
        assumption: next integer is separated by whitespace.
        :return: the next integer in the line.
        """
        self.cur_line = self.cur_line.lstrip()
        if not self.cur_line: #end of line
            self.next_line()
            return None
        cur_split = self.cur_line.split(maxsplit=1)
        if (len(cur_split) == 1): #end of line
            self.cur_line = ""
        else: #merging second cell to string
            self.cur_line = cur_split[1]

        #returning current int:
        return cur_split[0]




    def next_int(self):
        """

        :return: the next int represented in the line.
        """
        return int(self.next_word())

    def next_char(self):
        """

        :return: the next char in the line we're reading, None if end of line.
        """
        #searching for the first char which isn't a whitespace:

        self.cur_line = self.cur_line.lstrip()
        if not self.cur_line: #end of line
            self.next_line()
            return None
        else: #reading char
            c = self.cur_line[0]
            if (len(self.cur_line) > 1):
                self.cur_line = self.cur_line[1:]
            else:
                self.cur_line = ""
            return c




    def next_line(self):
        """
        reads next line into cur_line and updates other variables.
        :return:
        """
        line  = self.cur_line
        self.cur_line = self.file.readline()
        if not self.cur_line:
            self.eof = True
        return line




    def is_eof(self):
        """

        :return: whether we've reached the end of the file
        """
        return self.eof



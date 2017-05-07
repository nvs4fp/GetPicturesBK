# To study how to operate file
import re


class FileOperation(object):
    def __init__(self, fileName):
        self.fileName = fileName

    def add_line_index(self):
        f = open(self.fileName, 'r')
        if self.__check_index_existing(f.readline()):
            f.close()
            return
        else:
            f.close()

        f = open(self.fileName, 'r')
        m_new_lines = []
        m_line_num = 1
        for line in f.readlines():
            if line:
                m_new_lines.append("%d." % m_line_num + line)
                m_line_num += 1
        f.close()

        f = open(self.fileName, 'w')
        for line in m_new_lines:
            f.write(line)
        f.close()

    def __check_index_existing(self, lines):
        if len(lines) < 1:
            return False
        if re.findall('\d+\.', lines):
            return True


def file_read_write():
    file_op = FileOperation("finput.txt")
    file_op.add_line_index()


if __name__ == "__main__":
    file_read_write()

from HTMLParser import HTMLParser
import os
def strip_tags(file_path):
    input_file = open(file_path)
    raw_data = input_file.read()
    plain_text = []
    parser = HTMLParser()
    parser.handle_data = plain_text.append
    parser.feed(raw_data)
    parser.close()
    return ''.join(plain_text)

def write_file(filename, content, destination):
    folder = destination + '/' + os.path.dirname(filename)
    if not os.path.exists(folder):
        os.makedirs(folder)
    print filename
    file = open(destination + '/' + filename, "w")
    file.write(content)
    file.close()

if __name__=="__main__":
    print strip_tags("example.html")
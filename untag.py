def strip_tags(html,origin_directory):
    from HTMLParser import HTMLParser
    html = open(origin_directory+'/'+html)
    html=html.read()
    html = html.strip()
    html = html.strip("\n")
    result = []
    parser = HTMLParser()
    parser.handle_data = result.append
    parser.feed(html)
    parser.close()
    return ''.join(result)

def generate_untag_file(html,untag_text,origin_directory,destiny_directory):
	html='untag_'+html
	file = open(destiny_directory+'/'+html, "w")
	file.write(untag_text)
	file.close()
if __name__=="__main__":
    print strip_tags("example.html")
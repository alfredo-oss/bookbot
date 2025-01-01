def wordCount(s: str) -> int:
    s_list = s.split()  
    return len(s_list)
path_to_file = "books/frankestein.txt"

with open(path_to_file) as f:
    file_contents = f.read()

print(wordCount(file_contents))
def wordCount(s: str) -> int:
    s_list = s.split()  
    return len(s_list), s_list

def characterCount(s_list: list[str]) -> int:
    s = "".join(s_list)
    count = {}
    for c in s:
        count[c.lower()] = 1 + count.get(c.lower(), 0)
    for key, value in count.items():
        print(f"Character: {key} | {value}")    
    

path_to_file = "books/frankestein.txt"

with open(path_to_file) as f:
    file_contents = f.read()
wc, s_list = wordCount(file_contents)
characterCount(s_list)

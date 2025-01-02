def wordCount(s: str) -> int:
    s_list = s.split()  
    return len(s_list), s_list

def sortDictDescending(numDict: dict) -> dict:
    return dict(sorted(numDict.items(), key=lambda item: item[1], reverse=True))

def characterCount(s_list: list[str]) -> int:
    s = "".join(s_list)
    count = {}
    for c in s:
        count[c.lower()] = 1 + count.get(c.lower(), 0)
    revCount = sortDictDescending(count)
    for key, value in revCount.items():
        print(f"Character: '{key}' appears {value} times ")    
    

path_to_file = "books/frankestein.txt"

with open(path_to_file) as f:
    file_contents = f.read()
wc, s_list = wordCount(file_contents)

print("\n")
print(f"---------------------- Begin: {path_to_file} Report -----------------------")
print(f"{wc} words found in the document\n\n")
characterCount(s_list)
print("----------------------- End Report ------------------------------------------")
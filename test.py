import re

text = "Please contact us at support@example.com or sales@example.org for further information."

match_result = re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
if match_result:
    print(f"Match found: {match_result.group()} at index {match_result.span()}")
else:
    print("No match found at the beginning of the string.")

search_result = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
if search_result:
    print(f"Search found: {search_result.group()} at index {search_result.span()}")
else:
    print("No match found in the string.")

findall_result = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print(f"Findall found: {findall_result}")

# test git merge
# test git merge again
# test git merge again and again
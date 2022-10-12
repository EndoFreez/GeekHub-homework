# 2. Write a script to remove empty elements from a list.Test list: 
# [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

a = [(), ('hey'), ('',), ('ma', 'ke', 'my'),[''], {}, ['d', 'a', 'y'], '', []]
print(list(filter(None, a)))
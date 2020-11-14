import re
#inut text file to look for New Revision: 39772
finder = findall("^New .*: [0-9]+", Sentence)
if len(finder) > 0:
    print(finder)

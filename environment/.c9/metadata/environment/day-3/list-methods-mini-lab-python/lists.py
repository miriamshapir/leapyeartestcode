{"changed":true,"filter":false,"title":"lists.py","tooltip":"/day-3/list-methods-mini-lab-python/lists.py","value":"# As you may know, an anagram is a new word created by reorganizing all the letters in a word.\n# This list of anagrams are all based on the word \"Stop\"\nanagrams = [\"plots\", \"post\", \"stop\", \"puts\", \"tops\"]\n\n# Run this program after you try each step and see if it worked.\n# At the very bottom of this file is a line of code that prints out the list after your code is run.\n# You're welcome to print additional debugging statements if you need.\n\n# 1. Print out the third word in the list using bracket notation.\nprint (anagrams[2])\n\n\n\n\n# 2. The word \"opts\" is also an anagram of the word \"stop\". Find a way to add \"opts\" to the end of the list.\nanagrams.append(\"opt\")\n\n\n\n\n\n# 3. The word \"puts\", on the other hand, is not an anagram of the word \"stop\". Find a way to replace it with the word \"pots\".\n\nprint(anagrams[3])\nanagrams[3]=\"pots\"\nprint(anagrams[3])\n\n# 4. Use the documentation to figure out what the method \".pop()\" does.\n#   Now use it to remove the word \"plots\" (which isn't a correct anagram of \"stop\") from our list.\nanagrams.pop(0)\n\n\n\n# 5. Put the final list of anagrams in alphabetical order, and SAVE it.\n# (If you encounter an error here, it's probably because Python is sorting it temporarily, but then immediately restoring it to the original order.)\n\nanagrams.sort()\n\n\n\n\n\n# This code prints the list after you've manipulated it above.\n#print(anagrams)\n\n# LEVEL 2: At this point, the tasks will get more challenging, because you'll work with datasets too large to handle by just looking at it and reading it.\n# The lists used in the second half of this lab will be stored in a neighboring file called \"other_lists.py\".\n# If you'd like to look at that file, you certainly may, but do your work here.\n# This line of code connects the data.\nimport other_lists\n\n# Pro-tip: to make this easier, comment out the line \"print(anagrams)\" above so that you aren't printing extra information.\n#\n# 6. The first list is called \"fortunes\" and contains fortune-cookie style fortunes. Print out a random fortune from the list.\n#     Remeber to access the list with \"other_lists.fortunes\" because is is in a different file.\nother_lists.fortunes\nimport random     # You're going to need a method from the random library.\nprint(random.choice(other_lists.fortunes))\n \n\n# 7. This list is huge, so it'd be helpful to know how many fortunes are listed. Find a way to print out the number of fortunes in the list.\n\nprint(len(other_lists.fortunes))\n\n\n\n# 8. Challenge: Out of all the fortunes that are there, it'd mess up the program if some were listed twice, but with a list that big, it could happen.\n# Find a way to check and see whether any of the fortunes are duplicates. If so, find a way to delete those duplicates.\n\n\n\n\n\n\n\n\n\n\n\n","undoManager":{"mark":-2,"position":2,"stack":[[{"start":{"row":67,"column":79},"end":{"row":67,"column":80},"action":"insert","lines":["z"],"id":2}],[{"start":{"row":67,"column":79},"end":{"row":67,"column":80},"action":"remove","lines":["z"],"id":3}],[{"start":{"row":66,"column":33},"end":{"row":66,"column":34},"action":"insert","lines":["r"],"id":4}]]},"ace":{"folds":[],"scrolltop":882,"scrollleft":0,"selection":{"start":{"row":68,"column":0},"end":{"row":68,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":0},"timestamp":1563392344310}
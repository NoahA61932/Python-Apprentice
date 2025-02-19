"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = [words]

# Create a story using the words in the list

# Display the story to the user
print('[1:3]', words[1:3])      # print the second to third items, but not including the third item
print('[:2]', words[:2])        # print the first two items. Nothing before the ':' means 'from the start'
print('[2:]', words[2:]) 
import xml.etree.ElementTree as ET

# Read the XML data (from the string or file)
tree = ET.parse('movie.xml')  # Ensure your XML file is in the same directory
root = tree.getroot()

# 1. Use iter() function to list all child tags of the <movie> element and number the movies
print("Listing child elements of each movie:")

movies_count = 1  # Start numbering movies
for movie in root.iter('movie'):
    print(f"\nMovie {movies_count}:")
    for child in movie.iter():  # Use iter() to get all child elements of <movie>
        print(f"  - {child.tag}")
    movies_count += 1

# 2. Use itertext() to print the movie descriptions
print("\nMovie descriptions:")
for movie in root.iter('movie'):
    description = movie.find('description')
    if description is not None:  # Ensure description exists before printing
        print(f"- {description.text.strip()}")

# 3. Count the number of favorite and non-favorite movies
favorite_count = 0
non_favorite_count = 0

# Loop through all movies and count favorites and non-favorites
for movie in root.iter('movie'):
    # Retrieve the value of the 'favorite' attribute
    favorite = movie.attrib.get('favorite', '').strip().lower()
    
    # Check if favorite is 'true' or 'false', and count accordingly
    if favorite == 'true':
        favorite_count += 1
    elif favorite == 'false':
        non_favorite_count += 1
    else:
        # If the value is not 'true' or 'false' (or missing), treat it as undefined
        print(f"Movie with title '{movie.attrib['title']}' has an undefined favorite value: '{favorite}'")

# Print the results
print("\nNumber of favorite movies:", favorite_count)
print("Number of non-favorite movies:", non_favorite_count)

# Generate a string that serves a list containing all entries in a file
def from_list(file_contents):
    # Establishing a map of entries (entry:note)
    entry_map = {}
    for line in file_contents.split('\n'):
        if line.startswith("#"):
            continue
        split_entry = line.split(":")
        entry_map.update({split_entry[0]: split_entry[1]})

    # First entries = no note
    # Second entries = have note
    first_list = []
    second_list = []

    for cont in entry_map.keys():
        if entry_map.get(cont) == "":
            first_list.append(cont)
        else:
            second_list.append(cont)

    # Sorting entries alphabetically
    first_list.sort()
    second_list.sort()

    # First appending entries with no notes and those with notes later
    out = ""

    for first_entry in first_list:
        out += f"- {first_entry}\n"

    for second_entry in second_list:
        out += f"- {second_entry}\n"
        out += f"  - {entry_map.get(second_entry)}\n"

    # Removing the last new line
    out = out[:len(out)-1]

    return out

# Reading files required to generate the README
# These can be modified by a common contributor
template = open("data/template.md", "r").read()
contributors_list = open("data/contributors", "r").read()
sources_list = open("data/sources", "r").read()
links_list = open("data/links", "r").read()

# This will be written to README.md
output = template

# Generating contributors
contributors_out = from_list(contributors_list)

# Writing contributors to output
output = output.replace("contributors-here", contributors_out)

# Generating sources
sources_out = from_list(sources_list)

# Writing sources to output
output = output.replace("sources-here", sources_out)

# String that will be directly written to outpt
links_out = ""

for line in links_list.split('\n'):
    if line.startswith("#"):
        continue
    split_link = line.split("<---->")
    links_out += f"- [{split_link[0]}]({split_link[1]})\n"

# Removing the last new line
links_out = links_out[:len(links_out)-1]

# Writing links to output
output = output.replace("links-here", links_out)

# Writing the contents of output to README.md
f = open("README.md", "w")
f.write(output)
f.close()

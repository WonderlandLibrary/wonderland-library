template = open("README.template", "r").read()
contributors_list = open("contributors.list", "r").read();
links_list = open("links.list", "r").read();

output = template

contributors = {}
for line in contributors_list.split('\n'):
    if line.startswith("#"):
        continue
    split_contributor = line.split(":")
    contributors.update({split_contributor[0]: split_contributor[1]})
                                
        
first_contributors = []
second_contributors = []

for cont in contributors.keys():
    if contributors.get(cont) == "":
        first_contributors.append(cont)
    else:
        second_contributors.append(cont)

first_contributors.sort()
second_contributors.sort()

contributors_out = ""

for cont in first_contributors:
    contributors_out += f"- {cont}\n"

for cont in second_contributors:
    contributors_out += f"- {cont}\n"
    contributors_out += f"  - {contributors.get(cont)}\n"

output = output.replace("contributors-here", contributors_out)

links_out = ""

for line in links_list.split('\n'):
    if line.startswith("#"):
        continue
    split_link = line.split("<---->")
    links_out += f"- [{split_link[0]}]({split_link[1]})\n"

output = output.replace("links-here", links_out)

f = open("README.md", "w")
f.write(output)
f.close()

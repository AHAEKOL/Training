import xml.etree.ElementTree as ET
tree = ET.parse('bookshop.xml')
root = tree.getroot()

print(root.tag)

info = root.findall('info')[0]
print('Name:', info.attrib['name'])
print('State:', info.findall('state')[0].text)
print('City:', info.findall('city')[0].text)
print('Address:', info.findall('address')[0].text)


print('Book names:')
for child in root.findall('books')[0]:
    print(child.attrib['name'])

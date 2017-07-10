import xml.etree.ElementTree as ET
tree = ET.parse('usStates.xml')
root = tree.getroot()          

for state in root.findall('{http://www.w3.org/2000/svg}path'):
	print(state.attrib['id'])
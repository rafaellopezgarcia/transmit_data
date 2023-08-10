# The following scripts adds a unique id to requirements. 
# It uses hexadecimal numbers to encode the unique id.
# A maximum of FFFF (65,535) requirelments per section can be defined.
# A maximum of FFF (4095) sections can be defined.

import os
import pickle
import random
dir_path = os.path.dirname(os.path.realpath(__file__))
class CreateID:
  def __init__(self):  
        self.stored_file = dir_path + "/../.data/" + "stores.pckl"
        try:
          self.f,self.s = pickle.load(open(self.stored_file, 'rb'))
          self.last_section_id = self.f
          self.last_requirement_id = self.s
        except:
          self.last_section_id = 0
          self.last_requirement_id = 0
        
  def get_section_id(self):
    
    section_id = self.last_section_id + 1

    section_id = chr(random.randint(65, 90)) + "{:03x}".format(self.last_section_id)
    self.last_section_id = self.last_section_id + 1
    return section_id

  def get_new_id(self, section_id):
    requirement_id = "{:04x}".format(self.last_requirement_id)
    unique_id = section_id + ":" + requirement_id
    self.last_requirement_id = self.last_requirement_id + 1
    return unique_id
  
  def __del__(self):
    try:
      pickle.dump([self.last_section_id,self.last_requirement_id], open(self.stored_file, "wb"))
    except:
      print("error saving file")
  

def add_requirements_ids():
  create_id = CreateID()
  f = open("./README.md", "r")
  read_requirement = False
  section_id, content, key ="", "", "## Requirements"
  for x in f:
    if read_requirement:
      if len(x) > 2 and x[:3] == "###":
        section_id = create_id.get_section_id()
      if len(x) > 3 and x[:1] == "-" and x[2] != '[':
        requirement_id = create_id.get_new_id(section_id)
        x = f"- [{requirement_id}] " +x[2:]

    elif len(x) >= len(key) and x[:len(key)] == key:
      read_requirement = True
    content += x

  f = open("./README.md", "w")
  f.write(content)
  f.close()
  print(content)

add_requirements_ids()

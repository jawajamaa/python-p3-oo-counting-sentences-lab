#!/usr/bin/env python3
# value = "Is this a value?"

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")
  # above line is more pythonic and can replace the 4 below
  # if self.value.endswith(".") is True: 
    #   return True
    # else:
    #   return False
      
  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

# better solution
  # def count_sentences(self):
  #   value = self.value
  #   for punc in ['!','?']:
  #       value = value.replace(punc, '.')
    
  #   sentences = [s for s in value.split('.') if s]
    
  #   return len(sentences)

# my solution with help, but much more verbose
  def count_sentences(self):
    endings = ("!","?")
    # return len(self.value.split()) only works for one word sentences!
    # next three lines are not needed...
    # if self.value == "":
    #   return 0
    # else:
    for end in endings:
      self.value = self.value.replace(end,".")
    change_ending = self.value.split(".")
    print(change_ending)
    for change in change_ending:
      print(change)
      if change == "":
        change_ending.remove(change)
        print(change_ending)
    # breakpoint()   
    for change in change_ending:
      if change_ending[-1] == "":
        change_ending.pop() 
    return len(change_ending)
    # return len(self.value.split("."))

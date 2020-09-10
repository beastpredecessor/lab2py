#Author: xuanyi shen xjs5065@psu.edu
# Collaborator: Hanbit Kim hqk5400@psu.edu
# Collaborator: Seungki An sva5802@psu.edu
# Collaborator: Jacob Hallowell jph5997@psu.edu
# Section: 4
# Breakout: 5


def getLetterGrade(grade):
  if grade >= 93.0:
    return("A")
  elif grade >= 90.0:
    return("A-")
  elif grade >= 87.0:
    return("B+")
  elif grade >= 83.0:
    return("B")
  elif grade >= 80.0:
    return("B-")
  elif grade >= 77.0:
    return("C+")
  elif grade >= 70.0:
    return("C")
  elif grade >= 60.0:
    return("D")
  elif grade < 60.0:
    return("F")

def run():
  grade2 = getLetterGrade(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {grade2}.")

if __name__ == "__main__":
  run()
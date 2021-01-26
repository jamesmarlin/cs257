import csv


def athlete():
  athletes_dict = {}
  with open('athlete_events.csv', newline='') as csv_file:
      athlete_reader = csv.reader(csv_file, delimiter =',', quotechar= '|')
      next(athlete_reader)
      for row in athlete_reader:
          ID = int(row[0])
          names = row[1]
          sex = row[2]
          weight = int(row[4])
          if ID not in athletes_dict:
            #athletes_dict[ID] = len(athletes_dict) + 1
            athletes_dict[ID] = [names, sex, weight]
      field_names = ['ID', 'Name', 'Sex', 'Weight']
      writer=csv.writer(open('athletes.csv','w', fieldnames=fieldname))
      writer.writeheader()
      for key in athletes_dict:
        row = [key, athletes_dict[key][0], athletes_dict[key][1], athletes_dict[key][2]]
        writer.writerow(row)

      #writer=csv.writer(open('athletes.csv','w'))
      #for  in athlete_reader:
         #row = [names, sex, weight]
        #writer.writerow(row)
  return

def age:
  age_dict = {}
  with open('athlete_events.csv', newline='') as csv_file:
    age_reader = csv.reader(csv_file, delimiter = '', quotechar= ' ')
    for row in age_reader:
      age = row[3]
      height = row[4]
      if age not in age_dict:
        age_dict[age] = [height]
        
      else:
        
return

def main():
  athlete()
  
if __name__ == "__main__":
  main()
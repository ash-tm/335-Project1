def combineDailyActive(p1_DailyAct, p2_DailyAct, dailyActive):
  """ Combines daily activity of both persons. """
  dailyActive.append(max(p1_DailyAct[0], p2_DailyAct[0]))
  dailyActive.append(min(p1_DailyAct[1], p2_DailyAct[1]))

def sortSchedules(p1_Schedule, p2_Schedule):
  """ Sorts the schedules of both persons and and merges them into one Python list. """
  sorted = []
  i, j = 0, 0
  while i < len(p1_Schedule) and j < len(p2_Schedule):
      if p1_Schedule[i] < p2_Schedule[j]:
          sorted.append(p1_Schedule[i])
          i += 1
      else:
          sorted.append(p2_Schedule[j])
          j += 1
  while i < len(p1_Schedule):
      sorted.append(p1_Schedule[i])
      i += 1
  while j < len(p2_Schedule):
      sorted.append(p2_Schedule[j])
      j += 1
  return sorted

def findOpenTimes(combinedSched, dailyActive, duration_of_meeting):
  """ A function that checks for any available schedules 
  between both persons and the combined daily activity."""
  available_times = []
  end_of_last_meeting = dailyActive[0]
  # Compares last meeting time with potential meeting time, then appends to available_times list
  for meeting in combinedSched:
      if meeting[0] > end_of_last_meeting:
          available_times.append([end_of_last_meeting, meeting[0]])
      end_of_last_meeting = max(end_of_last_meeting, meeting[1])
  if dailyActive[1] > end_of_last_meeting:
      available_times.append([end_of_last_meeting, dailyActive[1]])
  # Converts the times into minutes and finds the difference between them
  return [time for time in available_times if int(time[1].split(':')[0])*60 + int(time[1].split(':')[1]) - (int(time[0].split(':')[0])*60 + int(time[0].split(':')[1])) >= duration_of_meeting]

def main():
    """ Main function for Matching Group Schedules """
    # Read input from file
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    # Iterators
    i = 0
    testCaseNum = 1

    # While loop to go to next line for each variable
    while i < len(lines):
        if lines[i] == "\n":
            i += 1

        p1_Schedule = eval(lines[i].strip())
        p1_DailyAct = eval(lines[i+1].strip())
        p2_Schedule = eval(lines[i+2].strip())
        p2_DailyAct = eval(lines[i+3].strip())
        duration_of_meeting = int(lines[i+4].strip())
        i += 5

        dailyActive = []
        available_times = []

        combineDailyActive(p1_DailyAct, p2_DailyAct, dailyActive)
        combinedSched = sortSchedules(p1_Schedule, p2_Schedule)
        available_times = findOpenTimes(combinedSched, dailyActive, duration_of_meeting)

        # Append to output.txt
        with open('output.txt', 'a') as f:
          f.write("Case #{}:".format(testCaseNum))
          for time in available_times:
            f.write(str(time) + " ")
          f.write("\n")

        testCaseNum += 1
        
        # Reset lists
        dailyActive.clear()
        combinedSched.clear()
        available_times.clear()

if __name__ == "__main__":
  """ Runs the main function """
  main()
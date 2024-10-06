def main():
  task = input("Enter your task: ")
  priority = input("Priority (high/medium/low): ").lower()
  time_bound = input("Is it time-bound? (yes/no): ").lower()

  priority_message = match priority:
      case "high":
          return "**HIGH PRIORITY**"
      case "medium":
          return "Medium priority"
      case "low":
          return "Low priority"
      case _:
          return "Invalid priority. Please enter high, medium, or low."


  if time_bound == "yes":
    reminder_message = f"{priority_message}: '{task}' requires immediate attention today!"
  else:
    reminder_message = f"{priority_message}: '{task}'. Consider completing it when you have free time."

 
  print(reminder_message)

if __name__ == "__main__":
  main()
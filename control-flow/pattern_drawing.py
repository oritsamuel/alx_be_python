def main():
  while True:
    try:
      size = int(input("Enter the size of the pattern: "))
      if size <= 0:
        print("Please enter a positive integer.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")
  for i in range(size):
    for j in range(size):
      print("*", end="")
    print() 

if __name__ == "__main__":
  main()
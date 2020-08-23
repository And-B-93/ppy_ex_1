from Accounting.Application.salary import calculated_salary

def main():
  yes = input('Посчитать заработную плату? ')
  print(yes)
  if yes == 'да':
    return(calculated_salary())
  else:
    return
if __name__ == '__main__':
  main()

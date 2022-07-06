def arithmetic_arranger(problems, answer = False):

  line1 = []
  line2 = []
  line3 = []
  line4 = []
  operators = ['+', '-']

  if len(problems) > 5:
      return 'Error: Too many problems.'

  for i in problems:
      values = i.split(' ')
        
      if values[1] not in operators:
          return "Error: Operator must be '+' or '-'."

      spaces = max(len(x) for x in values)

      if len(values[0]) > 4 or len(values[2]) > 4:
          return 'Error: Numbers cannot be more than four digits.'
        
      try:
          result = str(eval(i))
      except:
          return 'Error: Numbers must only contain digits.'

      line1.append(values[0].rjust(spaces+2) + ' '*4)
      line2.append(values[1] + ' ' + values[2].rjust(spaces) + ' '*4)
      line3.append('-'*(spaces+2) + ' '*4)
      line4.append(result.rjust(spaces + 2) + ' '*4)

  line1 = ''.join(str(x) for x in line1)
  line1 = line1.rstrip()
  line2 = ''.join(str(x) for x in line2)
  line2 = line2.rstrip()
  line3 = ''.join(str(x) for x in line3)
  line3 = line3.strip()
  line4 = ''.join(str(x) for x in line4)
  line4 = line4.rstrip()
    
  if answer == True:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
  else:
      arranged_problems = line1 + '\n' + line2 + '\n' + line3

  return arranged_problems
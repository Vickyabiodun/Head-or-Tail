<!DOCTYPE html>
<html>
  
  <body>
    <h1>Random Head or Tail Generator</h1>
    <p>This script generates a random head or tail using the Python <code>random</code> module.</p>
    <h2>Usage</h2>
    <pre>
import random

random_number = random.random()
if random_number <= 0.5:
    print(random_number)
    print('you chose head')
else:
    print(random_number)
    print('you picked tail')
    </pre>
    <p>The script first imports the <code>random</code> module. It then generates a random number between 0 and 1 using the <code>random()</code> function. If the number is less than or equal to 0.5, it prints 'you chose head', otherwise it prints 'you picked tail'.</p>
  </body>
</html>

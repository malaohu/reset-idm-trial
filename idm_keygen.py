import random

def generateSerial():
  Charset =  bytearray.fromhex("32594f5042334151435655584d4e52533937574530495a44344b4c4647484a3831363554").decode()
  Result = ""
  Value = 0
  L = 0
  while(True):
    K = 0;
    S = ""
    for i in range(0,5):
      J = random.randint(0, len(Charset)-1)
      S+=Charset[J]
      K += J + 36 * K
    if(L==1):
      Value = 23
    elif(L==2):
      Value = 17
    elif(L==3):
      Value = 53
    else:
      Value = 43
    if(K%Value==0):
      L+=1
      Result+=S
      if(L<4):
        Result+='-'
      else:
        break
  return Result

splash = """
+----------------------------------+
| Internet Download Manager v6.x.x |
+----------------------------------+

IMPORTANT: Generated keys will not work unless you block IDM online license check with a crack/patch.
"""
print(splash)
count = input("Enter how many serials wanna generate: ")
if(count==""):
  print("-> Input can't be empty!")
elif(not count.isdigit()):
  print("-> Enter only numbers.")
elif(int(count)<=0):
  print("-> Enter a number more than zero.")
else:
   for lmt in range(0,int(count)):
    print(generateSerial())

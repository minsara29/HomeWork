def isit_order(n):
  l = str(n)
  return all(l[i] <= l[i+1] for i in range(len(l)-1))


n = int(input("Print the Number:"))
c = 0 
while True:
  shiny = isit_order(n)
  if shiny == True:
    print(f" yes I am Order {n}"  )
    c += 1 
    if c == 100:
      break
  n += 1
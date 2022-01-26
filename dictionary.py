def most_frequent():
  x = input("enter a string")
  dict = {}
  for i in set(x):
    dict[i] = x.count(i)
  for j in sorted(dict,key=dict.get,reverse=True):
        print(j + "=", dict[j])
most_frequent()    

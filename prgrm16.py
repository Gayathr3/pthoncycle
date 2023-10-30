fruits = {'Apple': 2, 'Orange': 14, 'strawberry': 31, 'Watermelon': 61, 'pomergrante': 10}
l=list(fruits.items())
l.sort()
print('ascending order is:',l)
l=list(fruits.items())
l.sort(reverse=True)
print('decending orderis:',l)


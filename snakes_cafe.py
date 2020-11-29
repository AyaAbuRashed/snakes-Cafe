print("**   Welcome to the snakes Cafe!    **") 
print('**   please see our menu below      **')
print('**')
print('** To quit at any time ,type "quit" **')
print('****************************************')

list1=['Appetizers','-----','wings','cookies','spring rolls','   ']
list2=['Entrees','-----','salmon','steak','meat tornado','a literal garden','  ']
list3=['Desserts','-----','ice creem','cake','pie','   ']
list4=['Drinks','-----','Tea','Coffee','unicorn','   ']

def menu():
 for x in list1:
     print(x)
 for y in list2:
     print(y)
 for c in list3:
     print(c)
 for n in list4:
     print(n)

menu()  
def chooseItem():
    count=0
    print('***********************************')
    print('** What would you like to order? **')
    print('***********************************')
    i=0
    while i < 10 :
     item=input()
     count += 1 
     if item=='quit' :
         break
     print(count, 'order of ' + item +' have been added to your meal ')


chooseItem()
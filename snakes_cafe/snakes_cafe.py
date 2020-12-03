print("**   Welcome to the snakes Cafe!    **") 
print('**   please see our menu below      **')
print('**')
print('** To quit at any time ,type "quit" **')
print('****************************************')

list1=['Appetizers','-----','wings','cookies','spring rolls','   ']
list2=['Entrees','-----','salmon','steak','meat tornado','a literal garden','  ']
list3=['Desserts','-----','ice creem','cake','pie','   ']
list4=['Drinks','-----','tea','coffee','unicorn','   ']

"""
function to print the menu 
"""
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

"""
function that allows the user to pick up an order and return back what he choose and be able to quit 
"""
def chooseItem():
    lists=['salmon','steak','meat tornado','a literal garden','wings','cookies','spring rolls','ice creem','cake','pie','tea','coffee','unicorn']
    print('***********************************')
    print('** What would you like to order? **')
    print('***********************************')
    i=0
    itemList=[]
    while i < 10 :
     item=input('>')
     if item not in lists :
         print("Opps Your order not found !, Enter a valid order")
     else :    
         itemList.append(item)
     if item=='quit' :
         break
     print('** ',itemList.count(item), ' order of ' + item +' have been added to your meal **')


chooseItem()
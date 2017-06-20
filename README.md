#1 This is personal solution for coding challenge from Sortable



#2 Personal Analysis:

Purpose: Match each listing to the correct product
Constraints: Perfer missed matches over incorrect match(false positive)

#2 How to do?
1. Identification: according to the given example, I think the method the example used is by checking whether the prefix of the product match the listing (this should be one possible optional solution)

Programming: by using the String.Beginwith kind of thing

2. To avoid the false positive as much as possible, we can also check the match of manufacturer to avoid same name of products actually not from the same manafacturer


#2 Expected Time Complexity of the program and possible Optimization:
the number of listing m=200000, the number of products n=800
 



#1 This is personal solution for coding challenge from Sortable https://sortable.com/challenge/



#2 Personal Analysis:

Purpose: Match each listing to the correct product
Constraints: 
	1. A single listing to a product 
	2. Perfer missed matches over incorrect match(false positive)

#2 How to do?
1. Identification: according to the given example, I think the method the example used is by checking whether the prefix of the product match the listing title (one possible solution)

2. To avoid the false positive as much as possible, we can also check the match of manufacturer to avoid the situation when some products actually not from the same manafacturer but with the same prefix.


#2 Expected Time Complexity of the program and possible Optimization:
the number of listing m=200000, the number of products n=700
 	20000*700

A possbile Optimization is we first group the listing by the  manaufacturer and then try to match with the product under the same manafaturer, which may decrease the times of searching




### This is personal solution for coding challenge from Sortable (https://sortable.com/challenge/)


### Personal Analysis:
- Purpose: Match each listing to the correct product
- Constraints: 
	- A single listing to a product 
	- Perfer missed matches over incorrect match(false positive)

### How to do?
- Identification: according to the given example, I think the method the example used is by checking whether the prefix of the product match the listing title (one possible solution, but i just found the linking characters in the product_name like '-' and '_' should be processed into ' ' to match that in listings)
- To avoid the false positive as much as possible, we can also check the match correctness of manufacturer.

### Possible optimization for program?
- A possbile Optimization is that we can first group the listings by the manaufacturer and then try to match with the product under the same manafaturer, which may decrease the times of searching. But this seems impossible when the listings data too big, because we need to read and process by line
- Another optimization might happen when comparing the prefix of strings where we can use the data structure like Trie Tree (make the prefix comparsion very efficient), but this demands for large space if the length of string(product_name) can be very long.

### Run
git clone this repository and run main.py in ./solution/main.py with python




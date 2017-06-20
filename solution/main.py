#solution by python
import json


def convert(c):
	if(c=='-' or c=='_'):
		return ' '
	return c

file= '../input_data/products.txt'
fp=open(file,'r')

#product_list is the list with product name processed
product_list=[];
#product_ori_list with the name not processed
product_ori_list=[];

while 1:
	line = fp.readline()
	if not line:
		break
	data=json.loads(line)
	product_name=data['product_name'].strip()
	product_manu=data['manufacturer'].strip()

	#add to ori 
	product_ori_list.append(product_name)
	#process the linking characters like '-' and '_'
	product_name=''.join(map(convert,product_name))
	#print(product_name)
	product_list.append({'name':product_name,'manu':product_manu})

fp.close()

#get the length of products we have
product_len=len(product_list)
#print(product_list);


#processing
res_dict={};
file= '../input_data/listings.txt'
fp=open(file,'r')
while 1:
	#data to big read by line
	line = fp.readline()
	if not line:
		break
	data=json.loads(line)
	title=data['title'].strip();
	manu=data['manufacturer'].strip();
	for i in range(0,product_len):
		product_tempName=product_list[i]['name']
		product_tempManu=product_list[i]['manu']

		if( title.startswith(product_tempName)):
			#this listing belongs to product[i]
			print('title: '+title+'   is:   ' +product_tempName)
			if product_tempName not in res_dict:
				res_dict[product_tempName]={'product_name':product_ori_list[i],'listings':[]}
			else:
				res_dict[product_tempName]['listings'].append(data);
			break;
fp.close()


#output
file='../output.txt'
fp=open(file,'w+')
for key in res_dict:
	data=json.dumps(res_dict[key]);
	fp.write(data+'\n')
fp.close()



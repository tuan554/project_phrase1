# Thông tin: Nhà sản xuất, danh mục sản phẩm, sản phẩm
# + Nhà sản xuất: Số thứ tự, Tên nhà sản xuất, địa chỉ, phone: owner = [{ 'id': 1, 'name': 'Sam sung', 'address': 'viet nam', 'phone': '0120677773'}]
# + Danh mục:  Số thư tự, Tên danh mục, miêu tả: ví dụ: categories = [{'id': 1, 'name': 'Thời trang', 'description': 'Thời trang cho tre em'}]
# + Sản phẩm: Số thứ tự, Tên sản phẩm, giá, miêu tả, số lượng hàng còn, nhà sản xuất nào, danh mục nào, ảnh: 
# products = [{'id': 1, 'name': 'giay nam', 'description': ' giay cho gioi tre', 'price': 200000, 'owner_id': 1, 'category_id': 1}]
owner = []
categories = []
products = []

def list_id(oc):
    atr = []
    for item in oc:
        atr.append(item['id'])
    return atr

key1 = 'no'
id = 1
ownerid = []
while key1 == 'no':
    insert = {'id': id,
               'name': input('Enter name: '),
               'address': input('Enter address: '),
               'phone': input('Enter phone number: ')}
    owner.append(insert)
    ownerid.append(id)
    id = id + 1
    key1 = input('Enter key: ')

categoriesid = []
key2 = 'no'
id = 1
while key2 == 'no':
    insert = {'id': id,
               'name': input('Enter name: '),
               'description': input('Enter description: ')}
    categories.append(insert)
    categoriesid.append(id)
    id = id + 1
    key2 = input('Enter key: ')

ownerquestion = 'Enter owner id(choose from the following)',list_id(owner)
categoriesquestion = 'Enter category id(choose from the following)',list_id(categories)
key3 = 'no'
while key3 == 'no':
    insert = [{'id': id,
               'name': input('Enter name: '),
               'description': input('Enter description: '),
               'price': input('Enter price'),
               'owner_id': input(ownerquestion), 
               'categories_id': input(categoriesquestion)}]
    products.append(insert)
    id = id + 1
    key3 = input('Enter key: ')

print(owner)
print(categories)
print(products)
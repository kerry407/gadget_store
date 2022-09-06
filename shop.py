import sys
import random 




class Order:
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    number = str(random.randint(0, 9))
    symbols = '}{[]?/<>+=-)(*&^%$#@!~|'
    total_character = lower + upper + number + symbols

    products = {
        'iphone 12 pro': 340000, 
        'iphone 12 promax': 400000, 
        'iphone 13 pro': 450000, 
        'iphone 13 promax': 500000,
    }
    no_of_products = len(products)

    def __init__(self, customer_name, email, address, phone_number, product_name):
        self.customer_name = customer_name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.product_name = product_name
        self.cart = 0
        self.total_price = 0
         

    
    def addtocart(self, product):
        print(Order.products)
        item = list(Order.products) 

        print('AVAILABLE PRODUCTS AND THEIR PRICES:')
        for i in Order.products:
            print(f"{item.index(i)}.{i}, price: NGN {Order.products[i]}")
        
        if product in Order.products:
            self.product_name.append(product)
            print(f'{product} added to cart')
            print(self.product_name)


    def shopcart(self):
        # Create a unique item dictionary containing products as key and quantity as value
        unique_customer_items  = set()
        unique_customer_dict = {}

        
        for item in self.product_name:
            if Order.products.__contains__(item):
                unique_customer_items.add(item)
        for elem in unique_customer_items:
            if self.product_name.__contains__(elem):   
                unique_customer_dict[elem] = self.product_name.count(elem)
                # print(elem, ',' ,f'Qty: {self.product_name.count(elem)}')
        # Get total no. of items in cart
        self.cart = self.product_name.__len__()

        # Get total price of products in customer's cart
        self.total_price = sum(Order.products[i]*unique_customer_dict[i] for i in self.product_name if Order.products.__contains__(i))

        print('Product list:',unique_customer_dict)
        print(f"You have {self.cart} items in your shopcart!")
        print(f"Your total amount is {self.total_price} Naira!")


    def removefromcart(self, product):
        print('YOUR CART:')

        for item in self.product_name:
            print(f"{self.product_name.index(item)}. {item}")

        if product in self.product_name and Order.products.__contains__(product):
            self.product_name.remove(product)
            # self.total_price = self.total_price - Order.products[product]
            print(f'{product} successfully removed from cart')
        else:
            print(f'{product} not in cart')
        
    
    def get_order_code(self):
        order_code = "".join(random.choices(Order.total_character, k=24))
        print('Your order code:',order_code)
            

    @classmethod
    def get_no_of_products(cls):
        cls.no_items = Order.no_of_products
        return cls.no_items




order_1 = Order('Kerry Onyeogo', 'kerryonyeogo@gmail.com', '18, Adeleke street off Allen Avenue, Ikeja Lagos', '08102012239', product_name=['iphone 13 promax'])

# print(order_1.email)
# order_1.get_order_code()
# print(order_1.product)
# print(Order.get_no_of_products())
order_1.shopcart()
print('')
order_1.addtocart('iphone 12 pro')
order_1.addtocart('iphone 12 pro')
order_1.addtocart('iphone 13 pro')
print('')
order_1.shopcart()
# order_1.addtocart()
# print('')

# print('')
# order_2.shopcart()
# print('')
# order_1.removefromcart('iphone 12 pro')
# order_1.shopcart()




    




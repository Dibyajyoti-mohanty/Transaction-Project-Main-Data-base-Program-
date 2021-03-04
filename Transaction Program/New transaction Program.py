tr = [(('1210'),('apple',3),('grapes',4)),
       (('1211'),('pears',6),('mango',8),('orange',6)),
      (('1212'),('pears',2),('apple',3),('orange',4),('cherry',5),('mango',6),('apple',7)),
      (('1213'),('orange',9),('pears',8),('pineapple',5)),
      (('1214'),('grapes',3),('apple',7)),
      (('1215'),('mango',12),('orange',13),('guava',8),('Strawberry',10),('cherry',7)),
      (('1211'),('dates',15),('banana',10),('orange',10)),
      (('1214'),('dates',13),('banana',10),('Blackberry',2)),
      (('1215'),('dates',12),('apple',10),('mango',10),('cherry',8)),
      (('1216'),('apple',6),('dates',8),('jelly',5),('jackfruit',50))]


cu = [('1210','Rajesh'),('1211','Rakesh'),('1212','Sahil'),
      ('1213','Jack'),('1214','Steve'),('1215','Rohan'),('1216','Millan')]


item_detail = [('1001','apple',60),('1002','orange',40),('1003','pears',30),
               ('1004','mango',50),('1005','grapes',45),('1006','guava',40),
             ('1007','pineapple',60),('1008','dates',100),('1009','banana',10),
               ('1010','Strawberry',150),('1011','Blackberry',110),
              ('1012','cherry',90),('1013','jelly',20),('1014','jackfruit',40)]


stock_list =[('1001','apple',6000),('1002','orange',4000),('1003','pears',3000),
               ('1004','mango',5000),('1005','grapes',4500),('1006','guava',4000),
             ('1007','pineapple',6000),('1008','dates',1000),('1009','banana',1000),
               ('1010','Strawberry',1500),('1011','Blackberry',1100),
              ('1012','cherry',9000),('1013','jelly',2000),('1014','jackfruit',4000)]




print("{:>2}  {:10} {:10} {:>3}  {:5}  {:8}  {:>3}   {:>4}".format('ln','Item code','Item Name','Item Rate','CuID','CuName','Quantity','Amount'))
print()

x = 0
item = 0
quantity = 0
cu_id = 0
cu_name = 0
item_code = 0
item_rate = 0
amount = 0
quantity_sum = 0
amount_sum = 0
for i in range(len(tr)):
    for j in range(1,len(tr[i])):
        item = tr[i][j][0]
        quantity = tr[i][j][1]
        cu_id = tr[i][0]
        x = x+1


        for k in range(len(cu)):
            if cu_id == cu[k][0]:
                cu_name = cu[k][1]


            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity
        quantity_sum = quantity_sum + quantity
        amount_sum = amount_sum + amount

        print("{:>2}    {:8}   {:10}  {:>3}     {:>3}   {:8} {:>5} {:>10}".format(x,item_code,item,item_rate,cu_id,cu_name,quantity,amount))
print()
print("{}  {:>48}  {:>9} ".format('Total:- ',quantity_sum,amount_sum))



tr = [(('1210'),('apple',3),('grapes',4)),(('1211'),('pears',6),('mango',8),('orange',6)),
      (('1212'),('pears',2),('apple',3),('orange',4),('mango',6),('apple',7)),
      (('1213'),('orange',9),('pears',8),('pineapple',5)),(('1214'),('grapes',3),('apple',7)),
      (('1215'),('mango',12),('orange',13),('guava',8),('Strawberry',10)),
      (('1211'),('dates',15),('banana',10),('orange',10)),(('1214'),('dates',13),('banana',10),('Blackberry',2)),
      (('1215'),('dates',12),('apple',10),('mango',10))]


cu = [('1210','Rajesh'),('1211','Rakesh'),('1212','Sahil'),
      ('1213','Jack'),('1214','Steve'),('1215','Rohan')]


item_detail = [('1001','apple',60),('1002','orange',40),('1003','pears',30),
               ('1004','mango',50),('1005','grapes',45),('1006','guava',40),
             ('1007','pineapple',60),('1008','dates',100),('1009','banana',10),
               ('1010','Strawberry',150),('1011','Blackberry',110),
               ('1012','cherry',90)]
x = 0
amount = 0
q_sum = 0
a_sum = 0
item1 = 'orange'
c_id = ''
i_rate = 0
quantity = 0
c_name = ''
i_code = ''
for i in range(len(tr)):
    for j in range(1,len(tr[i])):                  
        item = tr[i][j][0]
        quantity = tr[i][j][1]
        c_id = tr[i][0]
        x = x+1
        for k in range(len(cu)):
            if c_id == cu[k][0]:
                c_name = cu[k][1]
        for l in range(len(item_detail)):
            if item == item_detail[i][1]:
                i_code = item_detail[i][0]
                i_rate = item_detail[i][2]
        amount = i_rate * quantity

        if item == item1:
            q_sum = q_sum + quantity
            a_sum = a_sum + amount
            print("{:>3}  {}  {}  {}  {:<9} {:<9} {:<10} {:>4}  {:>5}  {:>8}".format(x,i,j,c_id,c_name,i_code,item,i_rate,quantity,amount))
print()
print("  Total:-                                               {}     {}".format(q_sum,a_sum))







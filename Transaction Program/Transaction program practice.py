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



un_list = []

item = ''
quantity = 0
cu_id  = ''
cu_name = ''
item_code = ''
item_rate = 0
amount = 0
x = 0
for i in range(len(tr)):
    for j in range(1,len(tr[i])):
        item = tr[i][j][0]
        quantity = tr[i][j][1]
        cu_id = tr[i][0]
        

        for k in range(len(cu)):
            if cu_id == cu[k][0]:
                cu_name = cu[k][1]
            
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = quantity * item_rate
            
        if item not in un_list:
            un_list.append(item)
   
        print("{}  {:<10}  {:>3}  {}  {:<8} {:>3}  {:>4}".format(item_code,item,item_rate,cu_id,cu_name,quantity,amount))
print(un_list) 




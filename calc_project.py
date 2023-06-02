# # print('hello python')
# names = ["Tarteel", "Asmaa", "Ahmed"]
# # names.append("Sabrin")
# names.insert(0, "Sabrin")
# print(names)
# names.pop()
# print(names)
# names.append("Hamda")
# print(names)
# names.remove("Asmaa")
# print(names)
# ########q1
# friends = ["Adel", "Ahmed"]
# employees= ["Sameh", "Amjad"]
# school = ["Ali", "Basma"]
# new = friends + employees + school
# print(new)
# ############q2
# dic1 = {1: 10, 2:20}
# dic2 = {3: 30, 4:40}
# dic3 = {5: 50, 6:60}
# new_dic = {**dic1,**dic2,**dic3}
# print(new_dic)
# #########q3

# new_dict = {}
# for k in range (1, 16):
#     v = k*k
#     # dict = {k:v}
#     new_dict[k] = v
#     # print(dict, end="")
#     print(new_dict, end="")
# /#

# data = dict{k:v}
# for k,v in range (1, 16):
#     v = k*k
#     print(data)

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 150, 'b': 200, 'd': 300}
d3= {}
for k,v in d2.items():
    if k in d1:
        d3[k]= v + d1[k]
    else:
        d3[k]= v
print(d3)


# ###3
# new_dict= {}
# keys = ['Ten', 'Twenty','Thirty']
# values = [10, 20, 30]
# new_dict['Ten'] = 10
# new_dict['Twenty'] = 20
# new_dict['Thirty'] = 30
# print(new_dict)
########3
# sampleDict= {
#     "class":{
#         "student":{
#             "name": "Mike",
#             "mark":{
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# # first way
# print(sampleDict.get('class').get("student")
#       .get('mark').get('history'))
# # 2nd way
# v= sampleDict.get('class')
# c= v.get("student")
# b= c.get('mark')
# f= b.get('history')
# print(f)


# mydict= {1:"Alaa", 5:"Hadeel",
#          7:"Haneen", 13:"Malak"}
# for k,v in mydict.items():
#     if k <=10:
#         print(v, end="->")
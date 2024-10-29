#create a tuple with diffrent datatypes
tuplex=("tuple",False,3.2,1)
print(tuplex)

#create a tuple

tuplex=(4,6,2,8,3,1)
print(tuplex)
#tuples are immutable so you can not add new elements
#using merge of elememts+operator you can add an element and it will create a new tuple
tuplex=tuplex+(9,)
print(tuplex)
#counts the number occurrences of item 50 from a tuple
tuple1=(50,10,60,70,50)
print(tuple.count(50))

# create a tuplex
tuplex=(2,4,3,5,4,6,7,8,6,1)
#used tuple [start::stop] the start index is inclusive and the stop index
_slice=tuplex[3:5]
#is exclusive
print(_slice)
#if the start index isn't defiend, is taken from the beg inning of the tuple
_slice=tuple[:6]
print(_slice)









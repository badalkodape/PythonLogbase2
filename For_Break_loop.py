1) a5_all_even_numbers.py
--------------------------

numbers = [2,4,6]
for x in numbers:
    if x%2 == 1:
        break
else:
    print("All Even")
   
[ec2-user@cloud-bad ~]$ python3 a5_all_even_numbers.py

****************************************************************
                 OutPut:-
                     All Even
****************************************************************

2) a6_print_all_even_at_each_itearation.py
---------------------------------------

numbers = [2,4,6]
for x in numbers:
    if x%2 == 1:
        break
    else:
        print(f"x value is: {x} and it is even")
else:
    print("All Even")

[ec2-user@cloud-bad ~]$ python3 a6_print_all_even_at_each_itearation.py

*******************************************************************************
OutPut:-
  
x value is: 2 and it is even
x value is: 4 and it is even
x value is: 6 and it is even
All Even

*******************************************************************************

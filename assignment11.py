# Task: Explore in Google and Make a document :

# 1. What is data concatination in pandas ?
'''Concatenate pandas objects along a particular axis. Allows optional set logic along the other axes. 
Can also add a layer of hierarchical indexing on the concatenation axis, 
which may be useful if the labels are the same (or overlapping) on the passed axis number.'''

# 2. Types of data concatination in pandas?
# 3. What are the functions available for data concatination/append in pandas?


# Task: create a program
# Q1>Create and import file

import pandas as pd
# 1. Create boys Boysfriend_names.xls file and import file in spyder (atleast 10 names, columns are FriendName,Quality) ,
boys_friend_names=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\Boysfriend_names.xls")
print(boys_friend_names)

# 2. Create girls Girlsfriend_names.xls file and import file in spyder (atleast 10 names, columns are FriendName,Quality),
girls_freind_names=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\friend_names_dtfrm.xls")
print(girls_freind_names)

# 3. Append two dataframes and print data.
appended_data=pd.concat([boys_friend_names,girls_freind_names],axis=0,ignore_index=True)
print(appended_data)

# Q2>Create and import file
# 1. Create boys Boysfriend_names.xls file  (atleast 10 names, columns are boysFriendName,Quality) ,
# 2. Create girls Girlsfriend_names.xls file  (atleast 10 names, columns are GirlsFriendName,Quality),
boys_friend_names1=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\Boysfriend_names.xls")
print(boys_friend_names1)
girls_freind_names1=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\friend_names_dtfrm.xls")
print(girls_freind_names)
# 3. Append two dataframes and print data.
appended_data1=pd.concat([boys_friend_names,girls_freind_names],axis=0,ignore_index=True)
print(appended_data1)

# Q3>Create and import file
# 1. Create a father side fatherfamily_members.xls file and import file in spyder  (atleast 5 names, columns are FamilyMemberName*Relation)
# 2. Create a mother side montherfamily_members.xls file and import file in spyder  (atleast 5 names, columns are FamilyMemberName*Relation)
father_family=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\fatherfamily_members.xls")
print(father_family)
mother_family=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\montherfamily_members.xls")
print(mother_family)
# 3. Append two dataframes and print data.
family_members_data=pd.concat([father_family,mother_family],axis=0,ignore_index=True)
print(family_members_data)


# Q4>Create and import file
# 1. Create your sister names  Sisters.xls file and import file in spyder  (atleast 5 names, columns are SisterName*Relation)
# 2. Create your brother names Brothers.xls file and import file in spyder  (atleast 5 names, columns are BrotherName*Relation)
sisters_names_df=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\Sisters.xls")
print(sisters_names_df)
brother_names_df=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\Brothers.xls")
print(brother_names_df)
# 3. Append two dataframes and print data.
sis_bro_names_apnd=pd.concat([sisters_names_df,brother_names_df],axis=1)
print(sis_bro_names_apnd)


# Q5>Create and import file
# 1. Create a Dal related  dal_items.xlsx file and import file in spyder (atleast 5 names, columns are VegFoodName*Taste)
# 2. Create a vegitable related  vegitable_items.xlsx file and import file in spyder (atleast 5 names, columns are VegFoodName*Taste)
dal_items=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\dal_items.xlsx")
print(dal_items)
veg_items=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\vegitable_items.xlsx")
print(veg_items)
# 3. Append two dataframes and print data.
dal_veg_append=pd.concat([dal_items,veg_items],axis=1)
print(dal_veg_append)

# Q6>Create and import file
# 1. Create a soups related  soups_items.xlsx file and import file in spyder (atleast 5 names, columns are soups*Taste)
# 2. Create a fry related  fry_items.xlsx file and import file in spyder (atleast 5 names, columns are fry*Taste)
# 3. Append two dataframes and print data.


# Q7>Create and import file
# 1. Create a Chicken related chicken_items.xlsx file and import file in spyder (atleast 5 names, columns are NonVegFoodName*Taste)
chicken_items=pd.read_excel(r"C:\\Users\Abdul\\Downloads\\assignment8.a\\Chicken_items.xlsx")
print(chicken_items)
# 2. Create a mutton related mutton_items.xlsx file and import file in spyder (atleast 5 names, columns are NonVegFoodName*Taste)
mutton_items=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\Mutton_items.xlsx")
print(mutton_items)
# 3. Append two dataframes and print data.
chi_mut_append_df=pd.concat([chicken_items,mutton_items],axis=0,ignore_index=True)
print(chi_mut_append_df)


# Q8>Create and import file
# 1. Create a winter season  winterseason_names.xlsx file and import file in spyder  (atleast 2 names, columns are MonthName*Season)
win_names2=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\winterseason_names2.xlsx")
print(win_names2)
# 2. Create a summer season  summerseason_names.xlsx file and import file in spyder  (atleast 2 names, columns are MonthName*Season)
sum_names2=pd.read_excel(r"C:\\Users\Abdul\\Downloads\\assignment8.a\\summerseason_names2.xlsx")
print(sum_names2)
# 3. Create a rainy season  rainyseason_names.xlsx file and import file in spyder  (atleast 2 names, columns are MonthName*Season)
rainy_names2=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\rainyseason_names2.xlsx")
print(rainy_names2)
# 4. Append all dataframes and print data.
winsumrai_appended_df=pd.concat([win_names2,sum_names2,rainy_names2],axis=0,ignore_index=True)
print(winsumrai_appended_df)


# Q9>Create and import file
# 1. Create a red colour flowers redflowers_names.xlsx file and import file in spyder   (atleast 3 names, columns are FlowerName*color)
red3=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\redflowers_names3.xlsx")
print(red3)
# 2. Create a white colour flowers whiteflowers_names.xlsx file  and import file in spyder  (atleast 3 names, columns are FlowerName*color)
white3=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\whiteflowers_names3.xlsx")
print(white3)
# 3. Create a pink colour flowers pinkflowers_names.xlsx file and import file in spyder   (atleast 3 names, columns are FlowerName*color)
pink3=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\pinkflowers_names3.xlsx")
print(pink3)
# 4. Create a yellow colour flowers yellowflowers_names.xlsx file and import file in spyder   (atleast 3 names, columns are FlowerName*color)
yellow3=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\yellowflowers_names3.xlsx")
print(yellow3)
# 5. Append all dataframes and print data.
colours_append=pd.concat([red3,white3,pink3,yellow3],axis=0,ignore_index=True)
print(colours_append)


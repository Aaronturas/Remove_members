#Function to remove graduation members 
def remove_members(lst, yr):
  ptr1 = 1

  for r in range(len(lst)-1, -1, -1):
    grad_yr = lst[r][ptr1]
    booleen = lst[r][ptr1+1]
    if grad_yr > yr or booleen == False:
      del lst[r]
  return lst

#Test cases
member_list = [["Jane Smith", 2019, False],
              ["Steve Fox", 2018, True ],
              ["Michael Xin", 2017, False],
              ["Maria Garcia", 2020, True]]

year = 2020

print("\nInput \nmember_list = ", member_list, "\nyear = ", year)
print("\nOutput: ", remove_members(member_list, year))

member_list = []
year = 2022

print("\nInput \nmember_list = ", member_list, "\nyear = ", year)
print("\nOutput: ", remove_members(member_list, year))

member_list = [["Jane Smith", 2019, False],
               ["Steve Fox", 2018, True ],
               ["Michael Xin", 2017, False],
               ["Maria Garcia", 2020, True]]
year = 2018

print("\nInput \nmember_list = ", member_list, "\nyear = ", year)
print("\nOutput: ", remove_members(member_list, year))
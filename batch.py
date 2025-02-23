import pandas as pd

#reading the excel file 
xls = pd.ExcelFile("test.xlsx")
# print(xls.sheet_names)

inFile = pd.read_excel(xls, sheet_name="Target List_original",header= 0)
# print(inFile.columns)

#keywords to look out for 
keywords = ['San Diego','California','health','life science','drug','early-stage','biotechnology','vision','contact lens','medical devices','pharmaceuticals','chemicals','medicine']

# this functino will check how much the company description matches the keywords 
def priorities(row):
    count = 0 #match count, checks to see how many of the keywords are in the company desciption
    for word in keywords:
        if pd.notna(row['Company Description']) and word.lower() in str(row['Company Description']).lower():
            count +=1 

    matchPercentage = (count / len(keywords)) * 100

    #assign priorities 

    # 65 to 100% match or is based in san diego
    if matchPercentage >= 65 or ('San Diego' in str(row['Company Description'])): 
        return 'Priority 1'
 
    elif matchPercentage < 64 and matchPercentage >= 30: 
        return 'Priority 2'
    elif matchPercentage < 29 and matchPercentage >= 10: 
        return 'Priority 3'
    else:
        return 'Priority 4'

#apply the function to each row
if 'Company Description' in inFile.columns:
    inFile['Priority'] = inFile.apply(priorities, axis=1)
else:
    print("Column 'Company Description' not found in the data.")

#sort the priority 
inFile = inFile.sort_values(by = 'Priority', ascending=True)

#create batch 
inFile['Batch'] = inFile.groupby('Priority').cumcount() // 50 + 1

#write to Excel 
with pd.ExcelWriter("sorted_and_batched_investor.xlsx") as writer:
    for priority in inFile['Priority'].unique():
        priority_inFile = inFile[inFile['Priority'] == priority]
    
        for batch in priority_inFile['Batch'].unique():
            batch_inFile = priority_inFile[priority_inFile['Batch'] == batch]

            sheet_name = f"{priority}_Batch{batch}"

            batch_inFile.to_excel(writer, sheet_name = sheet_name, index=False)
print("sorted and batched")
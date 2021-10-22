import csv
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

data = pd.read_csv("/cs_school_data/cs_2016-2017.csv")
df = pd.DataFrame(data)
school_name = df["School Name"]
num_course = df["# of Comp Sci Courses"]
fig = plt.figure(figsize=(20, 8))
plt.bar(school_name[0:10], num_course[0:10])
plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize= 9 
)
plt.title('A Random Sample Of Number Of CS Courses Offered By Schools In The NYC School District')
plt.xlabel('Schools')
plt.ylabel('Number of CS Courses')
plt.tight_layout()
plt.show()





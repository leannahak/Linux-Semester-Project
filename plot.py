import matplotlib.pyplot as plt
import random
import math
from matplotlib.lines import Line2D  # Import Line2D for custom legend handles

# Create a figure instance that will later be written to a PDF
f = plt.figure()
x = []
y = []
colors = []

m = open("prod3.txt")
line = m.readline()
while line:
    fields = line.split("|")
    x.append(math.log10(float(fields[1])))  # Persian ratio
    y.append(math.log10(float(fields[3])))  # New corp ratio
    colors.append(1)
    x.append(math.log10(float(fields[2])))  # Korean ratio
    y.append(math.log10(float(fields[3])))  # New corp ratio
    colors.append(2)

    line = m.readline()

m.close()

# Create custom legend handles with desired colors and labels
legend_handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor='purple', markersize=10, label='Persian'),
                  Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', markersize=10, label='Korean')]

# Do the scatter plot with specified colors and sizes
scatter1 = plt.scatter(x, y, c=colors, alpha=0.05)

# Create a legend with custom handles and labels
legend = plt.legend(handles=legend_handles, title="Key", fontsize='small')

# Specify the x and y axis labels
plt.xlabel("Log of Foreign Born Percent")
plt.ylabel("Log of New Businesses Created per Capita")

# Save the plot into a PDF file
f.savefig("PersianandKoreanBusiness.pdf")

# Show the plot (optional)
plt.show()

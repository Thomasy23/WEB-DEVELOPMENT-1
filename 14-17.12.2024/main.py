from prettytable import PrettyTable

table = PrettyTable(["animal", "ferocity"])

table.add_row(["wolverine", 100])
table.add_row(["squirel", 0])
table.add_row(["dolphin", 50])

print(table)

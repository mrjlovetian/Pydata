import pandas as pd
path = 'qbb.xlsx'
colmuns = ['month', 'value', 'users']
qbb = pd.read_excel(path, names=colmuns)
new_qbb = qbb.pivot_table(index='month', aggfunc=sum)
print(new_qbb)

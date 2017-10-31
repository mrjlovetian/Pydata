import pandas as pd

years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'babynames/yob%s.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)
# total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
# total_births.plot(title='小孩')
# print(total_births)


def add_prop(group):
    # 证书除法向下元整
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group

def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]

groupby_year_sex = names.groupby(['year', 'sex']).apply(add_prop)

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
boys = top1000[top1000.sex == 'F']
print(boys)

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
subset = total_births[['John', 'Harry', 'Marry', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title='number of births per year')



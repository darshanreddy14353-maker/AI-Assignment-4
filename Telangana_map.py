districts = [
'Adilabad','Nirmal','Nizamabad','Kamareddy','Karimnagar','Peddapalli',
'Rajanna','Jagitial','Warangal','Hanamkonda','Jangaon','Mahabubabad',
'Khammam','Bhadradri','Medak','Siddipet','Sangareddy','Hyderabad',
'Medchal','Rangareddy','Vikarabad','Mahabubnagar','Nagarkurnool',
'Wanaparthy','Narayanpet','Nalgonda','Suryapet','Yadadri','Mulugu',
'Jayashankar','KomaramBheem','Mancherial','Kothagudem'
]

colors = ['Red','Green','Blue','Yellow']

neighbors = {d: [] for d in districts}

neighbors['Hyderabad'] = ['Rangareddy','Medchal']
neighbors['Rangareddy'] = ['Hyderabad','Vikarabad']
neighbors['Khammam'] = ['Bhadradri']

def is_valid(d, color, assign):
    for n in neighbors[d]:
        if n in assign and assign[n] == color:
            return False
    return True

def solve(assign={}):
    if len(assign) == len(districts):
        return assign

    d = [x for x in districts if x not in assign][0]

    for c in colors:
        if is_valid(d, c, assign):
            assign[d] = c
            res = solve(assign)
            if res:
                return res
            del assign[d]

    return None

print("\nTelangana Map Coloring:")
print(solve())

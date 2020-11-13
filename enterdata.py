classB = []
classV = []
classI = []
classS = []
a = 'o'
def inputData():
    mg = {'name': input('Enter name'),
        'mathScore': int(input('Enter math score: ')),
        'literatureScore': int(input('Enter literature score: ')),
        'englishScore': int(input('Enter English score: '))}
    return mg

while a == 'o':
    mg = inputData()
    nhap = input('Select a class(b, v, i, s):')
    if nhap == 'b':
        classB.append(mg)
    elif nhap == 'v':
        classV.append(mg)
    elif nhap == 'i':
        classI.append(mg)
    elif nhap == 's':
        classS.append(mg)
    a = input('Enter code to continue')

for e in classB:
    print(e['name'] + ', Math score: ' + str(e['mathScore']))
d = 0
t = 0
for i in classB:
    average = (i['mathScore']+i['literatureScore']+i['englishScore'])/3
    d = d + int(average)
    t = t + 1
print('Average score:', d / t)

import numpy as np
import matplotlib.pyplot as plt
import csv

header = []
fileName1 = "Esda1_maling_2.csv"
fileName2 = "Esda1_maling_3.csv"

#finner den største og den femtiende største verdien:
def femti_største(csv_fil):
    
    with open(csv_fil, 'r') as file:
        data=csv.reader(file)
        spenninger=[]
        for rad in data:
            spenninger.append(float(rad[1]))
        
        størsteverdier=sorted(spenninger)[-50:-1]
        return størsteverdier[0], størsteverdier[-1]


def readFile(filename):
    data = []

    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)

        header = next(csvreader)

        for datapoint in csvreader:
            values = [float(value) for value in datapoint]
            data.append(values)

    time = [(p[0]*1000) for p in data]
    ch = [(p[1]) for p in data]
    return time, ch

time1, ch1 = readFile(fileName1)
time2, ch2 = readFile(fileName2)

fig, (ax) = plt.subplots(1,1)
ax.plot(time1,ch1, label = 'A1')
ax.plot(time2,ch2, label = 'A2')
ax.set_title('Oscilloskop')
ax.set_xlabel('Tid (ms)')
ax.set_ylabel('Spenning (V))')
ax.legend(loc='upper right')
ax.grid(True)

plt.savefig('AmaxRes.png', dpi=500)
plt.show()


print(f'A1: \nstørste: {femti_største("Esda1_maling_2.csv")[1]}\nminste:  {femti_største("Esda1_maling_2.csv")[0]}')
print(f'\nA2: \nstørste: {femti_største("Esda1_maling_3.csv")[1]}\nminste:  {femti_største("Esda1_maling_3.csv")[0]}')
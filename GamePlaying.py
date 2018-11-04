class Person:
    def __init__(self, applicantId, gender, age, pets, medicalCondition, car, driverLicence, daysPlaceNeeded):
        self.applicantId = applicantId
        self.name = " steve "
        self.gender = gender
        self.age = age
        self.pets = pets
        self.medicalCondition = medicalCondition
        self.car = car
        self.driverLicence = driverLicence
        self.daysPlaceNeeded = daysPlaceNeeded


def SPLAefficiency():
    SPLADaysOccupied = [0, 0, 0, 0, 0, 0, 0]
    for i in already_spla_person:
        days = i.daysPlaceNeeded
        for j in range(len(days)):
            if (days[j] == '1'):
                SPLADaysOccupied[j] += 1
    return SPLADaysOccupied


def LAHSAefficiency():
    LAHSADaysOccupied = [0, 0, 0, 0, 0, 0, 0]
    for i in already_lahsa_person:
        days = i.daysPlaceNeeded
        for j in range(len(days)):
            if (days[j] == '1'):
                LAHSADaysOccupied[j] += 1
    return LAHSADaysOccupied


def AllPossibleLAHSA():
    checkCompatible = []
    l = []
    l = LAHSAefficiency()
    for eachApplicant in lahsa:
        flag = 0
        daysOccupied = l[:]
        days = eachApplicant.daysPlaceNeeded
        for j in range(len(days)):
            if (days[j] == '1'):
                daysOccupied[j] += 1
        for j in range(len(daysOccupied)):
            if daysOccupied[j] > B:
                flag = 1
                break
        if flag == 0:
            checkCompatible.append(eachApplicant)
    return checkCompatible

def AllPossibleSPLA():
    checkCompatible = []
    l = []
    l = SPLAefficiency()
    for eachApplicant in spla:
        flag = 0
        daysOccupied = l[:]
        days = eachApplicant.daysPlaceNeeded
        for j in range(len(days)):
            if (days[j] == '1'):
                daysOccupied[j] += 1
        for j in range(len(daysOccupied)):
            if daysOccupied[j] > P:
                flag = 1
                break
        if flag == 0:
            checkCompatible.append(eachApplicant)
    return checkCompatible

def sumEfficiency(participant):
    finalSum = 0
    if participant == "spla":
        SPLADaysOccupied = SPLAefficiency()
        for i in SPLADaysOccupied:
            finalSum += i
    elif participant == "lahsa":
        LAHSADaysOccupied = LAHSAefficiency()
        for i in LAHSADaysOccupied:
            finalSum += i
    return finalSum

def greedyApproach():
    SPLADaysOccupied = [0, 0, 0, 0, 0, 0, 0]
    for i in already_spla_person:
        days = i.daysPlaceNeeded
        for j in range(len(days)):
            if (days[j] == '1'):
                SPLADaysOccupied[j] += 1


    Maxlist = {}
    if len(common)>0:
        for p in common:
            flag = 0
            list1 = []
            for i in SPLADaysOccupied:
                list1.append(i)
            days = p.daysPlaceNeeded
            for j in range(len(days)):
                if (days[j] == '1'):
                    list1[j] += 1
            for j in list1:
                if list1[j] > P:
                    flag = 1
                    break
            if flag == 0:
                count = 0
                for j in list1:
                    count += j
                Maxlist[p.applicantId] = count
    else:
        print spla
        for p in spla:
            flag = 0
            list1 = []
            for i in SPLADaysOccupied:
                list1.append(i)
            days = p.daysPlaceNeeded
            for j in range(len(days)):
                if (days[j] == '1'):
                    list1[j] += 1
            for j in list1:
                if list1[j] > P:
                    flag = 1
                    break
            if flag == 0:
                count = 0
                for j in list1:
                    count += j
                Maxlist[p.applicantId] = count

    print Maxlist

    max = 0
    index = 100000000
    for key, value in Maxlist.iteritems():
        #print value
        if value==max:
            if key < index:
                index = key
        elif value>max:
            index = key
            max = value
    #print max
    finalid = 0
    for key, value in Maxlist.iteritems():
        if value == max:
            finalid = index
            break
    return finalid

def Game(participant,cutOff):
    e = []
    cutOff+=1
    if participant == "spla":
        AllAvailableSPLA = AllPossibleSPLA()
        if len(AllAvailableSPLA) == 0 or cutOff ==14:
            AllAvailableLAHSA = AllPossibleLAHSA()
            daysOccupied = LAHSAefficiency()
            for a in AllAvailableLAHSA:
                flag3 = 0
                days = a.daysPlaceNeeded
                for j in range(len(days)):
                    if (days[j] == '1'):
                        daysOccupied[j] += 1
                for j in daysOccupied:
                    if daysOccupied[j] > P:
                        flag3 = 1
                        break
                if flag3==0:
                    # check no of beds
                    already_lahsa_person.append(a)
            x = sumEfficiency("spla")
            y = sumEfficiency("lahsa")
            for a in AllAvailableLAHSA:
                if a in already_lahsa_person:
                    already_lahsa_person.remove(a)

            list4 = [-1, x, y]
            return list4
        for a in AllAvailableSPLA:
            flagl = -1
            flags = -1
            temp = []

            already_spla_person.append(a)
            if a in spla:
                flags = 0
                spla.remove(a)
            if a in lahsa:
                flagl = 0
                lahsa.remove(a)

            eff = Game("lahsa",cutOff)
            temp.append(a.applicantId)
            temp.append(eff[1])
            temp.append(eff[2])
            e.append(temp)

            if flags == 0:
                spla.append(a)
            if flagl == 0:
                lahsa.append(a)
            already_spla_person.remove(a)

        maxEfficiency = 0
        id1 = -1
        lahsaefficiency = 0
        for temp in e:
            eff1 = temp[1]
            if eff1 > maxEfficiency:
                maxEfficiency = eff1
                lahsaefficiency = temp[2]
                id1 = temp[0]
        efficiencyList = [id1, maxEfficiency, lahsaefficiency]

        return efficiencyList

    elif participant == "lahsa":
        AllAvailableLAHSA = AllPossibleLAHSA()
        if len(AllAvailableLAHSA) == 0 or cutOff ==14:
            AllAvailableSPLA = AllPossibleSPLA()
            efficiencySPLA = SPLAefficiency()
            for a in AllAvailableSPLA:
                flag3=0
                days = a.daysPlaceNeeded
                for j in range(len(days)):
                    if (days[j] == '1'):
                        efficiencySPLA[j] += 1
                for j in range(len(efficiencySPLA)):
                    if efficiencySPLA[j] > P:
                        flag3 = 1
                        break
                if flag3==0:
                    already_spla_person.append(a)

            x = sumEfficiency("spla")
            y = sumEfficiency("lahsa")
            for a in AllAvailableSPLA:
                if a in already_spla_person:
                    already_spla_person.remove(a)

            list4 = [-1, x, y]  # maintain applicant id.

            return list4
        for a in AllAvailableLAHSA:
            flagl = -1
            flags = -1
            temp = []

            already_lahsa_person.append(a)
            if a in spla:
                flags = 0
                ind = spla.index(a)
                spla.remove(a)
            if a in lahsa:
                flagl = 0
                ind = lahsa.index(a)
                lahsa.remove(a)

            eff = Game("spla",cutOff)
            temp.append(a.applicantId)
            temp.append(eff[1])
            temp.append(eff[2])
            e.append(temp)

            if flags == 0:
                spla.append(a)
            if flagl == 0:
                lahsa.append(a)
            already_lahsa_person.remove(a)

        maxEfficiency = 0
        splaefficiency = 0
        id1 = -1
        for temp in e:
            eff1 = temp[2]
            if eff1 > maxEfficiency:
                maxEfficiency = eff1
                id1 = temp[0]
                splaefficiency = temp[1]
        efficiencyList = [id1, splaefficiency, maxEfficiency]

        return efficiencyList

ft = open("output.txt", "w+")
with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    B = int(lines[0])
    P = int(lines[1])
    L = int(lines[2])

    already_lahsa = [] 
    for i in range(3, L + 3):
        already_lahsa.append(int(lines[i]))

    k = L + 3
    s = int(lines[k])

    already_spla = []
    for i in range(k + 1, k + s + 1):
        already_spla.append(int(lines[i]))

    k = k + s + 1
    a = int(lines[k])
    totalApplicants = []  # all applicant list  not chosen till now
    notInTotalApplicants = []  # all applicant list already chosen till now

    for i in range(k + 1, k + a + 1):
        str1 = lines[i]
        flag = 0
        id = int(str1[0:5])
        for j in already_lahsa:
            if (id == j):
                flag = 1
                break
        for j in already_spla:
            if id == j:
                flag = 1
                break

        if flag == 1:
            p = Person(int(str1[0:5]), str1[5:6], int(str1[6:9]), str1[9:10], str1[10:11], str1[11:12], str1[12:13],
                       str1[13:20])
            notInTotalApplicants.append(p)
            continue
        p = Person(int(str1[0:5]), str1[5:6], int(str1[6:9]), str1[9:10], str1[10:11], str1[11:12], str1[12:13],
                   str1[13:20])
        totalApplicants.append(p)

    lahsa = []
    spla = []
    common = []

    for p in totalApplicants:
        flag1 = 0
        flag2 = 0
        flag3 = 0
        if p.car == "Y" and p.driverLicence == "Y" and p.medicalCondition == "N":
            flag1 = 1

        if p.gender == "F" and p.age > 17 and p.pets == "N":
            flag2 = 1

        if flag1 == 1 and flag2 == 1:
            flag3=1

        if flag3==1:
            common.append(p)
        else:
            if flag1==1:
                spla.append(p)
            if flag2==1:
                lahsa.append(p)

    spla = spla + common
    lahsa = lahsa + common

    # Creating separate lists that contain entire persons who LAHSA, SPLA have already taken
    already_lahsa_person = []
    for i in already_lahsa:
        for j in notInTotalApplicants:
            if i == j.applicantId:
                already_lahsa_person.append(j)
                break

    already_spla_person = []
    for i in already_spla:
        for j in notInTotalApplicants:
            if i == j.applicantId:
                already_spla_person.append(j)
                break

    SPLADaysOccupied = [0, 0, 0, 0, 0, 0, 0]
    for i in spla:
        days = i.daysPlaceNeeded
        for j in range(len(days)):
            if (days[j] == '1'):
                SPLADaysOccupied[j] += 1

    maximum = max(SPLADaysOccupied)

    if P > maximum:
        sukriti = greedyApproach()
        sukriti = str(sukriti).zfill(5)
    else:
        x = Game("spla",1)
        print "answer is"
        print x
        sukriti = str(x[0]).zfill(5)

    print sukriti
    ft.write(sukriti)
    f.close()
    ft.close()

def insertionSort(case):
    #Vi starter ud med at definere at vi har en funktion som hedder insertionSort. Den skal køre for hvert case vi har.
    for i in range(1, len(case)):
        #Den skal altså gøre igennem hvert eneste index i vores case, fra 1 til den totale længde af casen.
        curNum = case[i]
        #Her der definerer vi at det nuværende nummer som sammenlignes med, er case[i]
        for j in range(i-1, -1, -1):
            if case[j] > curNum:
                case[j+1] = case[j]
                # Loopet bestemmer at den sammeligner case [j] sammen med det nuværende nummer
                # Hvis case[j] er større, flytter algoritmen en lavere på vores liste.
            else:
                j+=1
                break
            case[j]=curNum
                # Hvis ikke nummeret er større, så skal koden tilføje et til det nuværende nummer vi arbejder med
                # så listen bevæger sig længere og længere imod slutningen, og herefter slutte så koden lopper.



def selectionSort(case):
#Ligesom insertionSort, så skal vi definere funktionen som kører igennem hvert et case.
#Et case er defineret i performanceTests.py.
    for i in range (0, len(case) - 1):
    #Her siger vi at algoritmen skal læse vores case igennem fra 0 til længden af casen -1, hvilket er fra start til slut.
        minIndex = i
    #minIndex bliver så defineret som det første index i listen. Dette skal vi bruge til sammenligninger.
        for j in range (i+1, len(case)):
            if case[j] < case[minIndex]:
                minIndex = j
        #Her definerer vi vores forloop, som læser igennem de ulæste dele af casen, og sammenligner for at finde den mindste værdi.
        if minIndex !=i:
            case[i], case[minIndex] = case[minIndex], case[i]
    #Hvis minIndex ikke har samme værdi som i, så skal de to værdier vi har fat i bytte plads.




#Følgende er en test for at se om vores algoritmerne kan sortere både tekst og tal rigtigt.
#Fjern indent på testPrint() for test
def testPrint():
    list1 = ["yeet", "skeet", "meat", "deet", "beat", "greet", "seat", "feet", "kage"]
    list2 = [1,2,3,4,1,23]
    insertionSort(list1)
    print ("Insertion sort, Liste 1:")
    print (list1)
    selectionSort(list1)
    print ("Selection sort, Liste 1:")
    print (list1)
    insertionSort(list2)
    print ("Insertion sort, Liste 2:")
    print (list2)
    selectionSort(list2)
    print ("Insertion sort, Liste 2:")
    print (list2)
testPrint()

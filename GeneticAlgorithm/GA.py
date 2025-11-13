import random
import math


#Name: Grant Harsch
#Date Created: 9/22/25
#Last Modified: 9/29/25
#Description: A class that defines chromosomes and their attributes.
#The class has 3 attributes, the array of tasks, the chromosome ID, and the fitness value of the chromosome. 
#Variables: array, ID, fit_value, and a method called popChrom that populates the chromsome's array. 
#Returns: Nothing, a variable in main can be assigned this class. 
class ChromClass: 
    def __init__(self, ID):
        self.array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.ID = ID
        self.fit_value = 0

    #//Name: Jaden Alesi
    #//Date Created: 9/23/25
    #//Last Modified: 9/23/25
    #//Description: Randomizes which tasks will be in the genes of a chromosome on startup. 
    #//Variables:  ChromArray: the array of genes in a chromosome
    #//Returns:  nothing, but populates the chromosome
    def popChrom(self):
        i = 0
        while i<16:
            self.array[i] = random.randint(1,9)
            i = i + 1

#//Name: Daniel Hough
#//Date Created: 9/25/25
#//Last Modified: 9/25/25
#//Description: Calculates fitness value of a chromosome.
#//Variables:  chrom: the array of genes in a chromosome, arrt: array of time values for tasks, arrp: array of priority values for tasks.
#//Returns:  Fitness value
def findFitness(chrom, arrt, arrp):
    task = 0
    fitnessVal = 0
    while task < 9:
        times = chrom.array.count(int(task))
        fitFromCurrTask = 4**(arrp[task]*times/arrt[task]*math.exp(-1/(times+0.0001)*(abs(1-math.exp((times-arrt[task]))))))
        fitnessVal = fitnessVal + fitFromCurrTask
        task = task + 1
    return fitnessVal

#//Name: Jaden Alesi
#//Date Created: 9/25/25
#//Last Modified: 9/30/25
#//Description: Performs the selection part of the GA, using the roulette method to determine which members of the poulation get to reproduce.
#//Variables:  fitnessArray - Array to hold the fitness values for chromosomes
#              percentageArray - Array to hold the percentages corresponding to each chromosome
#              totalFitness - The total fitness value, used for finding percentages
#              parentArray - holds the two selected chromosomes
#//Returns:  Nothing, but modifies the parent array.
def roulette(populationArray, parentArray):
    #Array to hold the fitness for reference
    fitnessArray = []
    #Array to hold the corresponding percentages. 
    percentageArray = []
    #Value for the total fitness 
    totalFitness = 0.0

    #get the fitness for each member of the population
    for i in range(len(populationArray)):
        fitnessArray.append(populationArray[i].fit_value)
        totalFitness = totalFitness+fitnessArray[i]
    #get the relative percentage for each member of the population
    for i in range(len(fitnessArray)):
        currPercent = (fitnessArray[i]/totalFitness) * 100.0
        percentageArray.append(currPercent)
    #get the two parents, making sure to remove them from being eligible for secod selection.
    for i in range(2):
        selection = random.choices(populationArray, weights=percentageArray, k=1)[0]
        toRemove = populationArray.index(selection)
        percentageArray[toRemove] = 0.0
        parentArray.append(selection)

#Name: Grant Harsch
#Edits: Jaden Alesi
#Date Created: 9/28/25
#Last Modified: 9/29/25 - grant
#Description: Order Cross Over is performed here. Our chromosomes have several duplicates of genes. This created an issues when using the order 
# of the chromosomes. When a number is found in the middle slice of the array we do not add that number, but if that same number were too come up later
# then some bugs would come up and the child would not be complete. So to combat this we chose to count the amount of duplicates found in the order
# and children so that we are not checking if that number is in the middle slice but rather how many duplicates of that number are in the middle slice.
# In the end it all worked out and the order cross over works.   
#Variables: Chromsome objects parent1, and 2
# altPopulation which is basically the new population being made for the 2 children that are made.  
# crossOverPoint1, and 2 show where the cross over is done. 
# orderOfParent1, and 2 show the order of the child. Last slice -> first slice -> middle slice
# child1, and 2 are the children that will be put into the altPopulation.  
#Returns: A modified altPopulation. 
def crossOver(parent1, parent2, altPopulation):
    #2 points are chosen for the split in the chromsome. If you want to change the values of these points to experiment you can. 
    crossOverPoint1 = 4
    crossOverPoint2 = 14
    
    #The order of the crossover is put into arrays later which are set here.
    orderOfParent1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    orderOfParent2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #The children are objects.
    child1 = ChromClass(parent1.ID)
    child2 = ChromClass(parent2.ID)

    #Copy the center slice of the parents in their respective children. 
    child1.array[crossOverPoint1:crossOverPoint2] = parent1.array[crossOverPoint1:crossOverPoint2]
    child2.array[crossOverPoint1:crossOverPoint2] = parent2.array[crossOverPoint1:crossOverPoint2] 

    #Place the 3 different parts of the sliced parents into their respective order arrays. 
    orderOfParent1 = parent1.array[crossOverPoint2:len(parent1.array)] + parent1.array[0:crossOverPoint1] + parent1.array[crossOverPoint1:crossOverPoint2]
    orderOfParent2 = parent2.array[crossOverPoint2:len(parent2.array)] + parent2.array[0:crossOverPoint1] + parent2.array[crossOverPoint1:crossOverPoint2]

    #While loops for first child
    #First in the order is the right slice. [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #                                                                    ^
    j = crossOverPoint2
    i = 0

    while i < (len(child1.array)) and j < len(child1.array):
        if (child1.array.count(orderOfParent2[i]) < orderOfParent2.count(orderOfParent2[i])):
            child1.array[j] = orderOfParent2[i]
            j = j + 1
            i = i + 1
        else:
            i = i + 1

    #Set j at front of the array to continue order through the front slice [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #                                                                       ^
    #Not resetting i because that would reset the order array and we still want that.
    j = 0

    while i < (len(child1.array)) and j < crossOverPoint1:
        if (child1.array.count(orderOfParent2[i]) < orderOfParent2.count(orderOfParent2[i])):
            child1.array[j] = orderOfParent2[i]
            j = j + 1
            i = i + 1
        else:
            i = i + 1

    #While loops for second child
    #Comments would be the same as they were for the first child so I am not adding them here. 
    j = crossOverPoint2
    i = 0

    while i < (len(child2.array)) and j < len(child2.array):
        if (child2.array.count(orderOfParent1[i]) < orderOfParent1.count(orderOfParent1[i])):
            child2.array[j] = orderOfParent1[i]
            j = j + 1
            i = i + 1
        else:
            i = i + 1

    j = 0

    while i < (len(child2.array)) and j < crossOverPoint1:
        if (child2.array.count(orderOfParent1[i]) < orderOfParent1.count(orderOfParent1[i])):
            child2.array[j] = orderOfParent1[i]
            j = j + 1
            i = i + 1
        else:
            i = i + 1
    
    #Children are appended into the altPopulation array. 
    altPopulation.append(child1)
    altPopulation.append(child2)

    return altPopulation

#Name: Logan Haberman
#Date Created: 9/29/25
#Last Modified: 9/30/25
#Description: Performs the mutation for the GA using a random random method
#for the mutation of a gene in the chromosome.
#Variables: chromosome
#Returns: Nothing
def mutation(chromosome, mutation_prob=0.1):
    if random.random() < mutation_prob:
        #checks to see if mutation will occur

        mutatedIndex = random.randint(0, len(chromosome.array) - 1)
        #decides on gene to mutate in chromosome

        mutatedGene = random.randint(1, 9)
        #randomly mutates the gene

        chromosome.array[mutatedIndex] = mutatedGene
        #replaces old value with mutated value

#           print("mutated chromosome: " , chromosome.array)


#Name: Jaden Alesi
#Date Created: 9/30/25
#Last Modified: 9/30/25
#Description: Performs the replacement of the GA, using the parameters provided
#Variables: currPop - The current population
#           outPop - The outgoing population
#           checkRoom - Checks to see if there's room in the generation for kids.
#Returns: The next generation
def replacement(currPop, children, genSize, popSize, immChance):
    checkRoom = 0
    print (children[0].ID)
    sortedList = sorted(currPop, key=lambda chrom:chrom.fit_value, reverse=True)
    while checkRoom != genSize: #while there isn't room in the population
        for i in range(len(sortedList)-1, 0, -1): #for each chromosome starting from the worst
            if checkRoom == genSize: #if there is enough space already
                break #finish checking and leave
            elif i-1 < 0: #if we've miraculosly managed to have everyone roll insanely well and survive
                while checkRoom != genSize: #while there isn't room
                    cull = sortedList.pop() #kill the lowest fitness member
                    children[checkRoom].ID = cull.ID
                    checkRoom = checkRoom + 1 #increase the room count
            elif random.random() <= immChance: #if that chromosome randomly survives
                break #go to the next chromosome
            else: #otherwise
                cull = sortedList.pop(i) #kill that member of the population
                children[checkRoom].ID = cull.ID
                checkRoom = checkRoom + 1 #increase the room count
    sortedList = sortedList + children #add the kids
    return sortedList #return the new population

def main():
    #Variables will follow camelCase, and attributes from the chromosome class follow snake_case
    #Parameters
    popSize = 250  #Total size of population (Increased to 200 to allow more consistent ).
    genSize = 100  #number of children each generation and low fitness individuals to cull. ()
    numGens = 80 #Number of generations to run. (Roughly where runs usually seem to reach maximum fitness by)
    immChance = 0.08 #chance of random survival by otherwise culled members of population during replacement
    #Mutation rate is in mutation function, edit there if need be.

    populationArray = []
    timeArray = [6, 3, 5, 4, 1, 1, 7, 6, 4] #constant random array of times for 9 tasks
    priorityArray = [3, 2, 3, 2, 1, 2, 3, 1, 3] #constant random array of priorities for 9 tasks
    altPopulation = []
    parentArray = []
    bestFit = 0.0
    totalFit = 0.0
    meanFit = 0.0

    #Initialize Population
    for i in range(popSize):
        newObject = ChromClass(i+1)
        #Call the popChrom function in the newly made object. 
        newObject.popChrom()
        
        populationArray.append(newObject)

        #Evaluate initial fitness
        newObject.fit_value = findFitness(newObject, timeArray, priorityArray)

        print(populationArray[i].ID, ' ', populationArray[i].array, ' ', newObject.fit_value)

    #begin loop
    for k in range(numGens): 
        while len(altPopulation) != genSize:
            parentArray.append(roulette(populationArray, parentArray)) #select parents
            crossOver(parentArray[0], parentArray[1], altPopulation) #perform crossover
            parentArray.clear()
        for j in range(len(altPopulation)):
            mutation(altPopulation[j]) #Apply mutation
            altPopulation[j].fit_value = findFitness(altPopulation[j], timeArray, priorityArray) #Evaluate offspring
        populationArray = replacement(populationArray, altPopulation, genSize, popSize, immChance) #Replacement
        altPopulation.clear()

        i = 0
        bestFit = populationArray[i].fit_value
        for i in range(popSize):
            if populationArray[i].fit_value > bestFit:
                bestFit = populationArray[i].fit_value
            totalFit = totalFit + populationArray[i].fit_value
        meanFit = totalFit/popSize
        print("Generation " + str(k) + ":")
        print("Best Fitness: " + str(bestFit))
        print("Mean Fitness: " + str(meanFit))
        bestFit = 0.0
        meanFit = 0.0
        totalFit = 0.0

        #for i in range(popSize):
        #    print(populationArray[i].ID, ' ', populationArray[i].array, ' ',populationArray[i].fit_value)
        #print()
        #breakpoint()


main()

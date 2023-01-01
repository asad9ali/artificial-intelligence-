#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math

class GA:
    def __init__(self, individualSize, populationSize):
        self.population=dict()
        self.individualSize = individualSize
        self.populationSize = populationSize
        self.totalFitness = 0
        i=0
        while i < populationSize:
            listofBits = [0] * individualSize
            listofLocations = list(range(0,individualSize))
            numberofOnes = random.randint(0, individualSize-1)
            onesLocations = random.sample(listofLocations,numberofOnes)
            for j in onesLocations:
                listofBits[j]=1
                self.population[i] = [listofBits,numberofOnes]
                self.totalFitness = self.totalFitness + numberofOnes
                i=i+1

    def updatePopulationFitness(self):
        self.totalFitness =0
        for individual in self.population:
            individualFitness=sum(self.population[individual] [0])
            self.population[individual] [1] = individualFitness
            self.totalFitness = self.totalFitness + individualFitness

    def selectParents(self):
        rouletteWheel = []
        wheelSize=self.populationSize*5
        h_n=[]
        for individual in self.population:
            h_n.append(self.population[individual][1])
        j=0
        for individual in self.population:
            individualLength=round(wheelSize*(h_n[j]/sum(h_n)))
            j=j+1
            if individualLength>0:
                i=0
                while i < individualLength:
                    rouletteWheel.append(individual)
                    i=i+1
        random.shuffle(rouletteWheel)
        parentIndices=[]
        i=0
        while i<self.populationSize:
            parentIndices.append(rouletteWheel[\
                                     random.randint(0, len(rouletteWheel)-1)])
            i=i+1
        newGeneration=dict()
        i=0
        while i< self.populationSize:
            newGeneration[i]=self.population[parentIndices[i]].copy()
            i=i+1
        del  self.population
        self.population=newGeneration.copy()
        self.updatePopulationFitness()

    def generateChildren(self,crossoverProbability):
        numberofPairs = round(crossoverProbability*self.populationSize/2)
        individualIndices= list(range(0,self.populationSize))
        random.shuffle(individualIndices)
        i=0
        j=0
        while i< numberofPairs:
            crossoverPoint=random.randint(0, self.individualSize-1)
            child1=self.population[j][0][0:crossoverPoint]\
                +self.population[j+1][0][crossoverPoint:]
            child2 = self.population[j+1][0][0:crossoverPoint] \
                     + self.population[j][0][crossoverPoint:]
            self.population[j]= [child1, sum(child1)]
            self.population[j+1]=[child2,sum(child2)]
            i=i+1
            j=j+2
        self.updatePopulationFitness()

    def mutateChildren(self,mutationProbability):
        numberOfBits = round(mutationProbability*\
                             self.populationSize*self.individualSize)
        totalIndices = list(range(0,\
                                  self.populationSize*self.individualSize))
        random.shuffle(totalIndices)
        swapLocations=random.sample(totalIndices,numberOfBits)

        for loc in swapLocations:
            individualIndex=math.floor(loc/self.individualSize)
            bitIndex=math.floor(loc % self.individualSize)

            if self.population[individualIndex][0][bitIndex]==0:
                self.population[individualIndex][0][bitIndex]=1
            else:
                self.population[individualIndex][0][bitIndex]=0
        self.updatePopulationFitness()




individualSize,populationSize=8,10
i=0
instance=GA(individualSize,populationSize)
while True:
    instance.selectParents()
    instance.generateChildren(0.8)
    instance.mutateChildren(0.03)
    print(instance.population)
    print(instance.totalFitness)
    print(i)
    i=i+1
    found=False
    for individual in instance.population:
        if instance.population[individual][1]==individualSize:
            found=True
            break
    if found:
        break


# In[ ]:





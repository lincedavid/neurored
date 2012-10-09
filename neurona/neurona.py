#!/usr/bin/python

import random
import numpy
import sys
import os
import shutil
import subprocess

class Perceptron:
    def __init__(self):
        pass

class Layer:
    def __init__(self, ID, neuronSize, learningRate, layerSize):
        self.id = ID
        self.size = layerSize
        self.neurons = list()

        for a in range(self.size):
            self.addNeuron(a, neuronSize, learningRate)    
        return

    def addNeuron(self, ID, neuronSize, learningRate):
        neuron = Neuron(ID, neuronSize, learningRate)
        self.neurons.append(neuron)
        return

    def setVector(self, vector):
        self.vector = vector
        return

    def getVector(self, size):
        return self.vector

    def train(self):
        for a, neuron in enumerate(self.neurons):
            neuron.train()
            neuron.printClassification()
        return

    def start(self, vector):
        self.setVector(vector)
        self.response = list()
        self.activation = list()

        for neuron in self.neurons:
            if(not os.path.exists("./" + str(neuron.id))):
                os.mkdir("./" + str(neuron.id))
            response, activation = neuron.start(self.vector)
            self.response.append(response)
            self.activation.append(activation)
            neuron.printOutput()
        print "Layer response >> %s\n" %(self.response)
        print "Layer activation >> %s\n" %(self.activation)
        print "[O] Finishing...\n"
        return
    

class Neuron:
    def __init__(self, ID, size, learningRate):
        self.id = ID
        self.size = size
        self.learningRate = learningRate
        self.weights = numpy.array(self.generateWeights(self.size + 1))
        print "Initial weights >> %s\n" %(self.weights)
        self.threshold = self.weights[-1]
        self.condition = numpy.array(self.generateWeights(self.size + 1))

    def generateWeights(self, size):
        weights = list()
        for i in range(size):
            weights.append(random.uniform(-1,1))
        return weights

    def setVector(self, vector):
        self.vector = numpy.array(vector)

    def getVector(self, size):
        return self.vector
            
    def calculateActivation(self, weights, vector):
        activation = numpy.dot(weights, vector)
        response = 0 if(activation < 0) else 1
        return activation, response

    def train(self):
        delta = [((self.expectedResponse - self.response) * a ) * self.learningRate for a in self.vector]
        self.weights = [a+b for a,b in zip(self.weights, delta)]
        print "New weights >> %s\n" %(self.weights)
        return

    def printOutput(self):
        if(self.response == 0):
            filename = "./" + str(self.id) + "/zeros.txt"
        else:
            filename = "./" + str(self.id) + "/ones.txt"
        with open(filename, "a") as outputFile:
            line = list(self.vector[:-1])
            line.append(self.response)
            outputFile.write(" ".join(str(a) for a in line) + "\n")
        return

    def printClassification(self):
        classification = str(self.response) + str(self.expectedResponse)

        if(classification == "00"):
            filename = "./" + str(self.id) + "/00.txt"
        elif(classification == "01"):
            filename = "./" + str(self.id) + "/01.txt"
        elif(classification == "10"):
            filename = "./" + str(self.id) + "/10.txt"
        elif(classification == "11"):
            filename = "./" + str(self.id) + "/11.txt"
        with open(filename, "a") as outputFile:
            line = list(self.vector[:-1])
            outputFile.write(" ".join(str(a) for a in line) + "\n")
        return
            
    def start(self, vector):
        self.setVector(vector)
        self.activation, self.response = self.calculateActivation(self.weights, self.vector)
        self.dump, self.expectedResponse = self.calculateActivation(self.condition, self.vector)
        return self.response, self.activation


def getInputs(filename):
    inputs = list()
    with open(filename, "r") as inputFile:
        for line in inputFile:
            line = [float(value.rstrip("\n")) for value in line.split(",")]
            inputs.append(line)
    return inputs

def generateInputs(size, quantity, filename):
    # "".join([(",".join([str(random.uniform(-1, 1)) for b in range(size)])) + "\n" for a in range(10)])
    with open(filename, "w") as inputFile:
        for a in range(quantity):
            inputData = [str(random.uniform(-1, 1)) for b in range(size)]
            inputData.append("-1")
            inputFile.write(",".join(str(a) for a in inputData) + "\n")
    return

def verifyInputFile(filename):
    return True

def main():
    neuronSize, threshold, learningRate = 0, 0, 0.0 
    vector = list()

    if(len(sys.argv) < 5):
        print "[!] Se esperan 4 parametros (tamano neurona, tasa de aprendizaje, tamano capa, nombre archivo de entradas)\n"

    try:
        neuronSize = int(sys.argv[1])
        print "[!] Using neuron size %d" % (neuronSize)
    except:
        print "[!] Using standar neuron size %s" % ("2")
        neuronSize = 2
        
    try:
        learningRate = float(sys.argv[2])
        print "[!] Using learning rate %f" % (learningRate)
    except:
        print "[!] Using standar learning rate %s" % ("0.1")
        learningRate = 0.5

    try:
        layerSize = int(sys.argv[3])
        print "[!] Using layer size %d" % (layerSize)
    except:
        print "[!] Using standar layer size %s" % ("1")
        layerSize = 2

    try:
        inputsFilename = sys.argv[4]
    except:
        inputFilename = "input.dat"

    finally:
        print "[!] Searching file %s" % (inputFilename)
        if(os.path.exists(inputFilename)):
            print "[O] %s found" % (inputFilename)
        else:
            print "[O] %s does not found" % (inputFilename)
            print "[O] Generating file %s" % (inputFilename)
            generateInputs(neuronSize, 5000, inputFilename)

        if(verifyInputFile(inputFilename)):
            print "[O] File format is correct"
        else:
            print "[X] Error, format error"
            return
        
        if(learningRate < 0.0 or learningRate > 1.0):
            print "[X] Error, learning rate out of range (0.0 - 1.0)\n"
            return

    raw_input("[O] Press any key to continue...\n")

    layer = Layer(0, neuronSize, learningRate, layerSize)
    #neuron = Neuron(1, neuronSize, learningRate)
    #condition = Neuron(1, neuronSize, learningRate)

    inputs = getInputs(inputFilename)

    for vector in inputs:
        layer.start(vector)
        layer.train()
        #condition.start(vector)
        #neuron.train(condition.response)
     
    for a in range(layerSize):
        lastPath = os.getcwd()
        dst = "./%d/" %(a)
        shutil.copy("./phase1.plot", dst)
        shutil.copy("./phase2.plot", dst)
        os.chdir(dst)
        subprocess.call(["gnuplot", "phase1.plot"])   
        subprocess.call(["gnuplot", "phase2.plot"])
        os.chdir(lastPath)

    #print "%s %s" % (condition.vector[0], condition.vector[1])
    #print "%s %s" % (neuron.weights[0], neuron.weights[1])
    
if(__name__ == "__main__"):
    main()

# [!] [?] [X] [O] >> <<

#!/usr/bin/python

import random
import sys
import os
import shutil
import subprocess
from NeuralNet import Net

def verifyConfigFile(filename):
    return True

def verifyInputFile(filename):
    return True

def getConfiguration(filename):
    mainConfiguration = dict()
    netConfiguration = list()
    with open(filename, "r") as myFile:
        for a, line in enumerate(myFile):
            variables = dict()
            line = [float(value.rstrip("\n")) for value in line.split(",")]
            variables["ID"] = a
            variables["layerSize"] = line[0]
            variables["neuronSize"] = line[1]
            variables["learningRate"] = line[2]
            if(a == 0):
                mainConfiguration = variables
            netConfiguration.append(variables)
    return mainConfiguration, netConfiguration

def getInputs(filename):
    inputs = list()
    with open(filename, "r") as inputFile:
        for line in inputFile:
            line = [float(value.rstrip("\n")) for value in line.split(",")]
            inputs.append(line)
    return inputs

def generateInputs(size, quantity, filename):
    # "".join([(",".join([str(random.uniform(-1, 1)) for b in range(size)])) + "\n" for a in range(10)])
    inputs = list()
    with open(filename, "w") as inputFile:
        for a in range(quantity):
            inputData = [str(random.uniform(-1, 1)) for b in range(size)]
            inputData.append("-1")
            inputFile.write(",".join(str(a) for a in inputData) + "\n")
            inputs.append(inputData)
    return inputs

def netDirectoryTree(netConfiguration):
    netTree = list()
    netPath = "./net/"
    if(os.path.exists(netPath)):
        shutil.rmtree(netPath)
    os.mkdir(netPath)
    for a, config in enumerate(netConfiguration):
        layerTree = list()
        layerPath = netPath + "L" + str(a) + "/"
        os.mkdir(layerPath)
        for b in range(int(config["layerSize"])):
            neuronPath = layerPath + "N" + str(b) + "/"
            os.mkdir(neuronPath)
            layerTree.append(neuronPath)
        netTree.append(layerTree)
    return netTree

def printNetOutput(net, tree):
    for a, layer in enumerate(net.layers):
        for b, neuron in enumerate(layer.neurons):
            path = tree[a][b]
            if(neuron.response == 0):
                filename = path + "zeros.txt"
            else:
                filename = path + "ones.txt"
            with open(filename, "a") as outputFile:
                line = list(neuron.vector[:-1])
                line.append(neuron.response)
                outputFile.write(" ".join(str(a) for a in line) + "\n")
    
            classification = str(neuron.response) + str(neuron.expectedResponse) 
            if(classification == "00"):
                filename = path + "00.txt"
            elif(classification == "01"):
                filename = path + "01.txt"
            elif(classification == "10"):
                filename = path + "10.txt"
            elif(classification == "11"):
                filename = path + "11.txt"
            with open(filename, "a") as outputFile:
                line = list(neuron.vector[:-1])
                line.append(neuron.response)
                line.append(neuron.expectedResponse)
                outputFile.write(" ".join(str(a) for a in line) + "\n")
    
            with open(path + "weights.txt", "w") as outputFile:
                line = neuron.weights
                outputFile.write(" ".join(str(a) for a in line))

    #lastPath = os.getcwd()
    #dst = path
    #shutil.copy("./phase1.plot", dst)
    #shutil.copy("./phase2.plot", dst)
    #os.chdir(dst)
    #subprocess.call(["gnuplot", "phase1.plot"])   
    #subprocess.call(["gnuplot", "phase2.plot"])
    #os.chdir(lastPath)
    return
    

def main():
    configurationFilename = 0

    if(len(sys.argv) < 4):
        print "[!] 3 argument expected (Net configuration filename, train data filename, test data filename)\n"

    try:
        configurationFilename = sys.argv[1]
        print "[!] Net configuration filename >> %s" % (configurationFilename)
    except:
        print "[X] Error, first argument expected (Net configuration filename not given)\n"
        return
        
    try:
        inputFilename = sys.argv[2]
    except:
        print "[!] Input filename not given, using default [input.dat]\n"
        inputFilename = "input.dat"

    try:
        testFilename = sys.argv[3]
    except:
        print "[!] Test data filename not given\n"
        return

    if(configurationFilename):
        if(verifyConfigFile):
            mainConfiguration, netConfiguration = getConfiguration(configurationFilename)
            print "[!] Searching file %s" % (inputFilename)
            if(os.path.exists(inputFilename)):
                print "[O] %s found" % (inputFilename)
            else:
                print "[O] %s does not found" % (inputFilename)
                print "[O] Generating file %s [5000 inputs]" % (inputFilename)
                generateInputs(int(mainConfiguration["neuronSize"]), 5000, inputFilename)

            if(verifyInputFile(inputFilename)):
                print "[O] File format is correct"
            else:
                print "[X] Error, file format error"
                return
        else:
            print "[X] Error, bad configuration file"
            return

    raw_input("[O] Press any key to continue...\n")

    print mainConfiguration
    print netConfiguration

    net = Net(netConfiguration)
    netDirTree = netDirectoryTree(netConfiguration)
    print netDirTree
    raw_input("[O] Press any key to continue...\n")

    inputs = getInputs(inputFilename)
    #for input in inputs:
    #    print input
    for vector in inputs:
        net.start(vector)
        printNetOutput(net, netDirTree)
        net.train()

    raw_input("Termino entrenamiento!\n\n")
    
    with open(testFilename) as inputFile:
        vectors = list()
        for line in inputFile:
            line = [float(value.rstrip("\n")) for value in line.split(",")]
            vectors.append(line)
    print vectors
    inputs.append(vector)
    
    for vector in vectors:
        net.start(vector)
        #net.printOutput()

if(__name__ == "__main__"):
    main()

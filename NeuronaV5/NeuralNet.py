#!/usr/bin/python

import random
import numpy
import time
from math import exp

DEBUG = 1
magicNumber = 10

class Net:
    def __init__(self, configuration):
        self.layers = list()
        self.inputs = list()
        self.responses = list()
        self.epoch = 0
        self.configuration = configuration
        self.size = len(self.configuration)

        for a, config in enumerate(self.configuration):
            self.addLayer(a, config["layerSize"], config["neuronSize"], config["learningRate"])
        return

    def addLayer(self, ID, layerSize, neuronSize, learningRate):
        layer = Layer(ID, layerSize, neuronSize, learningRate)
        self.layers.append(layer)
        return

    def setVector(self, vector):
        self.vector = vector
        return

    def train(self):
        for layer in self.layers:
            layer.train()
        return

    def start(self, vector):
        #tInput = list()
        #tInput.append(vector)
        layerInput = vector
        self.setVector(vector)
        self.inputs.append(vector[:-2])
        for layer in self.layers:
            #if DEBUG: print self.inputs
            #if DEBUG: print "Input Layer %d >> %s" %(layer.id, tInput[-1])
            #tInput.append(layer.start(tInput[-1]))
            #tInput[-1].append(-1)
            #tInput[-1].append(self.vector[-1])
            #if DEBUG: print "Ouput Layer %d >> %s" %(layer.id, tInput[-1])

            if DEBUG: print "Input Layer %d >> %s" %(layer.id, layerInput)
            layerInput = layer.start(layerInput)
            layerInput.append(-1)
            layerInput.append(self.vector[-1])
            if DEBUG: print "Ouput Layer %d >> %s" %(layer.id, layerInput)

        self.output = layerInput
        self.responses.append(self.output)
        if DEBUG: print "[O] Finishing net"
        if DEBUG: print "Input Net >> %s" % (self.vector)
        if DEBUG: print "Response Net >> %s\n\n" % (self.output)
        return


class Layer:
    def __init__(self, ID, layerSize, neuronSize, learningRate):
        self.id = ID
        self.size = int(layerSize)
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

    def train(self):
        for a, neuron in enumerate(self.neurons):
            neuron.train()
        return

    def start(self, vector):
        self.setVector(vector)
        self.response = list()
        self.activation = list()
        for neuron in self.neurons:
            if DEBUG: print "Input Neuron %d >> %s" %(neuron.id, self.vector)
            response, activation = neuron.start(self.vector)
            self.response.append(response)
            self.activation.append(activation)
            if DEBUG: print "Response Neuron %d >> %s" %(neuron.id, response)
            if DEBUG: print "Activation Neuron %d >> %s" %(neuron.id, activation)
        if DEBUG: print "Response Layer %d >> %s" % (self.id, self.response)
        if DEBUG: print "Activation Layer %d >> %s" % (self.id, self.activation)
        if DEBUG: print "[O] Finishing layer..."
        return self.response
    

class Neuron:
    def __init__(self, ID, size, learningRate):
        self.id = ID
        self.size = int(size)
        self.learningRate = learningRate
        self.vMomentum = 0.1
        self.lastDelta = [0 for a in range(self.size + 1)]
        self.weights = numpy.array(self.generateWeights(self.size + 1))
        self.threshold = self.weights[-1]
        self.condition = numpy.array(self.generateWeights(self.size + 1))
        self.ones = 0
        self.zeros = 0
        print "Initial weights >> %s\n" %(self.weights)

    def setVector(self, vector):
        self.vector = numpy.array(vector)

    def generateWeights(self, size):
        weights = [random.uniform(-1,1) for a in range(size)]
        return weights

    def calculateActivation(self, weights, vector):
        if DEBUG: print "Weights Neuron %d >> %s" %(self.id, weights)
        if DEBUG: print "  Input Neuron %d >> %s" %(self.id, vector)
        activation = numpy.dot(weights, vector)
        #if(activation < 0):
        #    self.zeros += 1
        #    output = 0
        #else:
        #    self.ones += 1
        #    output = 1
        output = 1 / (1 + exp(activation))
        return activation, output

    def momentum(self, delta):
        deltaM = [d*self.vMomentum for d in self.lastDelta]
        self.weights = [a+b for a,b in zip(self.weights, deltaM)]
        self.lastDelta = delta
        if DEBUG: print "New weights + momentum >> %s" %(self.weights)
        pass

    #def update(self):
    #    global magicNumber
    #    lastLearning = self.learningRate
    #    lastMomentum = self.vMomentum

    #    if(self.ones%magicNumber == 0):
    #        if(self.learningRate >= 0.1):
    #            self.learningRate -= 0.05
    #        if(self.vMomentum >= 0.1):
    #            self.vMomentum -= 0.05

    #        if DEBUG: print "Updating learning rate >> %f" %(self.learningRate)
    #        if DEBUG: print "Updating momentum >> %f" %(self.vMomentum)
    #    if(self.zeros%magicNumber == 0):
    #        if(self.learningRate <= 1.0):
    #            self.learningRate += 0.05
    #        if(self.vMomentum <= 1.0):
    #            self.vMomentum += 0.05
    #        if DEBUG: print "Updating learning rate >> %f" %(self.learningRate)
    #        if DEBUG: print "Updating momentum >> %f" %(self.vMomentum)

    #    return


    def train(self):
        delta = [((self.expectedResponse - self.response) * a ) * self.learningRate for a in self.vector]
        self.weights = [a+b for a,b in zip(self.weights, delta)]
        if DEBUG: print "New weights >> %s" %(self.weights)
        self.momentum(delta)
        #self.update()
        #time.sleep(0.2)
        return

    def start(self, vector):
        self.expectedResponse = float(vector[-1])
        self.setVector(vector[:-1])
        #self.setVector(vector)
        self.activation, self.response = self.calculateActivation(self.weights, self.vector)
        #self.dump, self.expectedResponse = self.calculateActivation(self.condition, self.vector)
        if DEBUG: print "Respuesta >> %f ---- Esperada >> %f" %(self.response, self.expectedResponse)
        return self.response, self.activation


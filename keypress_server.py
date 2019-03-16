# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:28:39 2019

@author: Dave Lei
"""

import time
import zmq
from joblib import load
import numpy as np

NN_left_clf = load("NN_left_clf_relative_to_screen.joblib")

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)
    
    features = np.random.random((1,18))
    
    prediction = NN_left_clf.predict(features)
    #  Do some 'work'.
    #  Try reducing sleep time to 0.01 to see how blazingly fast it communicates
    #  In the real world usage, you just need to replace time.sleep() with
    #  whatever work you want python to do, maybe a machine learning task?

    #  Send reply back to client
    #  In the real world usage, after you finish your work, send your output here
    sendMessage = "Prediction: {}".format(prediction)
    socket.send(str.encode(sendMessage))
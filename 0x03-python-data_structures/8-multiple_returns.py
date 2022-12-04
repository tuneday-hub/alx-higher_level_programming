#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = ()
    if sentence == "":
        tuple = (len(sentence), None)
    else:
        tuple = (len(sentence), sentence[0])

import json  
import os

class Signals():

    signal_index = {
        0: 'RIP',
        1: 'SVC',
        2: 'HRA',
        3: 'MRA',
        4: 'LRA',
        5: 'RV',
        6: 'RVW',
        14: 'IVC',
        16: 'PA'
    }

    def __init__(self): #allows retrieval of signal from JSON file 
        json_file = os.path.abspath('guiserver/signals.json')

        with open(json_file) as f:
            self.ecg_signals = json.load(f)

    def get_signal(self, location, rate, version=0):  #location is the sensor, rate is the input hR, version 0 or 1 is possible
        signal = self.ecg_signals[location][version] #get x and y vector of selected signal from JSON file

        x = signal['x'] #get x and y vectors from JSON file
        y = signal['y']

        y[-1] = y[0] #set last value to be equal to first value
        time_beat = x[-1] - x[0] #elapsed time of one cycle
        r = 1 / (rate/60) #period of input heart rate 

        if r > time_beat: # case: period of input HR > period of o.g. signal
            x.append(x[0] + r)
            x = [xx - x[0] for xx in x] #start time at 0
            y.append(y[-1]) # add 31st value extending last y value of the cycle to flat line until correct period
        elif r <= time_beat: #case: period of input HR <= period of o.g. signal
            length = x[-1] - x[0]
            d = r / length #scale factor
            x.append(x[0])
            x = [xx * d for xx in x] #multiply by scale factor (<1) to get shorter period
            x = [xx - x[0] for xx in x] #start time at 0

        return x, y

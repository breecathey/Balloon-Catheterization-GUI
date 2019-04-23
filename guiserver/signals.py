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

    def __init__(self):
        json_file = os.path.abspath('guiserver/signals.json')

        with open(json_file) as f:
            self.ecg_signals = json.load(f)

    def get_signal(self, location, rate, version=0):
        signal = self.ecg_signals[location][version]

        x = signal['x']
        y = signal['y']

        # d = 60 / (rate * (xx[29]-xx[0]))
        # new_first = xx[0] * d

        # xx = [(w * d) - new_first for w in xx]

        y[-1] = y[0]
        time_beat = x[-1] - x[0]
        r = 1 / (rate/60)

        if r > time_beat:
            x.append(x[0] + r)
            x = [xx - x[0] for xx in x]
            y.append(y[-1])
        elif r < time_beat:
            length = x[-1] - x[0]
            d = r / length
            x = [xx * d for xx in x]
            x = [xx - x[0] for xx in x]

        return x, y

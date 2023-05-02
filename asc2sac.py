from obspy import Trace
import numpy as np


with open('./19990817000139_1404_mp_Acc_N.asc') as f:
    lines = f.readlines()

removed = []
[removed.append(x.replace('\n','')) for x in lines[64:]]


tr = Trace(data=np.array(removed))
tr.stats.delta = 1.0

tr.plot()

tr.write("out.sac", format="SAC")  
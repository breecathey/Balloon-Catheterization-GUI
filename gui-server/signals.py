def High_RA_V1(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[248.1661527, 250.4494045, 253.1039662, 254.1037761, 256.2452385, 260.1088337, 262.6047185, 264.7813772, 268.1228094, 271.6357545, 276.1210838, 281.0137051, 285.8602758, 290.1010252, 296.8946127, 302.9276547, 307.7097546, 312.534835, 317.3752657, 322.2279765, 325.2263828, 331.8689272, 336.7001477, 341.5835589, 346.4915305, 351.402572, 356.1816019, 360.8961608, 365.6168599, 369.7747182]
    y=[-0.418918919, -0.546448186, -1.011508166, -1.274533892, -3.054054054, -2.256756757, -2.002619598, -1.556619454, -1.018369707, -0.568049333, -0.264362625, -0.207183119, -0.207183119, -0.207183119, -2.581081081, -0.077576239, -0.157627547, -0.184311317, -0.191935251, -0.184311317, -0.222430987, -0.249114756, -0.268174592, -0.222430987, -0.146191646, -0.066140338, -0.150003613, -0.313918196, -0.470208845, -0.573131955]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))

    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)

    return xx, y

#High_RA_V1(rate)

def High_RA_V2(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[132.5557773,  138.1570833, 148.8873455, 152.1988959, 155.4776993, 159.1781215, 162.8457967, 165.8769501, 173.6042082, 178.8181944, 182.3630679, 185.9611555, 189.6083637, 193.2555719, 196.9027801, 200.5377081, 204.1398891, 207.762537, 211.3933716, 215.0282997, 218.6673211, 222.3472764, 226.1131928, 229.8136151, 233.4649167, 237.0343505, 240.553845, 244.034043, 247.5543562, 249.9448945]
    y=[-0.635135135, -3.013513514, -1.030568001, -0.679867033, -0.369827046, -0.288505083, -0.247844101, -0.245302789, -3, 0.026617527, -0.085200173, -0.130943778, -0.11569591, -0.100448042, -0.085200173,-0.085200173, -0.125861155, -0.141109023, -0.146191646, -0.146191646, -0.141109023, -0.085200173, 0.077443754, 0.158765718, 0.179096209, 0.097774245, -0.045555716, -0.237678855, -0.379992292, -0.420653274]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#High_RA_V2(rate)

def IVC_V1(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[121.1171552, 130.3141999, 140.0716788, 145.5704014, 151.069124, 156.5678465, 162.0623754, 167.5454798, 171.632935, 174.3426726, 179.6378988, 186.5215326, 190.2995536, 195.0542769, 200.5616762, 206.0603988, 211.5589767, 217.0533609, 222.5439852, 228.0390925, 233.5378151, 239.0401529, 244.5388755, 248.2373825, 251.9214572, 257.4117923, 262.3446354, 267.3061379, 272.5963746, 275.7095349]
    y=[0.161281156, -0.739181619, 0.028748448, 0.026622653, 0.024496858, 0.022371064, 0.030231624, 0.065296392, 0.150824384, 0.244115323, 0.30876025, 0.231985398, 0.119231386, 0.018509926, -0.004277293, -0.006403088, -0.008184525, 2.03919E-05, 0.017178593, 0.023661725, 0.02153593, 0.010801208, 0.008675414, 0.085264221, 0.196219864, 0.214066779, 0.156758566, 0.031205043, 0.057975207, 0.125737836]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#IVC_V1(rate)

def IVC_V2(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[121.7536738, 129.0866282, 136.9261996, 142.4302988, 147.9206339, 153.4176211, 164.412897, 169.6970667, 174.9483072, 180.4334362, 184.9628414, 189.5276925, 195.0487817, 200.5495288, 206.0482514, 211.5469739, 217.0503241, 222.5539635, 233.5540116, 239.0482512, 244.5309219, 248.2483151, 251.5314871, 256.6198975, 260.771705, 263.7799794, 268.5396773, 272.6420275, 274.7503965, 278.6035561]
    y=[0.145571162, -0.81602663, 0.015994154, 0.023016394, 0.040863309, 0.042869799, 0.043783566, 0.085000833, 0.204630854, 0.234874623, 0.203131108, 0.086981849, 0.031595495, 0.024648701, 0.022522906, 0.020397111, 0.00725189, -0.006582045, -0.017032062, -0.008482787, 0.027615052, 0.059230827, 0.189714137, 0.229522175, 0.161811272, 0.011772458, -0.100794884, -0.050735671, 0.071881204, 0.146788991]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#IVC_V2(rate)

def Mid_RA_V1(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[176.7895033, 183.2087646, 185.0898541, 191.3999976, 195.1080071, 198.8053996, 202.4390897, 206.0276573, 209.5949908, 212.561133, 217.8339757, 225.4206903, 228.538487, 232.1164375, 235.7129679, 239.3280782, 242.9272628, 246.4866335, 250.0460042, 253.6239547, 257.209868, 259.6093244, 266.8315822, 275.2296797, 278.725348, 282.1732395, 285.6264395, 289.114145, 292.6283931, 296.1559126]
    y=[0.142337505, -4.420343827, 2.224267094, -0.454506131, -0.165921063, 0.102093443, 0.246684582, 0.303850835, 0.319875966, 0.320373641, -2.333997315, 0.365262201, 0.24592148, 0.282517173, 0.355111347, 0.463704003, 0.541440818, 0.542038028, 0.542635237, 0.57923093, 0.631254543, 0.683079086, 0.884836478, 1.066222378, 0.943396221, 0.728002537, 0.522894134, 0.384640056, 0.29781238, 0.236697906]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#Mid_RA_V1(rate)

def Mid_RA_V2(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[50.27151085, 53.43783831, 58.29472134, 59.71506517, 62.78785779, 66.21287026, 71.14184217, 76.02502798, 80.22606745, 84.45676179, 89.74667648, 94.87030702, 100.437362, 102.2584657, 107.0859119, 111.881507, 116.6711299, 121.4408459, 126.1946362, 130.952408, 135.728096, 140.5256817, 145.2993791, 150.0053926, 154.6258061, 159.2362661, 163.9124192, 168.4087457, 173.3523161, 178.1479112]
    y=[0.013727103, 0.148486554, 1.558697441, -3.689386394, -0.735850691, -0.506363852, -0.15072539, 0.116202526, 0.210752456, 0.247650803, -2.503139479, 0.423894687, 0.210063656, 0.37514276, 0.53407523, 0.631296015, 0.71694586, 0.764025903, 0.780250104, 0.804188265, 0.862839248, 0.963917014, 1.018711017, 0.942367692, 0.700174217, 0.438695841, 0.304497813, 0.204979428, 0.205808886, 0.303029672]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#Mid_RA_V2(rate)

def Low_RA_V1(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[160.6864489, 170.1589852, 178.4067352, 182.2066014, 186.1153223, 189.3792884, 195.7619239, 204.6742811, 215.0146358, 220.292347, 224.1742729, 228.0595481, 231.9649196, 235.8970861, 239.8459995, 243.7982623, 247.77732, 251.7932209, 255.8158205, 259.8518177, 263.8576704, 267.7998851, 271.7153047, 275.5938812, 279.5026021, 287.3736338, 291.3225472, 299.1868802, 307.0780082, 310.3687694]
    y=[0.557251908, 1.809160305, -0.003751438, 0.244039527, 0.310859563, 0.355406253, 1.244274809, -2.572519084, 0.236641221, 0.388816271, 0.500182997, 0.605981387, 0.678369758, 0.70621144, 0.70621144, 0.700643104, 0.650528077, 0.539161351, 0.416657953, 0.271881209, 0.177219492, 0.188356164, 0.244039527, 0.36097459, 0.427794625, 0.472341315, 0.472341315, 0.528024678, 0.539161351, 0.539161351]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#Low_RA_V1(rate)

def Low_RA_V2(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[158.2896172, 170.1314355, 178.4285062, 182.2400952, 186.122021, 190.0441394, 195.2798026, 204.1921598, 216.3970236, 220.2622026, 224.1642247, 228.0829937, 232.0017627, 235.9037849, 239.8292526, 243.7748166, 247.7304288, 251.7161853, 255.722038, 259.7379389, 263.7873335, 267.746295, 271.6583653, 275.5503393, 279.4691083, 287.3367907, 295.2312681, 303.1089986, 307.057912, 311.0068253]
    y=[0.541984733, 1.854961832, -0.039945624, 0.188356164, 0.29972289, 0.344269581, 1.045801527, -2.770992366, 0.29972289, 0.438931298, 0.516888006, 0.567003033, 0.617118059, 0.695074767, 0.734053121, 0.739621458, 0.728484785, 0.667233086, 0.572571369, 0.461204643, 0.294154554, 0.277449545, 0.338701244, 0.433362961, 0.483477988, 0.533593015, 0.539161351, 0.572571369, 0.572571369, 0.572571369]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)

    return xx, y

#Low_RA_V2(rate)

def PA_V1(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[66.12771383, 71.37725449, 75.09692902, 83.89859571, 89.01565065, 94.14245952, 104.4127715, 109.5535547, 114.6961199, 119.8444061, 124.9819068, 130.1089032, 134.9910013, 139.8649774, 144.9911297, 155.2499996, 165.5092446, 170.6470266, 174.3972764, 176.9833837, 179.8053295, 182.1635421, 185.6830649, 190.5777962, 193.2963348, 194.7101276, 196.7860425, 199.7931376, 204.2079105, 209.1671979]
    y=[-0.233754546, 0.793955529, -1.152124189, -0.210052371, -0.135875708, -0.119247155, -0.184485854, -0.250306036, -0.326639816, -0.436727776, -0.483180806, -0.467658948, -0.382909601, -0.250240385, -0.229738402, -0.22746874, -0.227412468, -0.275525539, -0.391235132, -0.516867772, -0.658274559, -0.815001561, -0.94509443, -0.934880954, -0.741320097, -0.553526244, -0.420369332, -0.27848454, -0.18786221, -0.166710413]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#PA_V1(rate)

def PA_V2(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[65.45877236, 70.69931381, 75.09692902, 82.01811136, 86.66514422, 102.0511981, 107.188136, 112.3827429, 116.7801404, 121.2326511, 126.3716524, 131.5004308, 136.15183, 140.7959137, 151.0511259, 161.3103709, 166.4429946, 171.5810579, 176.4986734, 180.0165455, 181.9912542, 185.2012777, 189.8734977, 193.493589, 193.5629169, 194.0034375, 196.0700331, 200.0144765, 203.5053237, 207.1393753]
    y=[-0.286999888, 0.793805542, -1.152124189, -0.120576855, -0.024615402, -0.007930576, -0.051063523, -0.128738466, -0.241305938, -0.373336694, -0.42864328, -0.423635018, -0.353434952, -0.240073802, -0.216223599, -0.216167327, -0.233846301, -0.283619415, -0.408422659, -0.528776617, -0.7156179, -0.853895306, -0.906538322, -0.804581752, -0.663346909, -0.511073257, -0.322932077, -0.208711207, -0.169618164, -0.202557276]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#PA_V2(rate)

def RV_V1(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[73.03320948, 85.94371958, 93.03608975, 94.79769295, 97.26360154, 101.3526517, 106.7221097, 111.9155572, 119.6359342, 132.8782511, 140.51672, 145.0265659, 148.2889931, 152.9101501, 158.3009644, 163.6209906, 168.9474958, 174.309515, 179.5146005, 184.130645, 188.9514951, 194.3672653, 199.5049821, 203.359206, 206.1843371, 210.2860709, 215.3188109, 220.3437412, 225.7537523, 229.2788201]
    y=[-0.037731501, -6.178691783, 0.207552061, 0.344113252, 0.48044642, 0.553694543, 0.560995316, 0.518059779, 0.650306748, 1.966012846, 0.458020104, 0.306273824, 0.185901665, 0.064731688, 0.037061337, 0.125306512, 0.202942469, 0.222424196, 0.160431361, 0.047633061, -0.062081007, -0.130616493, -0.082293111, 0.037029628, 0.149224922, 0.201703677, 0.083473358, -0.021968746, -0.081073816, -0.099664693]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#RV_V1(rate)

def RV_V2(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[72.41337596, 85.40683775, 93.08217403, 96.85004816, 98.69651795, 102.5640882, 107.9364256, 112.9590219, 115.88665, 120.237334, 135.4774043, 143.6403154, 147.4399091, 152.8369624, 158.2011412, 163.5190078, 168.8740681, 174.2888784, 179.7173664, 185.1302571, 190.5640242, 195.9490795, 200.6467103, 204.4957104, 209.0009668, 212.7248012, 215.3489118, 219.5283582, 224.9076545, 228.6276295]
    y=[-0.022754112, -6.299547798, 0.132089058, 0.345351944, 0.503219523, 0.600687648, 0.603273213, 0.501653286, 0.446009634, 0.66551456, 1.709899479, 0.352136804, 0.22246319, 0.184576555, 0.200521876, 0.292303456, 0.323180269, 0.256216519, 0.166855532, 0.103035253, 0.005029718, -0.013210217, 0.078847317, 0.206724167, 0.275341306, 0.156905703, 0.034183106, -0.040592617, -0.049402137, -0.048700255]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#RV_V2(rate)

def RV_Wall_V1(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[153.3738284, 157.0854061, 161.5803529, 170.0337347, 174.0535014, 178.0816613, 182.1118728, 186.1465607, 190.1812486, 194.2159365, 198.2506244, 202.2853123, 206.3270877, 209.1107588, 218.2091428, 221.4896209, 224.5503286, 226.4531525, 229.6548653, 233.6944026, 237.7341264, 241.7809378, 245.0843385, 246.8877127, 249.6151228, 254.0019462, 258.0368206, 262.0759849, 264.8592829, 270.1837985]
    y=[-0.272189349, 2, -5.047337278, 5.124768706, 5.18799722, 5.215659694, 5.234628248, 5.234628248, 5.234628248, 5.234628248, 5.234628248, 5.234628248, 5.204594704, 5.162969266, 0.98816568, 0.792825196, 0.645818903, 0.489960618, 0.386581999, 0.366032732, 0.344693109, 0.293319942, 0.186463755, 0.024598761, -0.094674556, -0.20223353, -0.203023886, -0.22199244, -0.262037165, -0.25443787]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)

    return xx, y

#RV_Wall_V1(rate)

def RV_Wall_V2(rate):
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[149.1302299, 154.9615123, 161.64319, 171.5275316, 175.5424489, 179.5674381, 183.5965305, 187.6300993, 191.6700096, 195.7065627, 199.7427427, 203.7774306, 207.8218173, 210.353196, 218.9087291, 220.3707389, 223.944075, 224.6897418, 227.6347237, 231.6888091, 235.7236835, 239.7583714, 243.7934323, 247.8417358, 251.1468152, 253.4541523, 256.2656762, 260.0696453, 264.1183218, 266.9059719]
    y=[-0.289940828, 2, -5.313609467, 5.206175417, 5.289953197, 5.331051731, 5.354762423, 5.359504562, 5.337374582, 5.329471018, 5.323148166, 5.323148166, 5.282049633, 5.240951099, 1.023668639, 0.828402367, 0.686390533, 0.526627219, 0.398437345, 0.316240278, 0.315449922, 0.315449922, 0.313869209, 0.256173191, 0.142203796, -0.018080485, -0.177732481, -0.268623469, -0.3279002, -0.386386575]
    xx=[]
    yy=[]
    for item in x:
        xx.append(float(item))
    for item in y:
        yy.append(float(item))
    r=1/(rate/60)
    lens=xx[29]-xx[0]
    d=r/lens
    xx=[w * d for w in xx]
    xx=[w-xx[0] for w in xx]
    y.pop(29)
    y.append(y[0])
    z=xx[29]-xx[0]
    xxx=[w + z for w in xx]
    xx.extend(xxx)
    y.extend(y)
    
    return xx, y

#RV_Wall_V2(rate)

def Default_Line():
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    return x,y

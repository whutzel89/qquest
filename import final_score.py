import final_score.final_score as fs
from final_score.variables import GRAPH, LR, SHOTS
import matplotlib.pyplot as plt
import numpy as np
base_score=[]
balanced_score=[]
connected_score=[]
coefs=np.arange(0.1,1,0.1)
for coef in coefs:
    XS_brut, XS_balanced, XS_connected = fs.get_classical_brute_force_scores(GRAPH)
    ansatz = fs.build_ansatz(GRAPH)
    counts = fs.get_counts(SHOTS, ansatz, GRAPH, coef, LR)
    base_score.append(fs.final_score(GRAPH, XS_brut, counts, SHOTS, ansatz))
    balanced_score.append(fs.final_score(GRAPH, XS_balanced, counts, SHOTS, ansatz))
    connected_score.append(fs.final_score(GRAPH, XS_connected, counts, SHOTS, ansatz))
    print("Base score: " + str(fs.final_score(GRAPH, XS_brut, counts, SHOTS, ansatz)))
    print("Balanced score: " + str(fs.final_score(GRAPH, XS_balanced, counts, SHOTS, ansatz)))
    print("Connected score: " + str(fs.final_score(GRAPH, XS_connected, counts, SHOTS, ansatz)))
fig = plt.figure() 
plt.plot(coefs,base_score,label='base_score')
plt.plot(coefs,balanced_score,label='balanced_score')
plt.plot(coefs,connected_score,label='connected_score')
plt.ylabel('Score')
plt.ylabel('Coefficent value')
plt.legend()
plt.show()
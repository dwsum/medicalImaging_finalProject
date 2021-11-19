fat_color = 0.7747169032417183
muscle_color = 0.46249658372820346
nerve_color = 0.6783725593150846
tumor_color = 0.5652088003382723

overallSNR = 3.54

print("Muscle and Tumor CNR:",abs(muscle_color * overallSNR-tumor_color* overallSNR))
print("Muscle and Nerve CNR:",abs(muscle_color* overallSNR-nerve_color* overallSNR))
print("Nerve and Tumor CNR:",abs(nerve_color* overallSNR-tumor_color* overallSNR))

overallSNR = 20.94

print("Muscle and Tumor CNR:",abs(muscle_color * overallSNR-tumor_color* overallSNR))
print("Muscle and Nerve CNR:",abs(muscle_color* overallSNR-nerve_color* overallSNR))
print("Nerve and Tumor CNR:",abs(nerve_color* overallSNR-tumor_color* overallSNR))
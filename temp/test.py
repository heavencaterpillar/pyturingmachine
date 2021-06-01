tape = [" "]*27
tap = dict() #лента эмулятора
for i in range(-13, len(tape)//2 + 1):
    tap[i] = tape[i+13]
print(tap)
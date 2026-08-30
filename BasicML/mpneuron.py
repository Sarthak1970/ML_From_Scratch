class MPNeuron:
    noofinputs=0

    def __init__(self,inputs,threshold):
        self.inputs=inputs
        self.threshold=threshold

    def summation(self):
        return sum(self.inputs)

    def func(self):
        if(self.summation()>=self.threshold):
            return 1
        else:
            return 0

n = int(input("Enter number of inputs: "))
inputs = []

for i in range(n):
    inputs.append(int(input(f"Enter input {i} (0 or 1): ")))

thresh=int(input(f"Enter Threshold value:"))


MPN=MPNeuron(inputs,thresh)
print(MPN.func())
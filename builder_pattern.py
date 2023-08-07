class Computer:
    def __init__(self, cpu=None, ram=None, ssd=None, gpu=None):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.gpu = gpu

    def __str__(self):
        return f"Computer with CPU:{self.cpu}, RAM:{self.ram}, ssd:{self.ssd}, GPU:{self.gpu}"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu

    def set_ram(self, ram):
        self.computer.ram = ram

    def set_ssd(self, ssd):
        self.computer.ssd = ssd

    def set_gpu(self, gpu):
        self.computer.gpu = gpu

    def get_computer(self):
        return self.computer


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_computer(self):
        self.builder.set_cpu("Intel Core i8")
        self.builder.set_ram("16GB")
        self.builder.set_ssd("256GB")
        self.builder.set_gpu("Nvidia GTX 1660")


if __name__ == "__main__":
    builder = ComputerBuilder()
    director = Director(builder)
    director.build_computer()
    computer = builder.get_computer()
    print(computer) # Output: Computer with CPU:Intel Core i8, RAM:16GB, ssd:256GB, GPU:Nvidia GTX 1660


class Data:
    #Dictionary mapping location to current lines
    lines = {} 

    #Constructor method
    def __init__():

    #Getter method for lines
    def getLines(self, address):
        return Data.lines[address]

    #Setting method for lines
    def setLines(self, address, queue, eta):
        Data.lines[address] = [queue, eta]

    
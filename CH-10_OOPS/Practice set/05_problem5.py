# Write a class Train which has method to book
# a ticket, get status (no of seats) and get
# fare information of train running under 
# indian railway

from random import randint
class Train:
    def book(self, trainNo, fro, to):
        print(f"Ticket is booked in train no: {trainNo} from : {fro} to : {to}")
    def getStatus(self, trainNo):
        print(f"Trin no: {trainNo} is running on time")
    def getFare(self, trainNo, fro, to):
        print(f" Ticket fare in train no: {trainNo} from {fro} to {to} is : {randint(2222,555555)}")

t = Train()
Train.book("Anand Vihar", "Deli")
class employee():
    company = "ITC"
    def info(self):
        print(f"Name of employee is {self.name} and the sallary {self.sallary}")


class programmer():
    company = "ITC infotech"
    def lang(self):
        print(f"Name of employee is {self.name} and her/his language {self.language} is good")

a = employee()
b = programmer()

print(a.company, b.company)
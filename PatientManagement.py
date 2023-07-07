class Hospital:
    '''
    Patient Management System
    '''
    def __init__(self,action):
        self.action = action

    def PatientMgmt(self):
        if self.action == "insert":
            pid = input("Enter PID : ")
            pname = input("Enter Patient Name : ")
            padd = input("Enter Patient Address : ")
            pdf = open("patient.data","a")
            pdf.write(pid + ":" + pname + ":" + padd)
            pdf.write("\n")
            pdf.close()
        if self.action == "delete":
            pid = input("Enter PID : ")
            pdf = open("patient.data","r+")
            pd = pdf.readlines()
            print(pd)
            pdf.seek(0)
            pdf.truncate()

            for data in pd:
                s1 = data.find(pid)
                if s1 != 0:
                    pdf.write(data)
                    pdf.close()

 

action = "start"
while action != "stop":
    action = input("Please enter your action or use stop to quit")
    hosp = Hospital(action)
    hosp.PatientMgmt()
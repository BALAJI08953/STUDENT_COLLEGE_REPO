class Student():
    def __init__(self,id,name,age,cgpa,branch):
        self.id=id
        self.name=name
        self.age=age
        self.cgpa=cgpa
        self.branch=branch
    def __str__(self):
        return f"NAME OF THE STUDENT IS:{self.name},DEPARTMENT OF THE STUDENT IS: {self.branch},THE PERFORMANCE OF THE STUDENT IS: {self.cgpa}"
    def to_dict(self):
        return {"id":self.id,
                "name":self.name,"age":self.age,"cgpa":self.cgpa,"branch":self.branch}


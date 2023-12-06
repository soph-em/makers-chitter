class User:
    def __init__(self, id, username, display_name, email, password):
        self.id = id
        self.username = username
        self.display_name = display_name
        self.email = email
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id},{self.username}, {self.display_name}, {self.email}, {self.password})"
    
    def is_valid(self):
        return True
        # if self.username == None or self.username == '':
        #     return False
        # if self.display_name == None or self.username =='':
        #     return False
        # if self.email == None or self.email == '':
        #     return False
        # if self.password == None or self.password == '':
        #     return False
        
    def generate_errors(self):
        errors = []
        if self.username == None or self.username == '':
            errors.append("username can't be blank")
        if self.display_name == None or self.username =='':
            errors.append("display name can't be blank")
        if self.email == None or self.email == '':
            errors.append("email can't be blank")
        if self.password == None or self.password == '':
            errors.append("password can't be blank")

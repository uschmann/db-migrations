import os
from .SqlFile import SqlFile

class Migration():
    def __init__(self, name, dir):
        self.name = name
        self.dir = dir
        self.up = None
        self.down = None
        self.full_path = f'{dir}/{name}'
        
        up_path = self.full_path + f'/up.sql'
        down_path = self.full_path + f'/down.sql'
        
        if(os.path.exists(up_path)):
            self.up = SqlFile(up_path)
            
            
        if(os.path.exists(down_path)):
            self.down = SqlFile(down_path)
            
    def has_up(self):
        return self.up != None
    
    
    def has_down(self):
        return self.up != None
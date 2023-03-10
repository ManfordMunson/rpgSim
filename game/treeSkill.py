

class WoodCutting():
    def __init__(self) -> None:
        self.trees = {"Dirt" : {"XP" : 10, "Level Req" : 0},
                      "Plain" : {"XP" : 12.5, "Level Req" : 10},
                      "Oak" : {"XP" : 22.5, "Level Req" : 25},
                      "Redwood" : {},
                      "Sequoia" : {},
                      "Obsidian" : {}}
        
        self.level = 0
        self.base_xp_needed = 100
        self.xp_needed = self.base_xp_needed

    def level_up(self):
        self.level +=1
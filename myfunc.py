import numpy as np

def adding(x):
    for i in range(max(x.shape)):
        import numpy as np    
        if x.iloc[i,0] == 'CHN' or x.iloc[i,0] == 'JPN' or x.iloc[i,0] == 'KOR':
            if x.iloc[i,15]!=0:
                if i==0:
                    y2 = np.array(sum(x.iloc[i,4:14]))
                else:
                    y2 = np.concatenate([y2.reshape(-1,1), np.array(sum(x.iloc[i,4:14])).reshape(-1,1)])
            else:
                if i==0:
                    y2 = np.NaN
                else:
                    y2 = np.concatenate([y2.reshape(-1,1), np.array(np.NaN).reshape(-1,1)])
    y2 = np.array(y2)
    return y2


import numpy as np

def addanddivide(x):
    import numpy as np
    for i in range(max(x.shape)):
        if x.iloc[i,0] == 'CHN' or x.iloc[i,0] == 'JPN' or x.iloc[i,0] == 'KOR':
            if x.iloc[i,15]!=0:
                if i==0:
                    y2 = np.array(sum(x.iloc[i,4:14])/x.iloc[i,15])
                else:
                    y2 = np.concatenate([y2.reshape(-1,1), np.array(sum(x.iloc[i,4:14])/x.iloc[i,15]).reshape(-1,1)])
            else:
                if i==0:
                    y2 = np.NaN
                else:
                    y2 = np.concatenate([y2.reshape(-1,1), np.array(np.NaN).reshape(-1,1)])
    y2 = np.array(y2)
    return y2

#class Pokemon:
#    def __init__(self, power, level, names):
#        self.power = power
#        self.level = level
#        self.names = names
# 
#    def __repr__(self):
#        return (f'Pokemon({self.power}, '
#                f'{self.level}, '
#                f'{self.names})')
# 
#    def total_damage(self):
#        return self.damage(self.power, self.level)
# 
#    @staticmethod
#    def damage(power, level):
#        return (power * level * 2) / 50
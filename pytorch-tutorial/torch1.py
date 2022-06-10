import torch
x = torch.zeros(5, 3, dtype=torch.long)
print(x)
x = x.new_ones(5, 3, dtype=torch.double)      
# new_* methods take in sizes
print(x)

x = torch.randn_like(x, dtype=torch.float)    
# override dtype!
print(x)                    
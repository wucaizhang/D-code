import torch
def linreg(x,w):
    return w*x + 1
def squared_loss(h_hat,y):
    return (h_hat-y)**2/2
true_w = torch.tensor(2)
w = torch.tensor([1],dtype=float,requires_grad=True) # requires_grad=True 代表自动求导
x_sample = torch.tensor(1)
y_sample = torch.tensor(3)
net = linreg
loss = squared_loss
learn_rate = 0.1 #学习率
h_hat = net(x_sample,w)
h_hat
l = loss(h_hat,y_sample)
l
l.backward()
w.grad
with torch.no_grad():
    w -= learn_rate*w.grad
    w.grad.zero_()
w
x_sample = torch.tensor(2)
y_sample = torch.tensor(5)
w
h_hat = net(x_sample,w)
h_hat
l = loss(net(x_sample,w),y_sample)
l
l.backward()
w.grad
with torch.no_grad():
    print("w.grad",w.grad)
    w -= learn_rate*w.grad
    w.grad.zero_()
w
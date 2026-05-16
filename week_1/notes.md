# Exercise Sheet 1

### Plot styling
Personal plot settings

plt.rcParams.update({"axes.grid":True,
                     "grid.color":"black",
                     "grid.alpha":"0.25",
                     "grid.linestyle":"--"})


Pd.series object
    1. Object which simply stores a 1-d array, with a axis labels 

    essentially just two rows, one with a number that corresponds to the the other roiw, which can be a text or what ever


## HP Filter

The HP filter essentially tries to decompose the timeseries into  



np.diff

second_diff = np.diff(tau, n=2)

calculates this nice one:

(tau_t+1-tau_t)-t(tau_t-tau_t-1)


### Improvement in loop

I wrote the quite idiomatic way: 

for t in range(len(tau)): 
    if t < 1 or t > len(tau)-2:
        continue
    acc += ((tau[t+1]-tau[t])-(tau[t]-tau[t-1]))**0.5

There are to improvements first, we can imrove the for loop by 


for t in range(1,len(tau)-1)
    ....


Next we should rely on numpy vectorization, to do the calculation, which thus we can simply replace with:

np.diff(tau,n=2)


We can also wrie it like acc += (tau[t+1] - 2*tau[t] + tau[t-1])**2


28.2 sec
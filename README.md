Simulation of Quantum Random Walk

Try initial states like:   
[1., 0.]   
[1/sqrt(2), -1/sqrt(2)]   
[1/(4-2*sqrt(2)), (-1+sqrt(2))/(4-2*sqrt(2))]   

For the third example of initial state, which is an eigenstate of the mixing operator, the root-mean-square(rms) distance is very close to total_steps/2 for any choice of total_steps.

From this simulation, we can see that the rms distance ~ total_steps. This is different from a classical random walk, which has rms distance ~ sqrt(total_steps).

By plotting the probabilites to the positions in a scaled way, we can see that the distributions are similar for random walks with different total_steps.
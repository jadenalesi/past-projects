This is a Genetic Algorithm I helped to create as part of my Introduction to Artificial Intelligence Project.

Included is both the code for the Genetic algorithm itself (GA.py) and the small report that was submitted along with the project. 

The Algorithm is designed to optimize a workday based on the time a task takes and the priority of a task, as given in lines 232 and 233, respectively. 

For this project, I designed and implemented the means of generating the inital population of chromosomes, the parent selection process, and the replacement process.

The Inital Population (Lines 18-28) was just a matter of populating the genes of the chromosome randomly. 

The Parent Selection Process used Roulette selection to select the parents to create the next generation of offspring. Roulette
selection was used in order to prioritize well-performing members of the population for reproduction, as I thought this would be
the best way to make sure we explored as much of the solution space as possible. 

The Replacement Process was designed with an elitist strategy in mind, in order to maintain the well-performing members of the
population. I also made a process for alloting the random immigration of worse performers into the next generation, in order to
explore the solution space more thoroughly. 

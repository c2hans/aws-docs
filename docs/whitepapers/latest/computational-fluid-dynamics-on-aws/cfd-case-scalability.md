---
source_url: https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/cfd-case-scalability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# CFD case scalability
<a name="cfd-case-scalability"></a>

 CFD cases that cross multiple nodes raise the question, “How will my application scale on AWS?” CFD solvers depend heavily on the solver algorithm’s ability to scale compute tasks efficiently in parallel across multiple compute resources. Parallel performance is often evaluated by determining an application’s scale-up. Scale-up is a function of the number of processors used and is defined as the time it takes to complete a run on one processor, divided by the time it takes to complete the same run on the number of processors used for the parallel run.

![Example scale-up equation.](http://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/images/scale-up-equasion.png)

Scaling is considered to be excellent when the scale-up is close to or equal to the number of processors on which the application is run. An example of scale up as a function of core count is shown in the following figure.

![A graph showing strong scaling demonstrated for a 14M cell external aerodynamics use case.](http://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/images/strong-scaling.png)

 The example case in preceding figure is a 14 million cell external aerodynamics calculation using a cell-centered unstructured solver. The mesh is composed largely of hexahedra. The black line shows the ideal or perfect scalability. The blue diamond-based curve shows the actual scale-up for this case as a function of increasing processor count. Excellent scaling is seen to almost 1000 cores for this small-sized case. This example was run on Amazon EC2 c5n.18xlarge instances, with Elastic Fabric Adapter (EFA), and using a fully loaded compute node.

 Fourteen million cells is a relatively small CFD case by today’s standards. A small case was purposely chosen for the discussion on scalability because small cases are more difficult to scale. The idea that small cases are harder than large cases to scale may seem counter intuitive, but smaller cases have less total compute to spread over a large number of cores. An understanding of strong scaling vs. weak scaling offers more insight.

## Strong scaling vs. weak scaling
<a name="strong-scaling-vs.-weak-scaling"></a>

 Case scalability can be characterized two ways: strong scaling or weak scaling. Weak does not mean inadequate — it is a technical term facilitating the description of the type of scaling.

 Strong scaling, as demonstrated in the following figure, is a traditional view of scaling, where a problem size is fixed and spread over an increasing number of processors. As more processors are added to the calculation, good strong scaling means that the time to complete the calculation decreases proportionally with increasing processor count.

 In comparison, weak scaling does not fix the problem size used in the evaluation, but purposely increases the problem size as the number of processors also increases. The ratio of the problem size to the number of processors on which the case is run is constant. For a CFD calculation, problem size most often refers to the number of cells or nodes in the mesh for a similar configuration.

 An application demonstrates good weak scaling when the time to complete the calculation remains constant as the ratio of compute effort to the number of processors is held constant. Weak scaling offers insight into how an application behaves with varying case size. Well-written CFD solvers offer excellent weak scaling capability allowing for more cores to be used when running bigger applications. The scalability of CFD cases can then be determined by looking at a normalized plot of scale-up based on the number of mesh cells per core (cells/core). An example plot is shown in the following figure.

![A graph showing scale-up and efficiency as a function of cells per processor.](http://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/images/scale-up-graph.png)

## Running efficiency
<a name="running-efficiency"></a>

 Efficiency is defined as the scale-up divided by the number of processors used in the calculation. Scale-up and efficiency as a function of cells/core is shown in the preceding figure. In this figure, the cells per core are on the horizontal axis. The blue diamond-based line shows scale-up as a function of mesh cells per processor. The vertical axis for scale-up is on the left-hand side of the graph as indicated by the lower blue arrow. The orange circle-based line shows efficiency as a function of mesh cells per core. The vertical axis for efficiency is shown on the right side of the graph and is indicated by the upper orange arrow.

![The running efficiency and scale-up equation.](http://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/images/efficiency-equasion.png)

 For similar case types, running with similar solver settings, a plot like the one in this figure can help you choose the desired efficiency and number of cores running for a given case.

 Efficiency remains at about 100% between approximately 200,000 mesh cells per core and 100,000 mesh cells per core. Efficiency starts to fall off at about 50,000 mesh cells per core. An efficiency of at least 80% is maintained until 20,000 mesh cells per core, for this case. Decreasing mesh cells per core leads to decreased efficiency because the total computational effort per core is reduced. The inefficiencies that show up at higher core counts come from a variety of sources and are caused by “serial” work. Serial work is the work that cannot be effectively parallelized. Serial work comes from solver inefficiencies, I/O inefficiencies, unequal domain decomposition, additional physical modeling such as radiative effects, additional user-defined functions, and eventually, from the network as core count continues to increase.

## Turn-around time and cost
<a name="turn-around-time-and-cost"></a>

 Plots of scale-up and efficiency offer an understanding about how a case or application scales. However, what matters most HPC users is case turn-around time and cost. A plot of turn-around time versus CPU cost for this case is shown in the following figure. As the number of cores increases, the inefficiency also increases, which leads to increased costs.

![A graph demonstrating cost for per run based on on-demand pricing for the c5n.18xlarge instance as a function of turn-around time.](http://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/images/cost-per-run.png)

 In the preceding figure, the turn-around time is shown on the horizontal axis. The cost is shown on the vertical axis. The price is based on the “on-demand” price of a `c5n.18xlarge` for 1000 iterations, and only includes the computational costs. Small costs are also incurred for data storage. Minimum cost was obtained at approximately 50,000 cells per core or more. As the efficiency is 100% over a range of core counts, the price is the same regardless of the number of cores. Many users choose a cell count per core to achieve the lowest possible cost.

 As core count goes up, inefficiencies start to show up, but turn-around time continues to drop. When a fast turn-around is needed, users may choose a large number of cores to accelerate the time to solution. For this case, a turn-around time of about five minutes can be obtained by running on about 20,000 cells per core. When considering total cost, the inclusion of license costs may make the fastest run the cheapest run.

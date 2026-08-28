---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/distributed-system-availability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Distributed system availability
<a name="distributed-system-availability"></a>

 Distributed systems are made up of both software components and hardware components. Some of the software components might themselves be another distributed system. The availability of both the underlying hardware and software components affects the resulting availability of your workload.

 The calculation of availability using MTBF and MTTR has its roots in hardware systems. However, distributed systems fail for very different reasons than a piece of hardware does. Where a manufacturer can consistently calculate the average time before a hardware component wears out, the same testing can't be applied to the software components of a distributed system. Hardware typically follows the “bathtub” curve of failure rate, while software follows a staggered curve produced by additional defects that are introduced with each new release (see [Software Reliability](https://users.ece.cmu.edu/~koopman/des_s99/sw_reliability).)

![Diagram showing hardware and software failure rates](http://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/images/failure-rates.png)

 Additionally, the software in distributed systems typically changes at rates exponentially higher than hardware. For example, a standard magnetic hard drive might have an average annualized failure rate (AFR) of 0.93% which, in practice for an HDD, can mean a lifespan of at least 3–5 years before it reaches the wear-out period, potentially longer (see [Backblaze Hard Drive Data and Stats, 2020](https://www.backblaze.com/b2/hard-drive-test-data.html).) The hard drive doesn't materially change during that lifetime, where, in 3–5 years, as an example, Amazon might deploy more than 450 to 750 million changes to its software systems. (See [Amazon Builders' Library – Automating safe, hands-off deployments](https://aws.amazon.com/about-aws/whats-new/2020/06/new-abl-article-automating-safe-hands-off-deployments/).)

 Hardware is also subject to the concept of planned obsolescence, that is has a built-in lifespan, and will need to be replaced after a certain period of time. (See [The Great Lightbulb Conspiracy](https://spectrum.ieee.org/tech-history/dawn-of-electronics/the-great-lightbulb-conspiracy).) Software, theoretically, is not subject to this constraint, it doesn't have a wear-out period and can be operated indefinitely.

 All of this means that the same testing and prediction models used for hardware to generate MTBF and MTTR numbers don’t apply to software. There have been hundreds of attempts to build models to solve this problem since the 1970s, but they all generally fall into two categories, prediction modeling and estimation modeling. (See [List of software reliability models](https://en.wikipedia.org/wiki/List_of_software_reliability_models).)

 Thus, calculating a forward-looking MTBF and MTTR for distributed systems, and thus a forward-looking availability, will always be derived from some type of prediction or forecast. They may be generated through predictive modeling, stochastic simulation, historical analysis, or rigorous testing, but those calculations are not a guarantee of uptime or downtime.

 The reasons that a distributed system failed in the past may never reoccur. The reasons it fails in the future are likely to be different and possibly unknowable. The recovery mechanisms required might also be different for future failures than ones used in the past and take significantly different amounts of time.

 Additionally, MTBF and MTTR are averages. There will be some variance from the average value to the actual values seen (the standard deviation, σ, measures this variation). Thus, workloads may experience shorter or longer time between failures and recovery times in actual production use.

 That being said, the availability of the software components that makes up a distributed system is still important. Software can fail for numerous reasons (discussed more in the next section) and impacts the workload’s availability. Thus, for highly available distributed systems, equal focus to calculating, measuring, and improving the availability of software components should be given as to hardware and external software subsystems.

**Rule 2**
 The availability of the software in your workload is an important factor of your workload’s overall availability and should receive an equal focus as other components.

 It’s important to note that despite MTBF and MTTR being difficult to predict for distributed systems, they still provide key insights into how to improve availability. Reducing the frequency of failure (higher MTBF) and decreasing the time to recover after failure occurs (lower MTTR) will both lead to a higher empirical availability.

## Types of failures in distributed systems
<a name="types-of-failures-in-distributed-systems"></a>

 There are generally two classes of bugs in distributed systems that affect availability, affectionately named the *Bohrbug* and *Heisenbug* (see ["A Conversation with Bruce Lindsay", ACM Queue vol. 2, no. 8 – November 2004](http://queue.acm.org/detail.cfm?id=1036486).)

 A Bohrbug is a repeatable functional software issue. Given the same input, the bug will consistently produce the same incorrect output (like the deterministic Bohr atom model, which is solid and easily detected). These types of bugs are rare by the time a workload gets to production.

 A Heisenbug is a bug that is transient, meaning that it only occurs in specific and uncommon conditions. These conditions are usually related to things like hardware (for example, a transient device fault or hardware implementation specifics like register size), compiler optimizations and language implementation, limit conditions (for example, temporarily out of storage), or race conditions (for example, not using a semaphore for multi-threaded operations).

 Heisenbugs make up the majority of bugs in production and are difficult to find because they are elusive and seem to change behavior or disappear when you try to observe or debug them. However, if you restart the program, the failed operation will likely succeed because the operating environment is slightly different, eliminating the conditions that introduced the Heisenbug.

 Thus, most failures in production are transient and when the operation is retried, it is unlikely to fail again. To be resilient, distributed systems have to be fault tolerant to Heisenbugs. We’ll explore how to this can be achieved in the section [Increasing distributed system MTBF](increasing-mtbf.md#increasing-mtbf.title).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

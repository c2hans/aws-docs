---
source_url: https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/solving-big-data-problems-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Solving big data problems on AWS
<a name="solving-big-data-problems-on-aws"></a>

This whitepaper has examined some tools available on AWS for big data analytics. This paper provides a good reference point when starting to design your big data applications. However, there are additional aspects you should consider when selecting the right tools for your specific use case. In general, each analytical workload has certain characteristics and requirements that dictate which tool to use, such as:
+  How quickly do you need analytic results: in real time, in seconds, or is an hour a more appropriate time frame?
+  How much value will these analytics provide your organization and what budget constraints exist?
+  How large is the data and what is its growth rate?
+  How is the data structured?
+  What integration capabilities do the producers and consumers have?
+  How much latency is acceptable between the producers and consumers?
+  What is the cost of downtime or how available and durable does the solution need to be?
+  Is the analytic workload consistent or elastic?

 Each one of these questions helps guide you to the right tool. In some cases, you can simply map your big data analytics workload into one of the services based on a set of requirements. However, in most real-world, big data analytic workloads, there are many different, and sometimes conflicting, characteristics and requirements on the same data set.

 For example, some result sets may have real-time requirements as a user interacts with a system, while other analytics could be batched and run on a daily basis. These different requirements over the same data set should be decoupled and solved by using more than one tool. If you try to solve both of these examples using the same toolset, you end up either over-provisioning or therefore overpaying for unnecessary response time, or you have a solution that does not respond fast enough to your users in real time. Matching the best-suited tool to each analytical problem results in the most cost-effective use of your compute and storage resources.

 Big data doesn’t need to mean “big costs”. So, when designing your applications, it’s important to make sure that your design is cost efficient. If it’s not, relative to the alternatives, then it’s probably not the right design. Another common misconception is that using multiple tool sets to solve a big data problem is more expensive or harder to manage than using one big tool. If you take the same example of two different requirements on the same data set, the real-time request may be low on CPU but high on I/O, while the slower processing request may be very compute intensive.

 Decoupling can end up being much less expensive and easier to manage, because you can build each tool to exact specifications and not overprovision. With the AWS pay-as-you-go model, this equates to a much better value because you could run the batch analytics in just one hour and therefore only pay for the compute resources for that hour. Also, you may find this approach easier to manage rather than leveraging a single system that tries to meet all of the requirements. Solving for different requirements with one tool results in attempting to fit a square peg (real-time requests) into a round hole (a large data warehouse).

 The AWS platform makes it easy to decouple your architecture by having different tools analyze the same data set. AWS services have built-in integration so that moving a subset of data from one tool to another can be done very easily and quickly using parallelization. Following are some real world, big data analytics problem scenarios, and an AWS architectural solution for each.

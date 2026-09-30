---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/cap-theorem.html
---

# CAP theorem
<a name="cap-theorem"></a>

 Another way that we might think about availability is in relation to the CAP theorem. The theorem states that a distributed system, one made up of multiple nodes storing data, cannot simultaneously provide more than two out of the following three guarantees:
+  **C**onsistency: Every read request receives the most recent write or an error when consistency can't be guaranteed.
+  **A**vailability: Every request receives a non-error response, even when nodes are down or unavailable.
+  **P**artition tolerance: The system continues to operate despite the loss of an arbitrary number of messages between nodes.

(For more details, see Seth Gilbert and Nancy Lynch, [*Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services*](http://dl.acm.org/citation.cfm?id=564601&CFID=609557487&CFTOKEN=15997970), *ACM SIGACT News*, Volume 33 Issue 2 (2002), pg. 51–59.)

 Most distributed systems have to tolerate network failures, and thus, network partitioning has to be allowed. This means that these workloads have to make a choice between consistency and availability when a network partition occurs. If the workload chooses availability, then it always returns a response, but with potentially inconsistent data. If it chooses consistency, then during a network partition it would return an error since the workload can't be sure about the consistency of the data.

 For workloads whose goal it is to provide higher levels of availability, they might choose Availability and Partition tolerance (AP) to prevent returning errors (being unavailable) during a network partition. This results in requiring a more relaxed [consistency model](https://en.wikipedia.org/wiki/Consistency_model), like eventual consistency or monotonic consistency.

---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/performance.html
---

# Performance
<a name="performance"></a>

 The Dynamic Object and Rule Extensions for AWS Network solution offers *near* real-time resolution of AWS resources encapsulated by custom defined objects. However, it is important to note, that the resolution time is a function of the total number of distinct objects being referenced across all rules within the rule group. As the number of referenced objects increases, the resolution time also increases linearly as shown in the graph below.

![Rule group resolution using Dynamic Object and Rule Extensions for AWS Network Firewall solution](http://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/images/performance.png)

 To ensure performance of the solution, the capacity of the rule group ARN must be configured accordingly. We recommend setting the rule group capacity to at least 15,000.

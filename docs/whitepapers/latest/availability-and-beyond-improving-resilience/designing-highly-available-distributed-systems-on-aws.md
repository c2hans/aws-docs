---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/designing-highly-available-distributed-systems-on-aws.html
---

# Designing highly available distributed systems on AWS
<a name="designing-highly-available-distributed-systems-on-aws"></a>

 The previous sections have been mostly about the theoretical availability of workloads and what they can achieve. They are an important set of concepts to keep in mind as you build distributed systems. They will help inform your dependency selection process and how you implement redundancy.

 We've also looked at the relationship of MTTD, MTTR, and MTBF to availability. This section will introduce practical guidance based on the previous theory. In short, engineering workloads for high availability aims to increase the MTBF and decrease the MTTR as well as the MTTD.

 Although eliminating all failures would be ideal, it's not realistic. In large distributed systems with deeply stacked dependencies, failures are going to occur. "Everything fails all of the time" (see Werner Vogels, CTO, Amazon.com, [10 Lessons from 10 Years of Amazon Web Services](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html).) and "you can't legislate against failure [so] focus on fast detection and response." (see Chris Pinkham, founding member, Amazon EC2 team, [ARC335 Designing for failure: Architecting resilient systems on AWS](https://d1.awsstatic.com/events/reinvent/2019/REPEAT_1_Designing_for_failure_Architecting_resilient_systems_on_AWS_ARC335-R1.pdf))

 What this means is that frequently you don't have control over whether failure happens. What you can control is how quickly you detect the failure and do something about it. So, while increasing MTBF is still an important component of high availability, the most significant changes customers have within their control is reducing MTTD and MTTR.

**Topics**
+ [Reducing MTTD](reducing-mttd.md)
+ [Reducing MTTR](reducing-mttr.md)
+ [Increasing MTBF](increasing-mtbf.md)

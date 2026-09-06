---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/introduction.html
---

# Introduction
<a name="introduction"></a>

 Your workload must perform its intended function correctly and consistently. To achieve this, you must architect for *resiliency*. Resiliency is the ability of a workload to recover from infrastructure, service, or application disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions, such as misconfigurations or transient network issues.

 Disaster recovery (DR) is an important part of your resiliency strategy and concerns how your workload responds when a disaster strikes (a [disaster](what-is-a-disaster.md) is an event that causes a serious negative impact on your business). This response must be based on your organization's business objectives which specify your workload's strategy for avoiding loss of data, known as the [Recovery Point Objective (RPO)](business-continuity-plan-bcp.md#recovery-objectives-rto-and-rpo), and reducing downtime where your workload is not available for use, known as the [Recovery Time Objective (RTO)](business-continuity-plan-bcp.md#recovery-objectives-rto-and-rpo). You must therefore implement resilience in the design of your workloads in the cloud to meet your recovery objectives ([RPO and RTO](business-continuity-plan-bcp.md#recovery-objectives-rto-and-rpo)) for a given one-time disaster event. This approach helps your organization to maintain business continuity as part of [Business Continuity Planning (BCP)](business-continuity-plan-bcp.md).

 This paper focuses on how to plan for, design, and implement architectures on AWS that meet the disaster recovery objectives for your business. The information shared here is intended for those in technology roles, such as chief technology officers (CTOs), architects, developers, operations team members, and those tasked with assessing and mitigating risks.

## Disaster recovery and availability
<a name="disaster-recovery-and-availability"></a>

 Disaster recovery can be compared to *availability*, which is another important component of your resiliency strategy. Whereas disaster recovery measures objectives for one-time events, availability objectives measure mean values over a period of time.

![Image showing resiliency objectives for disaster recovery (RTO, RPO) and Availability (MTBF, MTTR).](http://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/images/resiliency-objectives.png)

*Figure 1 - Resiliency Objectives *

 Availability is calculated using Mean Time Between Failures (MTBF) and Mean Time to Recover (MTTR):

![Availability equals Available for Use Time divided by Total Time equals MTBF divided by MTBF plus MTTR.](http://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/images/availability-calculation-time-based.png)

 This approach is often referred to as “nines”, where a 99.9% availability target is referred to as “three nines”.

 For your workload, it may be easier to count successful and failed requests instead of using a time-based approach. In this case, the following calculation can be used:

![Availability equals successful responses divided by valid requests.](http://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/images/availability-calculation-successful-failed-requests.png)

 Disaster recovery focuses on disaster events, whereas availability focuses on more common disruptions of smaller scale such as component failures, network issues, software bugs, and load spikes. The objective of disaster recovery is business continuity, whereas availability concerns maximizing the time that a workload is available to perform its intended business functionality. Both should be part of your resiliency strategy.

## Are you Well-Architected?
<a name="well-architected"></a>

The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

The concepts covered in this whitepaper expand on the best practices contained in the [Reliability Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html), specifically question [REL 13](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-failure-management.html), “How do you plan for disaster recovery (DR)?”. After implementing the practices in this whitepaper, be sure to review (or re-review) your workload using the AWS Well-Architected Tool.

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel05.html
---

# Failure management
<a name="advrel05"></a>

 Failures are unavoidable, and every system eventually fails over time, especially in high volume advertising systems. Anticipate and manage failures before they happen through detection, testing, and quick recovery.

| ADVREL05: How do you continuously evaluate the resilience of your advertising workload to meet availability and recovery requirements? |
| --- |
|   |

 Continuous resilience evaluation of advertising workloads can be achieved through two main approaches.

 Perform regular fault tolerance testing and assessment using tools like AWS Gamedays, Well-Architected Framework Reviews, and Support Countdowns. Additionally, create and test disaster recovery procedures through documented runbooks and restoration processes, which helps you quickly recover during incidents.

**Topics**
+ [ADVREL05-BP01 Perform routine evaluation of your workload's fault tolerance capabilities](advrel05-bp01.md)
+ [ADVREL05-BP02 Create disaster recovery (DR) runbooks, and regularly test documented backup and restoration processes](advrel05-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

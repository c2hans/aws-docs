---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/performance-efficiency.html
---

# Performance efficiency
<a name="performance-efficiency"></a>

 The performance efficiency pillar focuses on the efficient use of computing resources to meet requirements and maintain efficiency as demand changes and technologies evolve.

 Use a data-driven approach to select a high-performance architecture. Gather data on all aspects of the architecture, from the high-level design to the selection and configuration of resource types. Review your choices on a cyclical basis to ensure that you are taking advantage of the continually evolving AWS platform. Monitor your workload to ensure that you are aware of any deviance from expected performance. Understand where you can make architecture tradeoffs to improve performance, such using VPN over internet vs dedicated circuits via AWS Direct Connect for your hybrid connectivity or terminating your hybrid connectivity on Virtual Private gateway instead of Transit Gateway.

**Topics**
+ [Architecture selection](architecture-selection.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

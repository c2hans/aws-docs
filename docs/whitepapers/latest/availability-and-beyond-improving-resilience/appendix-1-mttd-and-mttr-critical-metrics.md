---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/appendix-1-mttd-and-mttr-critical-metrics.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix 1 – MTTD and MTTR critical metrics
<a name="appendix-1-mttd-and-mttr-critical-metrics"></a>

 The following is a framework for standardization in instrumentation and observability that can help reduce the MTTD and MTTR during an event.

 **Customer Experience metrics.** These metrics reflect that a service is responsive and available to serve customer requests. For example, control plane latency. These metrics measure error rate, availability, latency, volume, and throttle rate.

 **Impact Assessment metrics.** These metrics provide insight into the scope of impact during events. For example, the number or percentage of customers impacted by a data plane event. Measures the number or percentage of things impacted.

 **Operational Health metrics.** These metrics reflect that a service is responsive and available to serve customer requests, but focuses on common infrastructure subsystems and resources. For example, the percentage of CPU utilization of your EC2 fleet. These metrics should measure utilization, capacity, throughput, error rate, availability, and latency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

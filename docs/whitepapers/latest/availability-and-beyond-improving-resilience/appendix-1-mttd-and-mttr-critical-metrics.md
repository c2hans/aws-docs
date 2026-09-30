---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/appendix-1-mttd-and-mttr-critical-metrics.html
---

# Appendix 1 – MTTD and MTTR critical metrics
<a name="appendix-1-mttd-and-mttr-critical-metrics"></a>

 The following is a framework for standardization in instrumentation and observability that can help reduce the MTTD and MTTR during an event.

 **Customer Experience metrics.** These metrics reflect that a service is responsive and available to serve customer requests. For example, control plane latency. These metrics measure error rate, availability, latency, volume, and throttle rate.

 **Impact Assessment metrics.** These metrics provide insight into the scope of impact during events. For example, the number or percentage of customers impacted by a data plane event. Measures the number or percentage of things impacted.

 **Operational Health metrics.** These metrics reflect that a service is responsive and available to serve customer requests, but focuses on common infrastructure subsystems and resources. For example, the percentage of CPU utilization of your Amazon EC2 fleet. These metrics should measure utilization, capacity, throughput, error rate, availability, and latency.

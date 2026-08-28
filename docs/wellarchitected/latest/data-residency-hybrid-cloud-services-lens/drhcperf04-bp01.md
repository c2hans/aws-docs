---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcperf04-bp01.html
---

# DRHCPERF04-BP01 Establish hybrid edge workload health KPIs
<a name="drhcperf04-bp01"></a>

 Demonstrate your workload is meeting your business requirements.

 **Desired outcome:** You can illustrate you are meeting your business requirements for the workload.

 **Benefits of establishing this best practice:** Metrics can provide data for continuous workload improvement.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-46"></a>

 You should develop [key performance indicators (KPIs)](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/) to show how effectively you're achieving objectives applicable to your workload. [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html) has additional metrics that should be monitored. Determine the application KPI's to monitor to provide the optimal user experience.

 Instrument your code using a tool such as [AWS X-Ray](https://aws.amazon.com/xray/), and use [Amazon CloudWatch](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html) to monitor in-Region dependencies. You should monitor service link [bandwidth and round trip latency](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html#sl-bandwidth-recommendations) to provide optimal performance. Hybrid edge services must meet unique minimum requirements as defined in the User Guide for Outposts racks and [servers](https://docs.aws.amazon.com/outposts/latest/server-userguide/region-connectivity.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

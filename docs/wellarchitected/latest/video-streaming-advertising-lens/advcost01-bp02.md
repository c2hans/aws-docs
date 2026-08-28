---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost01-bp02.html
---

# ADVCOST01-BP02 Evaluate resiliency needs against the cost of downtime for ad delivery and bidding
<a name="advcost01-bp02"></a>

 While resiliency can increase the cost of workloads, downtime can also be very expensive. It's important to understand the costs of having a resilient infrastructure against the costs of not having a resilient infrastructure.

## Implementation guidance
<a name="implementation-guidance-58"></a>
+  Quantify the cost of downtime for each campaign based on its expected revenue.
  +  Analyze historical data and projections to estimate the potential revenue loss due to downtime.
  +  Consider the impact on customer satisfaction and brand reputation.
+  Estimate the cost of applying resiliency measures.
  +  Evaluate the cost of additional resources required for multi-Regional deployments, backup, and recovery solutions
  +  Use AWS tools like [AWS Pricing Calculator](https://calculator.aws/#/) for estimating costs of future resiliency efforts and [Quick](https://aws.amazon.com/quicksight/), [Amazon Athena](https://aws.amazon.com/athena/), AWS Cost and Usage Report, and [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) for cost analysis and reporting.
+  Compare the cost of downtime with the cost of resiliency measures.
  +  If the potential lost revenue and reputation costs of downtime exceed the cost of resiliency, favor implementing resiliency measures.
  +  Consider multi-regional deployments, backup and recovery solutions, and other resiliency best practices.

 By following these steps, you can make informed decisions about implementing resiliency measures based on a cost-benefit analysis, using AWS tools and services to optimize your approach and ensure business continuity.

## Key AWS services
<a name="key-aws-services-33"></a>
+  [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/)
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

## Resources
<a name="resources-52"></a>
+  [Stage 1: Set objectives](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/stage-1.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

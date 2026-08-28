---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus08-bp01.html
---

# ADVSUS08-BP01 Optimize privacy workload processing patterns and resource allocation for sustainability
<a name="advsus08-bp01"></a>

 For privacy-enhanced collaboration, advertising workloads have specific sustainability considerations for combining first and third-party customer data directly.

## Implementation guidance
<a name="implementation-guidance-advsus08-bp01"></a>
+  Schedule intensive privacy computations during periods of lower carbon intensity.
+  Use batch processing for data cleansing and matching operations.
+  Implement efficient data compression and formatting using formats such as Parquet.
+  Leverage AWS Graviton processors for energy-efficient computing.
+  Use serverless architectures for matching operations where possible.
+  Implement auto scaling based on actual collaboration workload patterns.
+  Configure Regional data aggregation before central processing to reduce transfer needs.

## Key AWS services
<a name="aws-key-services-5"></a>
+  AWS Lambda
+  AWS Graviton Processors
+  AWS Auto Scaling

## Resources
<a name="resources-advsus08-bp01"></a>
+  [Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html)
+  [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/optimization.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

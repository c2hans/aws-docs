---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aossus02-bp01.html
---

# AOSSUS02-BP01 Evaluate instances in alignment to sustainability goals
<a name="aossus02-bp01"></a>

 Reduce carbon footprint, improve sustainability performance, and enhance regulatory compliance by evaluating instance choices that align with your organization's sustainability goals.

 **Level of risk exposed if this best practice is not established**: Medium

 **Desired outcome**: You use energy-efficient instances that help reduce your carbon footprint.

 **Benefits of establishing this best practice:**
+  Reduced carbon footprint due to increased energy efficiency
+  Improved sustainability performance and compliance with organizational goals
+  Enhanced ability to meet environmental regulations and standards

## Implementation guidance
<a name="implementation-guidance-58"></a>

 AWS Graviton-based instances use up to 60% less energy than comparable instances.
+  **Identify supported Graviton instance types:** Explore the [available Graviton-based instance types](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html), such as r7g and r6g, that are optimized for OpenSearch and energy efficiency.
+  **Search for suitable instance types:** Explore [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/) to find Graviton-based instances that align with your workload and financial requirements. You can filter results by Region to narrow down the options.
+  **Conduct performance testing:** Run rigorous performance tests to determine the most suitable Graviton instance type for your specific workload.

## Resources
<a name="resources-58"></a>
+  [Supported instance types in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html)
+  [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/)
+  [OpenSearch Benchmark tool](https://opensearch.org/docs/latest/benchmark/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aoscost01-bp01.html
---

# AOSCOST01-BP01 Use the latest generation of instances for your OpenSearch Service domains
<a name="aoscost01-bp01"></a>

 Improve performance and reduce costs by using the latest instance generation, which offers enhanced memory, security features, and potentially better price-performance ratios.

 **Level of risk exposed if this best practice is not established**: Medium

 **Desired outcome**: You use the latest generation of instances for OpenSearch Service domains to gain optimal performance, increased memory, and enhanced security features.

 **Benefits of establishing this best practice:**
+  Enhance the performance of your OpenSearch Service domains.
+  Modern instances can lead to cost savings, as they often provide better price-performance ratios compared to older instance types.

## Implementation guidance
<a name="implementation-guidance-46"></a>

 Amazon OpenSearch Service offers the option to create domains using the latest generation Amazon OpenSearch Service instance types, delivering enhanced performance and reduced instance costs. Regularly review the supported instance types, and upgrade your domain to use the latest generation of the instances.
+  **Identify supported instance types:** Visit the [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html) to explore the available instance types.
+  **Search for suitable instance types:** Use [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/) to find instances that align with your workload and financial requirements. You can filter results by Region to narrow down the options.

## Resources
<a name="resources-45"></a>
+  [Supported instance types in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html)
+  [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aoscost02-bp01.html
---

# AOSCOST02-BP01 Use the latest Amazon EBS gp3 volumes with your OpenSearch Service nodes
<a name="aoscost02-bp01"></a>

 Improve baseline performance and scalability by using the latest Amazon EBS gp3 volumes, which offer higher baseline performance and more scalable high performance.

 **Level of risk exposed if this best practice is not established:** Low

 **Desired outcome:** The latest Amazon EBS gp3 volumes are used with OpenSearch Service nodes to provide optimal performance, durability, and cost-effectiveness.

 **Benefits of establishing this best practice:**
+  **Improved baseline performance:** Using gp3 EBS volumes provides higher baseline performance compared to gp2 volumes.
+  **Scalable high performance:** With gp3 volumes, you can provision higher performance independently of the volume size, allowing for more scalable and efficient performance in your OpenSearch Service domains.

## Implementation guidance
<a name="implementation-guidance-49"></a>

 OpenSearch Service launched support for the next generation, general purpose SSD (gp3) EBS volumes. OpenSearch Service data nodes require low latency and high throughput storage to provide fast indexing and query. We recommend that you consider gp3 as an effective Amazon EBS option for price, performance, and flexibility.

 For more details about implementing this best practice for cost optimization, see [AOSPERF03-BP03](aosperf03-bp03.md).

## Resources
<a name="resources-48"></a>
+  [Making configuration changes in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

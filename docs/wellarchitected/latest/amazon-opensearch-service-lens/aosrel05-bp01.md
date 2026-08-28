---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aosrel05-bp01.html
---

# AOSREL05-BP01 Implement appropriate compute sizing for production workloads
<a name="aosrel05-bp01"></a>

 Improve OpenSearch Service domain performance by implementing compute sizing that meets production workload requirements. This practice helps you avoid CPU throttling due to depleted burst credits and minimize risks.

 **Level of risk exposed if this best practice is not established:** Medium

 **Desired outcome**: Your OpenSearch Service domain is running on instance families that meet the required performance and resource needs.

 **Benefits of establishing this best practice:**
+  Avoid CPU throttling if burst credits are depleted
+  Improve your ability to maintain performance and minimize risks

## Implementation guidance
<a name="implementation-guidance-28"></a>

 Avoid using t2 or t3.small instances for production domains, as they can become unstable under sustained heavy load. t3.medium instances are an option for small production workloads (both as data nodes and as dedicated leader nodes).

## Resources
<a name="resources-26"></a>
+  [Operational best practices for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp.html#bp-cost-optimization-instances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

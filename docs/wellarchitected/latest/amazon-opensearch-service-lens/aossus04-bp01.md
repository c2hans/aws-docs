---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aossus04-bp01.html
---

# AOSSUS04-BP01 Consolidate OpenSearch Service domain environments
<a name="aossus04-bp01"></a>

 Reduce costs, improve resource utilization, and enhance data protection by consolidating development and test workloads into fewer OpenSearch Service domains with implemented security features.

 **Level of risk exposed if this best practice is not established:** Medium

 **Desired outcome:** You consolidate development and test workloads into fewer OpenSearch Service domains, with security features implemented to protect data.

 **Benefits of establishing this best practice:**
+  Reduced costs and increased cost efficiency
+  Improved resource utilization and reduced waste
+  Enhanced ability to manage and optimize resources
+  Improved data protection and compliance due to security features

## Implementation guidance
<a name="implementation-guidance-63"></a>

 Combining multiple workloads into a smaller number of OpenSearch Service domains not only minimizes compute and storage waste but also contributes to a reduction in carbon emissions.

 Additionally, you can use fine-grained access control to implement tight security controls over your data.

## Resources
<a name="resources-63"></a>
+  [Storing Multi-Tenant SaaS Data with Amazon OpenSearch Service](https://aws.amazon.com/blogs/apn/storing-multi-tenant-saas-data-with-amazon-opensearch-service/)
+  [Build a multi-tenant serverless architecture in Amazon OpenSearch Service](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html)
+  [Building Multi-Tenant Solutions with Amazon OpenSearch Service](https://pages.awscloud.com/Building-Multi-Tenant-Solutions-with-Amazon-OpenSearch-Service_2022_0228-ABD_OD.html)
+  [Security in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

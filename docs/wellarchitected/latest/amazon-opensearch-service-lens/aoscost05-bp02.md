---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aoscost05-bp02.html
---

# AOSCOST05-BP02 Examine the costs associated with Amazon S3 storage for manually creating snapshots of your OpenSearch Service domain
<a name="aoscost05-bp02"></a>

 Improve cost awareness and inform backup strategy by examining Amazon S3 storage costs associated with manually creating snapshots of your OpenSearch Service domain.

 **Level of risk exposed if this best practice is not established:** Medium

 **Desired outcome**: You can estimate costs by examining the costs associated with Amazon S3 storage for manually creating snapshots of your OpenSearch Service domain.

 **Benefits of establishing this best practice:**
+  **Cost awareness**: Examining the costs associated with Amazon S3 storage for manually creating snapshots of your OpenSearch Service domain helps you understand that backups can incur standard Amazon S3 usage charges.
+  **Informed backup strategy**: By considering the cost of manual backups, you can choose the most suitable backup strategy for your needs, whether it's manual backups or using AWS services like Automated Backups or Snapshots in OpenSearch.

## Implementation guidance
<a name="implementation-guidance-56"></a>

 If you take manual backups of your OpenSearch Service domain, understand that the manual snapshots storing in Amazon S3 can incur standard Amazon S3 usage charges. For detailed information about the cost of the different storage tiers available in Amazon S3, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4).

## Resources
<a name="resources-55"></a>
+  [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4)
+  [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/#Free_tier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

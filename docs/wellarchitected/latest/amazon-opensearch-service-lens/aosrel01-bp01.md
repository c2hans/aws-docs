---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aosrel01-bp01.html
---

# AOSREL01-BP01 Implement a system update notification strategy
<a name="aosrel01-bp01"></a>

 Stay informed about notifications regarding updates to Amazon OpenSearch Service, which prepares you for changes or new features.

 **Level of risk exposed if this best practice is not established:** Medium

 **Desired outcome:** You stay informed about notifications regarding updates to Amazon OpenSearch Service.

 **Benefits of establishing this best practice:** Staying informed about updates to Amazon OpenSearch Service, can help you anticipate and prepare for any changes or new features in the service.

## Implementation guidance
<a name="implementation-guidance-20"></a>

 We recommend setting up alarms receive notifications on updates to the OpenSearch Service domains. Subscribe to AWS Region availability, new features, security patches, bug fixes, and other improvements about OpenSearch Service.

### Implementation steps
<a name="implementation-steps-11"></a>
+  Subscribe to [AWS Newsletters](https://aws.amazon.com/about-aws/whats-new/analytics/?whats-new-content.sort-by=item.additionalFields.postDateTime&whats-new-content.sort-order=desc&awsf.whats-new-products=general-products%23amazon-opensearch-service) and [Blogs](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-elasticsearch-service/)
+  Setup CloudWatch alarms. For detailed implementation steps, see [AOSOPS03-BP01](aosops03-bp01.md).

## Resources
<a name="resources-19"></a>
+  [What's New with Analytics?](https://aws.amazon.com/about-aws/whats-new/analytics/?whats-new-content.sort-by=item.additionalFields.postDateTime&whats-new-content.sort-order=desc&awsf.whats-new-products=general-products%23amazon-opensearch-service)
+  [Amazon OpenSearch Service Blog](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-elasticsearch-service/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

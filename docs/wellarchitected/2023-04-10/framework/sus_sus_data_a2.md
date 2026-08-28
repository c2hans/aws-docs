---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sus_sus_data_a2.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP01 Implement a data classification policy
<a name="sus_sus_data_a2"></a>

Classify data to understand its criticality to business outcomes and choose the right energy-efficient storage tier to store the data.

 **Common anti-patterns:**
+  You do not identify data assets with similar characteristics (such as sensitivity, business criticality, or regulatory requirements) that are being processed or stored.
+  You have not implemented a data catalog to inventory your data assets.

 **Benefits of establishing this best practice:** Implementing a data classification policy allows you to determine the most energy-efficient storage tier for data.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Data classification involves identifying the types of data that are being processed and stored in an information system owned or operated by an organization. It also involves making a determination on the criticality of the data and the likely impact of a data compromise, loss, or misuse.

 Implement data classification policy by working backwards from the contextual use of the data and creating a categorization scheme that takes into account the level of criticality of a given dataset to an organization’s operations.

 **Implementation steps**
+  Conduct an inventory of the various data types that exist for your workload.
  +  For more detail on data classification categories, see [Data Classification whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html).
+  Determine criticality, confidentiality, integrity, and availability of data based on risk to the organization. Use these requirements to group data into one of the data classification tiers that you adopt.
  +  As an example, see [Four simple steps to classify your data and secure your startup](https://aws.amazon.com/blogs/startups/four-simple-steps-to-classify-your-data-and-secure-your-startup/).
+  Periodically audit your environment for untagged and unclassified data, and classify and tag the data appropriately.
  +  As an example, see [Data Catalog and crawlers in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html).
+  Establish a data catalog that provides audit and governance capabilities.
+  Determine and document the handling procedures for each data class.
+  Use automation to continually audit your environment to identify untagged and unclassified data, and classify and tag the data appropriately.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Leveraging AWS Cloud to Support Data Classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/leveraging-aws-cloud-to-support-data-classification.html)
+  [Tag policies from AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)

 **Related videos:**
+ [ Enabling agility with data governance on AWS](https://www.youtube.com/watch?v=vznDgJkoH7k)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

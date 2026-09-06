---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_data_a2.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP01 Implement a data classification policy
<a name="sus_sus_data_a2"></a>

 Classify data to understand its significance to business outcomes. Use this information to determine when you can move data to more energy-efficient storage or safely delete it.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Determine requirements for the distribution, retention, and deletion of your data.
+  Use tagging on volumes and objects to record the metadata that’s used to determine how it’s managed, including data classification.
+  Periodically audit your environment for untagged and unclassified data, and classify and tag the data appropriately.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Data Classification Process](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-process.html)
+  [Leveraging AWS Cloud to Support Data Classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/leveraging-aws-cloud-to-support-data-classification.html)
+  [Tag policies from AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)

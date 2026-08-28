---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus-04.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS 4 How do you take advantage of data access and usage patterns to support your sustainability goals?
<a name="sus-04"></a>

Implement data management practices to reduce the provisioned storage required to support your workload, and the resources required to use it. Understand your data, and use storage technologies and configurations that best support the business value of the data and how it’s used. Lifecycle data to more efficient, less performant storage when requirements decrease, and delete data that’s no longer required.

**Topics**
+ [SUS04-BP01 Implement a data classification policy](sus_sus_data_a2.md)
+ [SUS04-BP02 Use technologies that support data access and storage patterns](sus_sus_data_a3.md)
+ [SUS04-BP03 Use lifecycle policies to delete unnecessary data](sus_sus_data_a4.md)
+ [SUS04-BP04 Minimize over-provisioning in block storage](sus_sus_data_a5.md)
+ [SUS04-BP05 Remove unneeded or redundant data](sus_sus_data_a6.md)
+ [SUS04-BP06 Use shared file systems or object storage to access common data](sus_sus_data_a7.md)
+ [SUS04-BP07 Minimize data movement across networks](sus_sus_data_a8.md)
+ [SUS04-BP08 Back up data only when difficult to recreate](sus_sus_data_a9.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

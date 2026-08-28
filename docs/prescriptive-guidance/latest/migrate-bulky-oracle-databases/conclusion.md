---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

In this guide, you learned how to minimize downtime by using Oracle cross-platform transportable tablespaces and RMAN incremental backups with AWS Snowball, AWS Direct Connect, and Amazon FSx for Lustre.

When migrating an Oracle database from on premises to AWS, consider the following variables:
+ The network bandwidth required by Direct Connect
+ The capacity of FSx for Lustre
+ The metadata size of the Oracle database
+ The incremental backup size

Using the method recommended in this guide, when migrating from an 100 TB Oracle database running on a Unix system to AWS, you can reduce the downtime to around 10 hours.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

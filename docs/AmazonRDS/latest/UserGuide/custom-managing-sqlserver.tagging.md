---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing-sqlserver.tagging.html
---

# Tagging RDS Custom for SQL Server resources
<a name="custom-managing-sqlserver.tagging"></a>

You can tag RDS Custom resources as with Amazon RDS resources, but with some important differences:
+ Don't create or modify the `AWSRDSCustom` tag that's required for RDS Custom automation. If you do, you might break the automation.
+ The `Name` tag is added to RDS Custom resources with the prefix `do-not-delete-rds-custom`. Any customer-passed value for the key is overwritten.
+ Tags added to RDS Custom DB instances during creation are propagated to all other related RDS Custom resources.
+ Tags aren't propagated when you add them to RDS Custom resources after DB instance creation.

For general information about resource tagging, see [Tagging Amazon RDS resources](USER_Tagging.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

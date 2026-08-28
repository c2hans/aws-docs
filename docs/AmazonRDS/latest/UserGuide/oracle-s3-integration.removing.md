---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.removing.html
---

# Removing the Amazon S3 integration option
<a name="oracle-s3-integration.removing"></a>

**Important**
Removing the S3\_INTEGRATION option invalidates the `rdsadmin.rdsadmin_s3_tasks` package. Ensure all S3 transfers are complete before removing this option.

You can remove Amazon S3 integration option from a DB instance.

To remove the Amazon S3 integration option from a DB instance, do one of the following:
+ To remove the Amazon S3 integration option from multiple DB instances, remove the `S3_INTEGRATION` option from the option group to which the DB instances belong. This change affects all DB instances that use the option group. For more information, see [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption).

+ To remove the Amazon S3 integration option from a single DB instance, modify the instance and specify a different option group that doesn't include the `S3_INTEGRATION` option. You can specify the default (empty) option group or a different custom option group. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

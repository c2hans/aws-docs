---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.removing.html
---

# Removing the EFS\_INTEGRATION option
<a name="oracle-efs-integration.removing"></a>

The steps for removing the `EFS_INTEGRATION` option depend on whether you're removing the option from multiple DB instances or a single instance.

| Number of DB instances | Action | Related information |
| --- | --- | --- |
| Multiple | Remove the EFS\_INTEGRATION option from the option group to which the DB instances belong. This change affects all instances that use the option group. | [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption) |
| Single | Modify the DB instance and specify a different option group that doesn't include the EFS\_INTEGRATION option. You can specify the default (empty) option group or a different custom option group. | [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md) |

After you remove the `EFS_INTEGRATION` option, you can optionally delete the EFS file system that was connected to your DB instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

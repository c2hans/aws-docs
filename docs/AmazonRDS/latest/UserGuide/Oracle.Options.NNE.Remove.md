---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.NNE.Remove.html
---

# Removing the NATIVE\_NETWORK\_ENCRYPTION option
<a name="Oracle.Options.NNE.Remove"></a>

You can remove NNE from a DB instance.

To remove the `NATIVE_NETWORK_ENCRYPTION` option from a DB instance, do one of the following:
+ To remove the option from multiple DB instances, remove the `NATIVE_NETWORK_ENCRYPTION` option from the option group they belong to. This change affects all DB instances that use the option group. After you remove the `NATIVE_NETWORK_ENCRYPTION` option, you don't need to restart your DB instances. For more information, see [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption).
+ To remove the option from a single DB instance, modify the DB instance and specify a different option group that doesn't include the `NATIVE_NETWORK_ENCRYPTION` option. You can specify the default (empty) option group, or a different custom option group. After you remove the `NATIVE_NETWORK_ENCRYPTION` option, you don't need to restart your DB instance. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

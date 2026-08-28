---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html
---

# Parameter groups for Amazon RDS
<a name="USER_WorkingWithParamGroups"></a>

*Database parameters* specify how the database is configured. For example, database parameters can specify the amount of resources, such as memory, to allocate to a database.

You manage your database configuration by associating your DB instances and Multi-AZ DB clusters with parameter groups. Amazon RDS defines parameter groups with default settings. You can also define your own parameter groups with customized settings.

**Note**
Some DB engines offer additional features that you can add to your database as options in an option group. For information about option groups, see [Working with option groups](USER_WorkingWithOptionGroups.md).

**Topics**
+ [Overview of parameter groups](parameter-groups-overview.md)
+ [DB parameter groups for Amazon RDS DB instances](USER_WorkingWithDBInstanceParamGroups.md)
+ [Working with DB cluster parameter groups for Multi-AZ DB clusters](USER_WorkingWithDBClusterParamGroups.md)
+ [Comparing DB parameter groups](USER_WorkingWithParamGroups.Comparing.md)
+ [Specifying DB parameters](USER_ParamValuesRef.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

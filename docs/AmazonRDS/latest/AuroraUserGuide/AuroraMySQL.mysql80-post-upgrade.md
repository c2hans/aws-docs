---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-post-upgrade.html
---

# Post-upgrade cleanup for Aurora MySQL version 3
<a name="AuroraMySQL.mysql80-post-upgrade"></a>

After you finish upgrading any Aurora MySQL version 2 clusters to Aurora MySQL version 3, you can perform these other cleanup actions:
+ Create new MySQL 8.0–compatible versions of any custom parameter groups. Apply any necessary custom parameter values to the new parameter groups.
+ Update any CloudWatch alarms, setup scripts, and so on to use the new names for any metrics whose names were affected by inclusive language changes. For a list of such metrics, see [Inclusive language changes for Aurora MySQL version 3](AuroraMySQL.Compare-v2-v3.md#AuroraMySQL.8.0-inclusive-language).
+ Update any CloudFormation templates to use the new names for any configuration parameters whose names were affected by inclusive language changes. For a list of such parameters, see [Inclusive language changes for Aurora MySQL version 3](AuroraMySQL.Compare-v2-v3.md#AuroraMySQL.8.0-inclusive-language).

## Spatial indexes
<a name="AuroraMySQL.mysql80-spatial"></a>

After upgrading to Aurora MySQL version 3, check if you need to drop or recreate objects and indexes related to spatial indexes. Before MySQL 8.0, Aurora could optimize spatial queries using indexes that didn't contain a spatial resource identifier (SRID). Aurora MySQL version 3 only uses spatial indexes containing SRIDs. During an upgrade, Aurora automatically drops any spatial indexes without SRIDs and prints warning messages in the database log. If you observe such warning messages, create new spatial indexes with SRIDs after the upgrade. For more information about changes to spatial functions and data types in MySQL 8.0, see [Changes in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html) in the *MySQL Reference Manual*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

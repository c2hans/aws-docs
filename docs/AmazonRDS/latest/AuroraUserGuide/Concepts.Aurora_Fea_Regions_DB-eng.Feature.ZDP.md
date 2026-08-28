---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.ZDP.html
---

# Supported Regions and Aurora DB engines for zero-downtime patching (ZDP)
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.ZDP"></a>

Performing upgrades for Aurora DB clusters involves the possibility of an outage when the database is shut down and while it's being upgraded. By default, if you start the upgrade while the database is busy, you lose all the connections and transactions that the DB cluster is processing. If you wait until the database is idle to perform the upgrade, you might have to wait a long time.

The zero-downtime patching (ZDP) feature attempts, on a best-effort basis, to preserve client connections through an Aurora upgrade. If ZDP completes successfully, application sessions are preserved and the database engine restarts while the upgrade is in progress. The database engine restart can cause a drop in throughput lasting for a few seconds to approximately one minute.

For detailed information on the conditions and engine versions where ZDP is available for Aurora MySQL upgrades, see [Using zero-downtime patching](AuroraMySQL.Updates.ZDP.md).

For detailed information on the conditions and engine versions where ZDP is available for Aurora PostgreSQL upgrades, see [Minor release upgrades and zero-downtime patching](USER_UpgradeDBInstance.PostgreSQL.MinorUpgrade.md#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

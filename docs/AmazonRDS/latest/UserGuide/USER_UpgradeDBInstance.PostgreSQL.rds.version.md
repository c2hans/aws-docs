---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.rds.version.html
---

# RDS version numbers in RDS for PostgreSQL
<a name="USER_UpgradeDBInstance.PostgreSQL.rds.version"></a>

RDS version numbers use the `{{major}}.{{minor}}.{{patch}}` naming scheme. An RDS patch version includes important bug fixes added to a minor version after its release. For information about RDS Extended Support version numbering, see [Amazon RDS Extended Support version naming](extended-support-versions.md#extended-support-naming).

To identify the Amazon RDS version number of your database, you must first create the `rds_tools` extension by using the following command:

```
CREATE EXTENSION rds_tools;
```

Starting with the release of PostgreSQL version 15.2-R2, you can find out the RDS version number of your RDS for PostgreSQL database with the following SQL query:

```
postgres=> SELECT rds_tools.rds_version();
```

For example, querying an RDS for PostgreSQL 15.2 database returns the following:

```
rds_version
----------------
 15.2.R2
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

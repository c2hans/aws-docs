---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.minor-version-upgrades.html
---

# Applying database minor version upgrades
<a name="sqlserver-dev-edition.minor-version-upgrades"></a>

RDS for SQL Server Developer Edition requires creating a new custom engine version (CEV) with latest cumulative update to apply database minor version upgrade. Database minor version upgrades for SQL Server Developer Edition involve the following steps:

1. Before upgrading, verify current engine version on the instance, identify the target database engine version from Amazon RDS supported versions. For information about what SQL Server versions are available on Amazon RDS, see [Working with SQL Server Developer Edition on RDS for SQL Server](sqlserver-dev-edition.md).

1. Obtain and upload installation media (ISO and CU), then [create a new custom engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.creating-cev.html).

1. Apply database minor version upgrade by using Amazon RDS [https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) with the new CEV.

   ```
   aws rds modify-db-instance \
   --db-instance-identifier <instance-id> \
   --engine-version <new-cev-version> \
   --no-apply-immediately ## use --apply-immediately for immediate update
   ```
**Note**
`--no-apply-immediately` (the default) to apply the changes during the next maintenance window.

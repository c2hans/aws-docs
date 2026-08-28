---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.ExtensionUpgrades.html
---

# Upgrading PostgreSQL extensions in RDS for PostgreSQL databases
<a name="USER_UpgradeDBInstance.PostgreSQL.ExtensionUpgrades"></a>

A PostgreSQL engine upgrade doesn't upgrade most PostgreSQL extensions. To update an extension after a version upgrade, use the `ALTER EXTENSION UPDATE` command.

**Note**
For information about updating the PostGIS extension, see [Managing spatial data with the PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.PostGIS.md) ([Step 6: Upgrade the PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.PostGIS.md#Appendix.PostgreSQL.CommonDBATasks.PostGIS.Update)).
To update the `pg_repack` extension, drop the extension and then create the new version in the upgraded database. For more information, see [pg\_repack installation](https://reorg.github.io/pg_repack/) in the `pg_repack` documentation.

To upgrade an extension, use the following command.

```
ALTER EXTENSION {{extension_name}} UPDATE TO '{{new_version}}';
```

For the list of supported versions of PostgreSQL extensions, see [Supported PostgreSQL extension versions](PostgreSQL.Concepts.General.FeatureSupport.Extensions.md).

To list your currently installed extensions, use the PostgreSQL [pg\_extension](https://www.postgresql.org/docs/current/catalog-pg-extension.html) catalog in the following command.

```
SELECT * FROM pg_extension;
```

To view a list of the specific extension versions that are available for your installation, use the PostgreSQL [ pg\_available\_extension\_versions](https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html) view in the following command.

```
SELECT * FROM pg_available_extension_versions;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rdsadmin_transport_util.html
---

# Transporting tablespaces
<a name="rdsadmin_transport_util"></a>

Use the Amazon RDS package `rdsadmin.rdsadmin_transport_util` to copy a set of tablespaces from an on-premises Oracle database to an RDS for Oracle DB instance. At the physical level, the transportable tablespace feature incrementally copies source data files and metadata files to your target instance. You can transfer the files using either Amazon EFS or Amazon S3. For more information, see [Migrating using Oracle transportable tablespaces](oracle-migrating-tts.md).

**Topics**
+ [Importing transported tablespaces to your DB instance](rdsadmin_transport_util_import_xtts_tablespaces.md)
+ [Importing transportable tablespace metadata into your DB instance](rdsadmin_transport_util_import_xtts_metadata.md)
+ [Listing orphaned files after a tablespace import](rdsadmin_transport_util_list_xtts_orphan_files.md)
+ [Deleting orphaned data files after a tablespace import](rdsadmin_transport_util_cleanup_incomplete_xtts_import.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

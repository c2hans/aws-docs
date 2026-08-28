---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.html
---

# Supported Regions and Aurora DB engines for exporting snapshot data to Amazon S3
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3"></a>

You can export Aurora DB cluster snapshot data to an Amazon S3 bucket. You can export manual snapshots and automated system snapshots. After the data is exported, you can analyze the exported data directly through tools like Amazon Athena or Amazon Redshift Spectrum. For more information, see [Exporting DB cluster snapshot data to Amazon S3](aurora-export-snapshot.md).

Exporting snapshots to S3 is available in all AWS Regions except the following:
+ Asia Pacific (Malaysia)
+ Asia Pacific (New Zealand)
+ Asia Pacific (Taipei)
+ Asia Pacific (Thailand)
+ Mexico (Central)

**Topics**
+ [Exporting snapshot data to S3 with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.ams)
+ [Exporting snapshot data to S3 with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.apg)

## Exporting snapshot data to S3 with Aurora MySQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.ams"></a>

All currently available Aurora MySQL engine versions support exporting DB cluster snapshot data to Amazon S3. For more information about versions, see [*Release Notes for Aurora MySQL*](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/Welcome.html).

## Exporting snapshot data to S3 with Aurora PostgreSQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.apg"></a>

All currently available Aurora PostgreSQL engine versions support exporting DB cluster snapshot data to Amazon S3. For more information about versions, see the [*Release Notes for Aurora PostgreSQL*](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/Welcome.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

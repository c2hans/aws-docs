---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Trino-release-history-690.html
---

# Amazon EMR 6.9.0 - Trino release notes
<a name="Trino-release-history-690"></a>

## Amazon EMR 6.9.0 - Trino new features
<a name="Trino-release-history-features-690"></a>
+ To support long running queries, Trino now includes a fault-tolerant execution mechanism. Fault-tolerant execution mitigates query failures by retrying failed queries or their component tasks.

## Amazon EMR 6.9.0 - Trino changes
<a name="Trino-release-history-changes-690"></a>

**Amazon EMR 6.9.0 - Trino changes**

| Type | Description |
| --- | --- |
| Upgrade | Trino Upgrade to 398  |
| Upgrade | Support for Hadoop 3.3.3  |
| Feature | Tardigrade support: Add support for exchange spooling on HDFS and Amazon S3.  |
| Bug fix | When Trino Iceberg is used and Glue catalog is enabled, avoid adding metastore uri in `iceberg.properties.` |

## Amazon EMR 6.9.0 - Trino known issues
<a name="Trino-release-history-known-690"></a>
+ For Amazon EMR release 6.9.0, Trino does not work on clusters enabled for Apache Ranger. If you need to use Trino with Ranger, contact [Support](https://console.aws.amazon.com/support/home#/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Flink-release-history-790.html
---

# Amazon EMR 7.9.0 - Flink release notes
<a name="Flink-release-history-790"></a>

**Amazon EMR 7.9.0 - Flink Changes**

| Type | Description |
| --- | --- |
| New Feature | Starting with Amazon EMR 7.9.0, Apache Flink provides out-of-the-box support for Avro, Parquet, and ORC file formats. You can use these formats directly with any Flink API (DataStream, Table, or SQL) without requiring any additional configuration. |
| New Feature | Starting with Amazon EMR version 7.9.0, you can enable Hive metastore or AWS Glue data catalogs more easily by using configuration settings. Add either `hive.enabled: true` or `glue.enabled: true` in the `flink-conf` classification during cluster creation to automatically configure the respective data catalog. This streamlined approach eliminates the manual configuration steps that were previously required. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

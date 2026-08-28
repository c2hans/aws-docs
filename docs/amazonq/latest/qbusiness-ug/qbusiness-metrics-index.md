---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-metrics-index.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Amazon Q Business index metrics
<a name="qbusiness-metrics-index"></a>

The following table shows the [Index](concepts-terms.md#index) metrics that Amazon Q Business sends to CloudWatch in real time.

| Metric name | Unit | Description |
| --- | --- | --- |
| `DocumentCount` | Count | The number of documents. This metric is published every 15 minutes.<br />Valid dimensions: `ApplicationId`, `IndexId` |
| `DocumentsIndexed` | Count | The number of documents that were indexed.<br />Valid dimensions: `ApplicationId`, `IndexId`, `DataSourceId` |
| `DocumentsFailedToIndex` | Count | The number of documents that failed to index.<br />Valid dimensions: `ApplicationId`, `IndexId`, `DataSourceId` |
| `DocumentsFailedToIndexDueToCDE` | Count | The number of documents that failed to index because of custom document enrichment.<br />Valid dimensions: `ApplicationId`, `IndexId`, `DataSourceId` |
| `ExtractedTextSize` | MB | Size of the extracted text<br />Valid dimensions: `ApplicationId`, `IndexId`  |
| MonthlyDataSyncDuration | Count | Duration of data synchronization operations over a monthly period.<br />Valid dimensions: `ApplicationId`, `IndexId`, `DataSourceId` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

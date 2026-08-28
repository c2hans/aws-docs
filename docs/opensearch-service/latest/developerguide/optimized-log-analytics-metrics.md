---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/optimized-log-analytics-metrics.html
---

# CloudWatch metrics
<a name="optimized-log-analytics-metrics"></a>

Amazon OpenSearch Service publishes the following CloudWatch metrics for domains running the Optimized engine. These metrics help you monitor native analytics engine performance, resource utilization, and ingestion health. For the full list of Amazon OpenSearch Service metrics, see [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](managedomains-cloudwatchmetrics.md).

| Metric | Node type | Description |
| --- | --- | --- |
| NativeMemoryPressure | Hot, Warm, Coordinator | The percentage of native (off-heap) memory in use on the node. This metric is analogous to `JVMMemoryPressure` but measures memory consumed by the native analytics engine rather than the Java heap.<br />Relevant statistics: Maximum |
| NativeRuntimeResidentMemory | Hot, Warm, Coordinator | The amount of resident memory, in bytes, consumed by the native analytics engine on the node.<br />Relevant statistics: Maximum, Average |
| NativeSearchRuntimeCPUUtilization | Hot, Warm, Coordinator | The CPU utilization, as a percentage, of the DataFusion query execution engine on the node.<br />Relevant statistics: Maximum, Average |
| ThreadpoolNativeSearchCPUQueue | Hot, Warm, Coordinator | The number of queued tasks in the native search CPU thread pool. If the queue size is consistently high, consider scaling your cluster.<br />Relevant statistics: Maximum |
| ThreadpoolNativeSearchCPUThreads | Hot, Warm, Coordinator | The size of the native search CPU thread pool.<br />Relevant statistics: Maximum |

**Note**
The following metrics don't apply to Optimized domains because OpenSearch Dashboards is not available:
`OpenSearchDashboardsHealthyNodes`
`OpensearchDashboardsReportingFailedRequestSysErrCount`
`OpensearchDashboardsReportingFailedRequestUserErrCount`
`OpensearchDashboardsReportingRequestCount`
`OpensearchDashboardsReportingSuccessCount`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

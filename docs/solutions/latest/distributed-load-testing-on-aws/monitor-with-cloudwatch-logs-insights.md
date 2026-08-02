---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/monitor-with-cloudwatch-logs-insights.html
---

# Monitor with CloudWatch Logs Insights
<a name="monitor-with-cloudwatch-logs-insights"></a>

This solution deploys four CloudWatch Logs Insights saved queries that appear in the [CloudWatch Logs Insights console](https://console.aws.amazon.com/cloudwatch/home#logsV2:logs-insights) under **Saved queries**. These queries provide visibility into test orchestration, errors, task failures, and orphan cleanup without requiring you to write custom queries.

Each query name includes the stack name and Region for identification across multiple deployments. For example: `DLT - Test Timeline [my-stack us-east-1]`.

## Using saved queries
<a name="using-saved-queries"></a>

To run a saved query:

1. Open the [CloudWatch Logs Insights console](https://console.aws.amazon.com/cloudwatch/home#logsV2:logs-insights).

1. In the left panel, expand **Saved queries**.

1. Select a query prefixed with `DLT -`.

1. If the query contains a placeholder value such as `REPLACE_WITH_TEST_RUN_ID`, replace it with the actual test run ID from your test results.

1. Choose **Run query**.

## DLT - Test Timeline
<a name="test-timeline-query"></a>

Shows the full lifecycle for a single test run across all orchestration Lambda functions. Use this query to trace the sequence of events from test creation through completion.

| Attribute | Value |
| --- | --- |
| Fields |  `@timestamp`, `logEvent`, `message`, `region`, `error`  |
| Filter |  `testRunId = "REPLACE_WITH_TEST_RUN_ID"`  |
| Sort |  `@timestamp asc`  |
| Limit | 500 |

Replace `REPLACE_WITH_TEST_RUN_ID` with the test run ID you want to investigate.

## DLT - Test Errors
<a name="test-errors-query"></a>

Shows all ERROR-level entries for a single test run across Lambda functions and ECS tasks. Use this query to identify the root cause when a test fails or produces unexpected results.

| Attribute | Value |
| --- | --- |
| Fields |  `@timestamp`, `logEvent`, `message`, `region`, `taskId`, `error`  |
| Filter |  `testRunId = "REPLACE_WITH_TEST_RUN_ID" and level = "ERROR"`  |
| Sort |  `@timestamp asc`  |

Replace `REPLACE_WITH_TEST_RUN_ID` with the test run ID you want to investigate.

## DLT - Task Failures
<a name="task-failures-query"></a>

Shows individual ECS task failures with stop codes and failure classification. Use this query to understand why specific Fargate tasks stopped during a test.

| Attribute | Value |
| --- | --- |
| Fields |  `@timestamp`, `testId`, `testRunId`, `region`, `taskArn`, `stopCode`, `exitCode`, `stopCategory`, `stoppedReason`  |
| Filter |  `logEvent = "TASK_FAILURE_DETECTED"`  |
| Sort |  `@timestamp desc`  |
| Limit | 50 |

This query does not require a test run ID — it shows all recent task failures across all test runs.

## DLT - Orphan Cleanup
<a name="orphan-cleanup-query"></a>

Shows the history of orphaned ECS service detection. Use this query to verify that the hourly orphan cleanup process is finding and removing abandoned services.

| Attribute | Value |
| --- | --- |
| Fields |  `@timestamp`, `logEvent`, `message`, `region`, `cluster`, `orphanCount`, `orphanTestIds`  |
| Filter |  `logEvent = "ORPHAN_DETECTED"`  |
| Sort |  `@timestamp desc`  |
| Limit | 50 |

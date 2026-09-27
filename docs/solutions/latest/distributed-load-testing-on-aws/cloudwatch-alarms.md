---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/cloudwatch-alarms.html
---

# CloudWatch Alarms
<a name="cloudwatch-alarms"></a>

This solution deploys two CloudWatch Alarms that monitor for operational conditions requiring attention. By default, these alarms have no notification actions configured. We recommend subscribing an Amazon SNS topic to each alarm so that operators receive immediate notification when issues occur.

## Subscribe to alarm notifications
<a name="subscribe-to-alarms"></a>

To receive notifications when an alarm fires:

1. Open the [CloudWatch Alarms console](https://console.aws.amazon.com/cloudwatch/home#alarmsV2:).

1. Search for alarms prefixed with your stack name (for example, `my-stack-OrphanCleanupFailure`).

1. Select the alarm and choose **Edit**.

1. Under **Notification**, choose **Add notification**.

1. Select or create an SNS topic with your preferred notification endpoints (email, SMS, or Lambda).

1. Choose **Update alarm**.

Repeat for each alarm.

## OrphanCleanupFailure
<a name="orphan-cleanup-failure-alarm"></a>

| Attribute | Value |
| --- | --- |
| Alarm name |  `{StackName}-OrphanCleanupFailure`  |
| Metric |  `OrphanCleanupFailures` in the `distributed-load-testing` namespace |
| Threshold | >= 1 failure within 5 minutes |
| Treat missing data | Breaching |

 **What this alarm monitors:** The solution uses three layers of defense to prevent runaway ECS services:
+  **Layer 1: Automated error handling** — The test orchestration workflow includes error handling at every step. If anything fails during provisioning, stabilization, or execution, the workflow automatically triggers cleanup to drain and delete the ECS services.
+  **Layer 2: Execution failure detection** — If the orchestration workflow itself exits unexpectedly (for example, due to a timeout or internal error that bypasses normal error handling), an EventBridge rule detects the failure and independently triggers cleanup for every Region involved in the test.
+  **Layer 3: Hourly orphan cleanup** — A scheduled process runs every hour, scans for ECS services that are not associated with any active test, and force-deletes them. This is the last-resort safety net — if both Layer 1 and Layer 2 fail, leaked services are still removed within an hour. If the orphan cleanup process itself fails, this alarm fires.

 **Why it matters:** Orphaned ECS Fargate services continue running and incurring charges with no visibility in the DLT console. Without a notification subscription, operators will only discover the problem when unexpected costs appear on the bill.

 **Recommended response:** When this alarm fires, navigate to the [Amazon ECS console](https://console.aws.amazon.com/ecs/), identify services in the DLT cluster that do not correspond to a running test, and manually delete them.

## MetricFilterCount
<a name="metric-filter-count-alarm"></a>

| Attribute | Value |
| --- | --- |
| Alarm name |  `{StackName}-MetricFilterCount-Alarm`  |
| Metric |  `MetricFilterCount` in the `distributed-load-testing` namespace |
| Threshold | >= 90 |
| Treat missing data | Not breaching |

 **What this alarm monitors:** The solution creates CloudWatch metric filters dynamically on the ECS log group to support live metrics during test execution. AWS limits each log group to 100 metric filters. This alarm fires when usage reaches 90% of that limit.

 **Why it matters:** If the limit is reached, new load test runs will fail.

 **Recommended response:** Delete test scenarios that are no longer needed. When a test scenario is deleted, the solution removes the associated metric filters and frees capacity for new tests.

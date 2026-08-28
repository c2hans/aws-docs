---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/monitoring-cloudhsm/operational-monitoring.html
---

# Operational monitoring for AWS CloudHSM
<a name="operational-monitoring"></a>

You can use [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) to monitor your AWS CloudHSM clusters in near real time. Using CloudWatch metrics, you can configure CloudWatch alarms to alert you if any of these metrics exceed the threshold you define. For more information, see [Working with Amazon CloudWatch Logs and AWS CloudHSM Audit Logs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-hsm-audit-logs-using-cloudwatch.html) and [Getting CloudWatch metrics for AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-metrics-cw.html) in the AWS CloudHSM documentation.

The section describes how to configure alarms for the following metrics, which can help you monitor the operational status of AWS CloudHSM clusters and hardware security modules (HSMs):
+ [Session keys in use](#operational-monitoring-session-keys)
+ [Token keys in use](#operational-monitoring-token-keys)
+ [Total keys in use (Recommended)](#operational-monitoring-total-keys)
+ [Open sessions (Recommended)](#operational-monitoring-open-sessions)
+ [Available users (Recommended)](#operational-monitoring-users-available)

## Session keys in use
<a name="operational-monitoring-session-keys"></a>

AWS CloudHSM [session keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/whatis-hsm-keys.html) are ephemeral encryption keys for single sessions. Session keys are deleted when the session between the application and the HSM is closed. The `HsmKeysSessionOccupied` metric shows the number of session keys that are being used by the HSM instance. Observe and set the baseline value for this metric based on the expected behavior of the application.

An [AWS CloudHSM system quota](https://docs.aws.amazon.com/cloudhsm/latest/userguide/limits.html) limits the maximum number of keys per cluster to 3,300. This quota includes session keys and token keys. If there is a bug in the application or an unexpected behavior, the total number of keys in the HSM might reach the quota. If this occurs, then the application might have an outage because it cannot create more keys.

Creating an alarm on this metric helps you detect the increase in the number of session keys before the quota is reached. This helps you resolve the issue before the application is affected. You can use this alarm if your application regularly creates session keys. We recommend that you set up this alarm for each HSM in the cluster.

If you receive an alarm for this metric, troubleshoot your application to find the reason for the large number of session keys. Optimize the logic of the application to make sure that you are using the session keys appropriately.

The following table shows the configuration values for this alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** | **Notes** |
| --- |--- |--- |
| Metric | `HsmKeysSessionOccupied` | None |
| Namespace | `AWS/CloudHSM` | None |
| Dimension | `HSM ID` and `cluster ID` | None |
| Statistic | `Maximum` | None |
| Threshold type | `Static` | None |
| Whenever duration is | `Greater/Equal` | None |
| Than | `2500` | This value should be as close as possible to the number of session keys your application uses under normal conditions. |

## Token keys in use
<a name="operational-monitoring-token-keys"></a>

AWS CloudHSM [token keys](https://docs.aws.amazon.com/cloudhsm/latest/userguide/whatis-hsm-keys.html) are persistent encryption keys for long-term use. As a security best practice, your application should delete token keys when they are no longer needed. The `HsmKeysTokenOccupied` metric shows the number of token keys that are being used by the HSM instance. Observe and set the baseline value for this metric based on the expected behavior of the application.

An [AWS CloudHSM system quota](https://docs.aws.amazon.com/cloudhsm/latest/userguide/limits.html) limits the maximum number of keys per cluster to 3,300. This quota includes session keys and token keys. If there is a bug in the application or an unexpected behavior, the total number of keys in the cluster might reach the upper limit. If this occurs, then the application might have an outage because it cannot create more keys.

Creating an alarm on this metric helps you detect the increase in the number of token keys before the quota is reached. This helps you resolve the issue before the application is affected. You can use this alarm if your application regularly creates token keys.

If you receive an alarm for this metric, troubleshoot your application to find the reason for the large number of token keys. Optimize the logic of your application to make sure that the application is deleting any unused token keys.

The following table shows the configuration values for this alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** | **Notes** |
| --- |--- |--- |
| Metric | `HsmKeysTokenOccupied` | None |
| Namespace | `AWS/CloudHSM` | None |
| Dimension | `cluster ID` | None |
| Statistic | `Maximum` | None |
| Threshold type | `Static` | None |
| Whenever duration is | `Greater/Equal` | None |
| Than | `2500` | This value should be as close as possible to the number of token keys your application uses under normal conditions. |

## Total keys in use (Recommended)
<a name="operational-monitoring-total-keys"></a>

An [AWS CloudHSM system quota](https://docs.aws.amazon.com/cloudhsm/latest/userguide/limits.html) limits the maximum number of keys per cluster to 3,300. This quota includes session keys and token keys. If there is a bug in the application or an unexpected behavior, the total number of keys might reach the upper limit. If this occurs, then the application might have an outage because it cannot create more keys.

Even if your application is not creating session keys and token keys regularly, you should monitor the total number of keys to help prevent unexpected outages. You can create an alarm on the value of a `SUM` function of the `HsmKeysTokenOccupied` and `HsmKeysSessionOccupied` metrics. We recommend that you set up this alarm for each HSM in the cluster.

The following table shows the configuration values for this alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a metric math expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** | **Notes** |
| --- |--- |--- |
| Namespace | `AWS/CloudHSM` | None |
| Dimension | `HSM ID` and `cluster ID` | None |
| Math expression | `SUM` | None |
| Metrics | `HsmKeysTokenOccupied` and `HsmKeysSessionOccupied` | None |
| Statistic | `Maximum` | None |
| Threshold type | `Static` | None |
| Whenever duration is | `Greater/Equal` | None |
| Than | `2500` | This value should be as close as possible to the number of session and token keys that your application uses under normal conditions. |

## Open sessions (Recommended)
<a name="operational-monitoring-open-sessions"></a>

The `HsmSessionCount` metric shows the number of sessions open from the AWS CloudHSM client to the HSMs in the cluster. The number of open sessions depends on the application and the rate of requests. Observe and set the baseline value for this metric based on the expected behavior of the application.

AWS CloudHSM allows up to 2,048 open connections to the HSM instance. The application may experience an outage if the session count reaches this limit. This alarm helps you monitor the session count and respond to any unexpected scenarios. It can also help you identify whether the number of HSMs in the cluster is sufficient to manage the rate of requests that the application sends.

If you receive an alert for this alarm, check whether the application is properly managing sessions.

The following table shows the configuration values for this alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** | **Notes** |
| --- |--- |--- |
| Metric | `HsmSessionCount` | None |
| Namespace | `AWS/CloudHSM` | None |
| Dimension | `cluster ID` | None |
| Statistic | `Maximum` | None |
| Threshold type | `Static` | None |
| Whenever duration is | `Greater/Equal` | None |
| Than | `1800` | This value should be as close as possible to the number of sessions required under normal conditions. |

## Available users (Recommended)
<a name="operational-monitoring-users-available"></a>

The `HsmUsersAvailable` metric shows the number of additional users that can be created in the cluster. An [AWS CloudHSM system quota](https://docs.aws.amazon.com/cloudhsm/latest/userguide/limits.html) limits the maximum number of users per cluster to 250. This alarm helps you monitor the user count so that you can create or delete users as needed. If the quota has been reached, this can affect your ability to create new users.

Observe and set the baseline value for this metric based on the frequency of user creation. If new users are needed frequently, you can increase the threshold of this alarm to receive early notification.

The following table shows the configuration values for this alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Metric | `HsmUsersAvailable` |
| Namespace | `AWS/CloudHSM` |
| Dimension | `cluster ID` |
| Statistic | `Minimum` |
| Threshold type | `Static` |
| Whenever duration is | `Greater/Equal` |
| Than | `15` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/monitoring-cloudhsm/reliability-monitoring.html
---

# Reliability and performance monitoring for AWS CloudHSM
<a name="reliability-monitoring"></a>

You can use [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) to monitor your AWS CloudHSM cluster in near real time. Using CloudWatch metrics, you can configure CloudWatch alarms to alert you if any of these metrics exceed their defined thresholds. For more information, see [Working with Amazon CloudWatch Logs and AWS CloudHSM Audit Logs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-hsm-audit-logs-using-cloudwatch.html) and [Getting CloudWatch metrics for AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-metrics-cw.html) in the AWS CloudHSM documentation.

The section describes how to configure alarms for the following metrics, which can help you monitor the reliability status of AWS CloudHSM clusters and hardware security modules (HSMs):
+ [Unhealthy HSM instance (Recommended)](#reliability-monitoring-unhealthy)
+ [HSM temperature](#reliability-monitoring-temperature)

## Unhealthy HSM instance (Recommended)
<a name="reliability-monitoring-unhealthy"></a>

The `HsmUnhealthy` metric indicates that the HSM instance is not performing properly. The baseline value for this metric is zero. If the metric is greater than zero, it means that one or more HSMs in the cluster are not working as expected. AWS CloudHSM automatically replaces unhealthy instances for you. However, all the requests that were sent to the HSM after it started behaving unexpectedly and before it is marked as unhealthy will fail.

Creating an alarm on this metric helps you validate that the unhealthy HSM instance has been successfully replaced. It also provides insights about application-reported errors that might be the result of the unhealthy HSM.

If you receive an alarm for this metric, monitor the application to make sure that it can handle failure for short duration and validate that it is still working as expected after the HSM is replaced.

The following table shows the configuration values for this alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Metric | `HsmUnhealthy` |
| Namespace | `AWS/CloudHSM` |
| Dimension | `HSM ID` and `cluster ID` |
| Statistic | `Maximum` |
| Threshold type | `Static` |
| Whenever duration is | `Greater/Equal` |
| Than | `1` |

**Note**
You cannot make an HSM unhealthy in order to test the alarm or the application performance. However, you can simulate an HSM failure by blocking and unblocking the traffic between the application and the HSM for short amount of time. To block this traffic, you can modify your [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) or [network access controls lists (Network ACLs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html).

## HSM temperature
<a name="reliability-monitoring-temperature"></a>

The `HsmTemperature` metric denotes the junction temperature of the hardware processor. The HSM becomes unhealthy if the temperature reaches 110 degrees Centigrade. An alarm for this metric can help you anticipate whether an HSM will become unhealthy.

The following table shows the configuration values for this alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Metric | `HsmTemperature` |
| Namespace | `AWS/CloudHSM` |
| Dimension | `HSM ID` and `cluster ID` |
| Statistic | `Maximum` |
| Threshold type | `Static` |
| Whenever duration is | `Greater/Equal` |
| Than | `90` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

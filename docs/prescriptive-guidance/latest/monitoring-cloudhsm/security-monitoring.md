---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/monitoring-cloudhsm/security-monitoring.html
---

# Security monitoring for AWS CloudHSM
<a name="security-monitoring"></a>

By default, AWS CloudHSM collects your HSM audit logs and sends them to Amazon CloudWatch Logs on your behalf. Security-related events are also included in this log data. We recommend that you monitor the logs for security-related events, such as the creation or deletion of certain user types or login failures.

You cannot create an alarm directly on the log stream. First, you must set up a CloudWatch Logs [metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html), and then you can create an alarm on the metric filter.

The section describes how to configure CloudWatch metric filters and alarms for the following security-related events in AWS CloudHSM:
+ [Creation of crypto officers (Recommended)](#security-monitoring-crypto-officer)
+ [Creation of crypto users (Recommended)](#security-monitoring-crypto-user)
+ [Deletion of crypto officers or crypto users (Recommended)](#security-monitoring-delete-user)
+ [Entry of incorrect user names (Recommended)](#security-monitoring-incorrect-user-name)
+ [Entry of incorrect passwords (Recommended)](#security-monitoring-incorrect-password)

This section also describes how to configure an Amazon EventBridge rule for the following security-related events in AWS CloudHSM:
+ [Security-related API calls (Recommended)](#security-monitoring-api-calls)

## Creation of crypto officers (Recommended)
<a name="security-monitoring-crypto-officer"></a>

An AWS CloudHSM [crypto officer (CO)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/understanding-users-cmu.html#crypto-officer) can perform user management operations. For example, they can create and delete users, and they can change user passwords. Therefore, it is important to track and monitor the creation of new COs so that you can detect any security risks, such as unauthorized access or over-privileged permissions.

The following table shows the configuration values for the metric filter. For instructions about how to set up a metric filter, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Pattern | `CN_CREATE_CO` |
| Log group name | <Name of the log group for the AWS CloudHSM cluster> |
| Metric name | `Event count` |
| Metric namespace | <Your custom namespace> |
| Metric value | `1` |

The following table shows the configuration values for the alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Namespace | <Custom namespace you created for the metric filter> |
| Statistic | `Maximum` |
| Threshold type | `Static` |
| Whenever duration is | `Greater/Equal` |
| Than | `1` |

## Creation of crypto users (Recommended)
<a name="security-monitoring-crypto-user"></a>

An AWS CloudHSM [crypto user (CU)](https://docs.aws.amazon.com/cloudhsm/latest/userguide/understanding-users-cmu.html#crypto-user-cmu) can perform key management and cryptographic operations on the HSM. Therefore, it is important to track and monitor the creation of new CUs so that you can detect any security risks, such as unauthorized usage of encryption keys or over-privileged permissions.

The following table shows the configuration values for the metric filter. For instructions about how to set up a metric filter, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Pattern | `CN_CREATE_USER` |
| Log group name | <Name of the log group for the AWS CloudHSM cluster> |
| Metric name | `Event count` |
| Metric namespace | <Your custom namespace> |
| Metric value | `1` |

The following table shows the configuration values for the alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Namespace | <Custom namespace you created for the metric filter> |
| Statistic | `Maximum` |
| Threshold type | `Static` |
| Whenever duration is | `Greater/Equal` |
| Than | `1` |

## Deletion of crypto officers or crypto users (Recommended)
<a name="security-monitoring-delete-user"></a>

Similar to tracking the creation of COs and CUs, it is important to track the deletion of these user types. Tracking user deletion can help you detect access issues and identify potential security breaches.

The following table shows the configuration values for the metric filter. For instructions about how to set up a metric filter, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Pattern | `CN_DELETE_USER` |
| Log group name | <Name of the log group for the AWS CloudHSM cluster> |
| Metric name | `Event count` |
| Metric namespace | <Your custom namespace> |
| Metric value | `1` |

The following table shows the configuration values for the alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Namespace | <Custom namespace you created for the metric filter> |
| Statistic | `Maximum` |
| Threshold type | `Static` |
| Whenever duration is | `Greater/Equal` |
| Than | `1` |

## Entry of incorrect user names (Recommended)
<a name="security-monitoring-incorrect-user-name"></a>

We recommend that you monitor login attempts with an incorrect user name. These can indicate that someone is trying to gain unauthorized access. To help prevent alert fatigue, the alarm is triggered if a user enters the wrong user name two or more times. You can configure this value as needed for your organization and policies.

The following table shows the configuration values for the metric filter. For instructions about how to set up a metric filter, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Pattern | `\"Error: This user doesn't exist\"` |
| Log group name | <Name of the log group for the AWS CloudHSM cluster> |
| Metric name | `Event count` |
| Metric namespace | <Your custom namespace> |
| Metric value | `1` |

The following table shows the configuration values for the alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Namespace | <Custom namespace you created for the metric filter> |
| Statistic | `Sum` |
| Threshold type | `Static` |
| Whenever duration is | `Greater/Equal` |
| Than | `2` |

## Entry of incorrect passwords (Recommended)
<a name="security-monitoring-incorrect-password"></a>

We recommend that you monitor login attempts with an incorrect password. These can indicate that someone is trying to gain unauthorized access. To help prevent alert fatigue, the alarm is triggered if a user enters the wrong password two or more times. You can configure this value as needed for your organization and policies.

The following table shows the configuration values for the metric filter. For instructions about how to set up a metric filter, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Pattern | `RET_USER_LOGIN_FAILURE` |
| Log group name | <Name of the log group for the AWS CloudHSM cluster> |
| Metric name | `Event count` |
| Metric namespace | <Your custom namespace> |
| Metric value | `1` |

The following table shows the configuration values for the alarm. For instructions about how to set up this alarm, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the CloudWatch Logs documentation.

|
|
| **Property** | **Value** |
| --- |--- |
| Namespace | <Custom namespace you created for the metric filter> |
| Statistic | `Sum` |
| Threshold type | `Static` |
| Whenever duration is | `Greater/Equal` |
| Than | `2` |

## Security-related API calls (Recommended)
<a name="security-monitoring-api-calls"></a>

Monitoring the `DeleteHsm`, `CopyBackupToRegion`, and `ModifyCluster` API calls for AWS CloudHSM can provide critical oversight of high-impact operations. These API calls can alter the security posture and operational state of the AWS CloudHSM infrastructure.

By implementing near real-time alerts for these API calls, you can promptly detect and respond to potentially unauthorized or accidental changes to HSMs and clusters. Alarms provide notification about actions that can affect cryptographic key availability, cross-Region data transfers, or cluster configurations. Vigilance is essential to maintain the integrity and availability of sensitive cryptographic operations. Alarms help you maintain compliance with security policies and facilitate rapid incident response. Ultimately, this targeted monitoring approach enhances the overall security governance of your AWS CloudHSM resources because it provides stakeholders with timely insights into critical changes that might require immediate attention or review.

AWS CloudHSM is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for AWS CloudHSM as *events*. In [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html), you can create a rule that monitors CloudTrail for events associated with the `DeleteHsm`, `CopyBackupToRegion`, and `ModifyCluster` API calls for AWS CloudHSM. You can configure a target that will receive alerts when the event occurs. We recommend that you configure an Amazon Simple Notification Service (Amazon SNS) topic because it enables near real-time alerts when these critical operations are performed.

When you create an EventBridge rule, you can customize the text that is passed to the rule target. The [input transformer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html#eb-transform-input-api) extracts specific fields from the event and formats them into a concise, informative message. The resulting alert provides immediate context about the event, including the AWS account, AWS Region, specific API call, time of the event, and the identity of the user who performed the action.

### To create the EventBridge rule
<a name="to-create-the-9999999999999999ev--rule.087f960c-1a4d-5e58-97ec-03dbd8016148"></a>

1. Follow the instructions in [Define the rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html#eb-create-rule-define) to enter a custom name and description for your rule.

1. Follow the instructions in [Build the event pattern](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html#eb-create-rule-event-pattern). Choose **Custom pattern (JSON editor)**, and then enter the following event pattern:

   ```
   {
       "source": ["aws.cloudhsm"],
       "detail-type": ["AWS API Call via CloudTrail"],
       "detail": {
           "eventSource": ["cloudhsm.amazonaws.com"],
           "eventName": ["DeleteHsm", "CopyBackupToRegion", "ModifyCluster"]
       }
   }
   ```

1. Follow the instructions in [Select targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html#eb-create-rule-target) and note the following:
   + Choose the Amazon SNS topic that will receive events that match the specified pattern.
   + Under **Additional settings**, for **Configure target input**, choose **Input transformer**.
   + Choose **Configure input transformer**.
   + In **Input path**, enter the following:

     ```
     {
         "account": "$.account",
         "region": "$.region",
         "eventName": "$.detail.eventName",
         "eventTime": "$.detail.eventTime",
         "userIdentity": "$.detail.userIdentity.arn"
     }
     ```
   + In **Template**, enter the following:

     ```
     {
         "account": <account>,
         "region": <region>,
         "message": "Critical AWS CloudHSM operation detected: <eventName> was performed at <eventTime> by <userIdentity>"
     }
     ```

1. Follow the instructions in [Configure tags and review rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html#eb-create-rule-review) to finish creating the rule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

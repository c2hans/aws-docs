---
source_url: https://docs.aws.amazon.com/iot-device-defender/latest/devguide/mitigation-action-commands.html
---

# Mitigation action commands
<a name="mitigation-action-commands"></a>

You can use these mitigation action commands to define a set of actions for your AWS account that you can later apply to one or more sets of audit findings. There are three command categories:
+ Those used to define and manage actions.
+ Those used to start and manage the application of those actions to Audit findings.
+ Those used to start and manage the application of those actions to Detect alarms.

**Mitigation action commands**

|  Define and manage actions  |  Start and manage Audit execution  |  Start and manage Detect execution  |
| --- | --- | --- |
| [CreateMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateMitigationAction.html) | [CancelAuditMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelAuditMitigationActionsTask.html) | [CancelDetectMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelDetectMitigationActionsTask4e.html)<br /> |
| [DeleteMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteMitigationAction.html) | [DescribeAuditMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditMitigationActionsTask.html) | [DescribeDetectMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDetectMitigationActionsTask.html) |
| [DescribeMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeMitigationAction.html) | [ListAuditMitigationActionsTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditMitigationActionsTasks.html) | [ListDetectMitigationActionsTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDetectMitigationActionsTasks.html) |
| [ListMitigationActions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListMitigationActions.html) | [StartAuditMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartAuditMitigationActionsTask.html) | [StartDetectMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartDetectMitigationActionsTask.html) |
| [UpdateMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateMitigationAction.html) | [ListAuditMitigationActionsExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditMitigationActionsExecutions.html) | [ListDetectMitigationActionsExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDetectMitigationActionsExecutions.html) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Device Defender. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-device-defender` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/using-the-cloudwatch-dashboard.html
---

# Using the CloudWatch dashboard
<a name="using-the-cloudwatch-dashboard"></a>

To view the dashboard:

1. Navigate to [Amazon CloudWatch](https://console.aws.amazon.com/cloudwatch/) and then Dashboards.

1. Select the dashboard named "ASR-Remediation-Metrics-Dashboard".

The CloudWatch dashboard contains the following sections:

1.  **Total Successful Remediations** - Gives you insight into the number of Security Hub findings that have been successfully remediated by the solution.

1.  **Remediation Failures** - Shows how many remediations have been failing, both in total and as a percentage, and the failure cause. A high number of failures can hint at a technical problem with the solution that you might need to investigate in more detail.

1.  **Remediation Success/Failure by Control ID** - If you enabled Enhanced Metrics at deployment time, this section lists remediation results by control ID. When the **Remediation Failures** section shows a high failure rate in general, this section shows you whether the failures are distributed across many control IDs, or if only certain control IDs are failing.

1.  **Runbook Assume Role Failures** - Shows the number of failures that occurred because of remediation attempts in accounts that don’t have the solution Member role installed. Repeated failures by automated remediation attempts due to missing roles cause unnecessary cost. Mitigate this by installing the [Member role stack](aws-cloudformation-template.md#member-roles) in the concerned accounts, [disabling all EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-delete-rule.html) created by the solution, or [disassociating the account](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-disassociate-members.html) in Security Hub.

1.  **Cloud Trail Management Actions by ASR** - Lists management actions by the solution across all member accounts where you enabled Action Logs with the **EnableCloudTrailForASRActionLog** parameter at deployment time. When you observe unexpected resource changes in any of your AWS accounts, this widget can help you understand if resources were modified by the solution.

1.  **Rollback** - If you enabled rollback with the **EnableRollback** parameter at deployment time, this section shows pre-remediation snapshot capture outcomes (captured, failed, or skipped) and rollback execution outcomes (success or failure). Use it to confirm that snapshots are being captured for rollback-eligible remediations and to spot rollbacks that fail. For more information about the feature, see [Remediation rollback](remediation-rollback.md).

The CloudWatch dashboard also comes with predefined alarms that alert to common operational errors.

1. State Machine executions > 1000 in a 24-hour period.

   1. A large spike in remediation executions could indicate an event rule is initiating more often than intended.

   1. Threshold can be changed using the CloudFormation parameter.

1. Remediation Failures by Type = NOREMEDIATION > 0

   1. Remediations are being attempted for remediations that are not included in ASR. This could indicate an event rule has been modified to include more than the intended remediations.

1. Runbook Assume Role Failures > 0

   1. Remediations are being attempted on accounts or Regions that do not have the solution properly deployed. This could indicate an event rule has been modified to include more accounts than intended.

1. Snapshot Capture Failure >= 1 (only when rollback is enabled)

   1. A pre-remediation snapshot could not be captured, so the affected remediation is not rollback-capable. The remediation still proceeds (fail-open); this alarm surfaces the loss of rollback coverage.

1. Rollback Execution Failure Rate > 20% over 15 minutes (only when rollback is enabled)

   1. More than a fifth of rollback executions failed in the window. This can indicate a broken rollback path, missing member-account permissions, or resource drift.

All alarm thresholds can be modified to suit the individual deployment needs.

![Automated Security Response on AWS Remediations Metrics Dashboard.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/asr-remediations-metrics-dashboard.png)

## Modifying alarm thresholds
<a name="modifying-alarm-thresholds"></a>

1. Navigate to [Amazon CloudWatch → Alarms → All Alarms](https://console.aws.amazon.com/cloudwatch/home#alarmsV2:).

1. Choose the Alarm you would like to modify, then choose **Actions**, and then choose **Edit**.

![CloudWatch Alarms console showing ASR solution alarm states](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/cloudwatch-alarm-list.png)

1. Change the threshold to the desired value and save.

![Edit alarm dialog with threshold value and condition fields](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/edit-options-for-alarms.png)

1. Navigate to the [CloudWatch dashboard](https://console.aws.amazon.com/cloudwatch/home#dashboards:) to modify the charts there to match the new settings.

   1. Choose the ellipsis on the top right of the corresponding widget.

   1. Choose **Edit**.

   1. Choose the **Options** tab.

   1. Modify the Alarm annotation to match the new settings.

![Widget editor Options tab with horizontal annotation settings](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/modify-dashboard-widget.png)

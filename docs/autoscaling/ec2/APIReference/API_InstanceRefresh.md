---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRefresh.html
---

# InstanceRefresh
<a name="API_InstanceRefresh"></a>

Describes an instance refresh for an Auto Scaling group.

## Contents
<a name="API_InstanceRefresh_Contents"></a>

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** DesiredConfiguration **
Describes the desired configuration for the instance refresh.
Type: [DesiredConfiguration](API_DesiredConfiguration.md) object
Required: No

 ** EndTime **
The date and time at which the instance refresh ended.
Type: Timestamp
Required: No

 ** InstanceRefreshId **
The instance refresh ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** InstancesToUpdate **
The number of instances remaining to update before the instance refresh is complete.
If you roll back the instance refresh, `InstancesToUpdate` shows you the number of instances that were not yet updated by the instance refresh. Therefore, these instances don't need to be replaced as part of the rollback.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PercentageComplete **
The percentage of the instance refresh that is complete. For each instance replacement, Amazon EC2 Auto Scaling tracks the instance's health status and warm-up time. When the instance's health status changes to healthy and the specified warm-up time passes, the instance is considered updated and is added to the percentage complete.
 `PercentageComplete` does not include instances that are replaced during a rollback. This value gradually goes back down to zero during a rollback.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Preferences **
The preferences for an instance refresh.
Type: [RefreshPreferences](API_RefreshPreferences.md) object
Required: No

 ** ProgressDetails **
Additional progress details for an Auto Scaling group that has a warm pool.
Type: [InstanceRefreshProgressDetails](API_InstanceRefreshProgressDetails.md) object
Required: No

 ** RollbackDetails **
The rollback details.
Type: [RollbackDetails](API_RollbackDetails.md) object
Required: No

 ** StartTime **
The date and time at which the instance refresh began.
Type: Timestamp
Required: No

 ** Status **
The current status for the instance refresh operation:
+  `Pending` - The request was created, but the instance refresh has not started.
+  `InProgress` - An instance refresh is in progress.
+  `Successful` - An instance refresh completed successfully.
+  `Failed` - An instance refresh failed to complete. You can troubleshoot using the status reason and the scaling activities.
+  `Cancelling` - An ongoing instance refresh is being cancelled.
+  `Cancelled` - The instance refresh is cancelled.
+  `RollbackInProgress` - An instance refresh is being rolled back.
+  `RollbackFailed` - The rollback failed to complete. You can troubleshoot using the status reason and the scaling activities.
+  `RollbackSuccessful` - The rollback completed successfully.
+  `Baking` - Waiting the specified bake time after an instance refresh has finished updating instances.
Type: String
Valid Values: `Pending | InProgress | Successful | Failed | Cancelling | Cancelled | RollbackInProgress | RollbackFailed | RollbackSuccessful | Baking`
Required: No

 ** StatusReason **
The explanation for the specific status assigned to this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Strategy **
 The strategy to use for the instance refresh. This determines how instances in the Auto Scaling group are updated. Default is Rolling.
+  `Rolling` – Terminates instances and launches replacements in batches
+  `ReplaceRootVolume` – Updates instances by replacing only the root volume without terminating the instance
Type: String
Valid Values: `Rolling | ReplaceRootVolume`
Required: No

## See Also
<a name="API_InstanceRefresh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/InstanceRefresh)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/InstanceRefresh)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/InstanceRefresh)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

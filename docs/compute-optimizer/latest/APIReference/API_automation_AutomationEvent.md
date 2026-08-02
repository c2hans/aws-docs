---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AutomationEvent.html
---

# AutomationEvent
<a name="API_automation_AutomationEvent"></a>

 Contains information about an automation event.

## Contents
<a name="API_automation_AutomationEvent_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-automation_AutomationEvent-accountId"></a>
 The AWS account ID associated with the automation event.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** completedTimestamp **   <a name="computeoptimizer-Type-automation_AutomationEvent-completedTimestamp"></a>
 The timestamp when the automation event completed.
Type: Timestamp
Required: No

 ** createdTimestamp **   <a name="computeoptimizer-Type-automation_AutomationEvent-createdTimestamp"></a>
The timestamp when the automation event was created.
Type: Timestamp
Required: No

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-automation_AutomationEvent-estimatedMonthlySavings"></a>
 The estimated monthly cost savings associated with this automation event.
Type: [EstimatedMonthlySavings](API_automation_EstimatedMonthlySavings.md) object
Required: No

 ** eventDescription **   <a name="computeoptimizer-Type-automation_AutomationEvent-eventDescription"></a>
 A description of the automation event.
Type: String
Required: No

 ** eventId **   <a name="computeoptimizer-Type-automation_AutomationEvent-eventId"></a>
 The unique identifier for the automation event.
Type: String
Pattern: `[0-9A-Za-z]{16}`
Required: No

 ** eventStatus **   <a name="computeoptimizer-Type-automation_AutomationEvent-eventStatus"></a>
 The current status of the automation event.
Type: String
Valid Values: `Ready | InProgress | Complete | Failed | Cancelled | RollbackReady | RollbackInProgress | RollbackComplete | RollbackFailed`
Required: No

 ** eventStatusReason **   <a name="computeoptimizer-Type-automation_AutomationEvent-eventStatusReason"></a>
 The reason for the current event status.
Type: String
Required: No

 ** eventType **   <a name="computeoptimizer-Type-automation_AutomationEvent-eventType"></a>
 The type of automation event.
Type: String
Valid Values: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`
Required: No

 ** recommendedActionId **   <a name="computeoptimizer-Type-automation_AutomationEvent-recommendedActionId"></a>
 The ID of the recommended action associated with this automation event.
Type: String
Pattern: `[0-9A-Za-z]{16}`
Required: No

 ** region **   <a name="computeoptimizer-Type-automation_AutomationEvent-region"></a>
 The AWS Region where the automation event occurred.
Type: String
Required: No

 ** resourceArn **   <a name="computeoptimizer-Type-automation_AutomationEvent-resourceArn"></a>
 The Amazon Resource Name (ARN) of the resource affected by the automation event.
Type: String
Pattern: `arn:aws[a-z0-9-]*:[a-z0-9-]+:[a-z0-9-]*:[0-9]{0,12}:[a-zA-Z0-9/_.-]+`
Required: No

 ** resourceId **   <a name="computeoptimizer-Type-automation_AutomationEvent-resourceId"></a>
 The ID of the resource affected by the automation event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** resourceType **   <a name="computeoptimizer-Type-automation_AutomationEvent-resourceType"></a>
 The type of resource affected by the automation event.
Type: String
Valid Values: `EbsVolume`
Required: No

 ** ruleId **   <a name="computeoptimizer-Type-automation_AutomationEvent-ruleId"></a>
 The ID of the automation rule that triggered this event.
Type: String
Pattern: `[0-9A-Za-z]{16}`
Required: No

## See Also
<a name="API_automation_AutomationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/AutomationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/AutomationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/AutomationEvent)

---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AutomationEventStep.html
---

# AutomationEventStep
<a name="API_automation_AutomationEventStep"></a>

 Contains information about a step in an automation event.

## Contents
<a name="API_automation_AutomationEventStep_Contents"></a>

 ** completedTimestamp **   <a name="computeoptimizer-Type-automation_AutomationEventStep-completedTimestamp"></a>
The timestamp when this automation event step completed execution.
Type: Timestamp
Required: No

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-automation_AutomationEventStep-estimatedMonthlySavings"></a>
 Contains information about estimated monthly cost savings.
Type: [EstimatedMonthlySavings](API_automation_EstimatedMonthlySavings.md) object
Required: No

 ** eventId **   <a name="computeoptimizer-Type-automation_AutomationEventStep-eventId"></a>
 The ID of the automation event this step belongs to.
Type: String
Pattern: `[0-9A-Za-z]{16}`
Required: No

 ** resourceId **   <a name="computeoptimizer-Type-automation_AutomationEventStep-resourceId"></a>
The unique identifier of the resource being acted upon in this step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** startTimestamp **   <a name="computeoptimizer-Type-automation_AutomationEventStep-startTimestamp"></a>
The timestamp when this automation event step started execution.
Type: Timestamp
Required: No

 ** stepId **   <a name="computeoptimizer-Type-automation_AutomationEventStep-stepId"></a>
 The unique identifier for this step.
Type: String
Pattern: `[0-9A-Za-z]{16}`
Required: No

 ** stepStatus **   <a name="computeoptimizer-Type-automation_AutomationEventStep-stepStatus"></a>
 The current status of the step.
Type: String
Valid Values: `Ready | InProgress | Complete | Failed`
Required: No

 ** stepType **   <a name="computeoptimizer-Type-automation_AutomationEventStep-stepType"></a>
 The type of step.
Type: String
Valid Values: `CreateEbsSnapshot | DeleteEbsVolume | ModifyEbsVolume | CreateEbsVolume`
Required: No

## See Also
<a name="API_automation_AutomationEventStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/AutomationEventStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/AutomationEventStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/AutomationEventStep)

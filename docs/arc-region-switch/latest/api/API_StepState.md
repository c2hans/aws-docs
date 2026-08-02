---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_StepState.html
---

# StepState
<a name="API_StepState"></a>

Represents the state of a step in a plan execution.

## Contents
<a name="API_StepState_Contents"></a>

 ** endTime **   <a name="regionswitch-Type-StepState-endTime"></a>
The timestamp when a step endeded execution.
Type: Timestamp
Required: No

 ** name **   <a name="regionswitch-Type-StepState-name"></a>
The name of a step in a workflow.
Type: String
Required: No

 ** startTime **   <a name="regionswitch-Type-StepState-startTime"></a>
The timestamp when a step started execution.
Type: Timestamp
Required: No

 ** status **   <a name="regionswitch-Type-StepState-status"></a>
The status of a step in a workflow. For example, a status might be Completed or Pending Approval.
Type: String
Valid Values: `notStarted | running | failed | completed | canceled | skipped | pendingApproval`
Required: No

 ** stepMode **   <a name="regionswitch-Type-StepState-stepMode"></a>
The mode for a step execution. The mode can be Graceful or Ungraceful.
Type: String
Valid Values: `graceful | ungraceful`
Required: No

## See Also
<a name="API_StepState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/StepState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/StepState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/StepState)

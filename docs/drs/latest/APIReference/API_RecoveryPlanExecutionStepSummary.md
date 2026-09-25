---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryPlanExecutionStepSummary.html
---

# RecoveryPlanExecutionStepSummary
<a name="API_RecoveryPlanExecutionStepSummary"></a>

Summary information about a Recovery Plan execution step.

## Contents
<a name="API_RecoveryPlanExecutionStepSummary_Contents"></a>

 ** configuration **   <a name="drs-Type-RecoveryPlanExecutionStepSummary-configuration"></a>
The type-specific configuration of the execution step.
Type: [RecoveryPlanExecutionStepConfiguration](API_RecoveryPlanExecutionStepConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** recoveryPlanExecutionStepArn **   <a name="drs-Type-RecoveryPlanExecutionStepSummary-recoveryPlanExecutionStepArn"></a>
The ARN of the execution step.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:drs:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9_/.-]+`
Required: Yes

 ** status **   <a name="drs-Type-RecoveryPlanExecutionStepSummary-status"></a>
The status of the execution step.
Type: String
Valid Values: `NOT_STARTED | EXECUTING | WAITING | COMPLETED | FAILED | TIMED_OUT | SKIPPED`
Required: Yes

 ** stepIndex **   <a name="drs-Type-RecoveryPlanExecutionStepSummary-stepIndex"></a>
The 1-based position of the step within the Recovery Plan execution.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: Yes

 ** stepName **   <a name="drs-Type-RecoveryPlanExecutionStepSummary-stepName"></a>
The name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _-]*`
Required: Yes

 ** errorDetail **   <a name="drs-Type-RecoveryPlanExecutionStepSummary-errorDetail"></a>
Error details if the step failed.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

## See Also
<a name="API_RecoveryPlanExecutionStepSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryPlanExecutionStepSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryPlanExecutionStepSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryPlanExecutionStepSummary)

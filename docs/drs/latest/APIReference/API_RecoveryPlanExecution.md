---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryPlanExecution.html
---

# RecoveryPlanExecution
<a name="API_RecoveryPlanExecution"></a>

A Recovery Plan execution.

## Contents
<a name="API_RecoveryPlanExecution_Contents"></a>

 ** mode **   <a name="drs-Type-RecoveryPlanExecution-mode"></a>
The execution mode.
Type: String
Valid Values: `DRILL | RECOVERY`
Required: Yes

 ** recoveryPlanArn **   <a name="drs-Type-RecoveryPlanExecution-recoveryPlanArn"></a>
The ARN of the Recovery Plan being executed.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:drs:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9_/.-]+`
Required: Yes

 ** recoveryPlanExecutionArn **   <a name="drs-Type-RecoveryPlanExecution-recoveryPlanExecutionArn"></a>
The ARN of the Recovery Plan execution.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:drs:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9_/.-]+`
Required: Yes

 ** startedAt **   <a name="drs-Type-RecoveryPlanExecution-startedAt"></a>
The timestamp when the execution started.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: Yes

 ** status **   <a name="drs-Type-RecoveryPlanExecution-status"></a>
The execution status.
Type: String
Valid Values: `CREATED | IN_PROGRESS | COMPLETED | FAILED | CANCELLING | CANCELLED`
Required: Yes

 ** completedAt **   <a name="drs-Type-RecoveryPlanExecution-completedAt"></a>
The timestamp when the execution completed.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** errorDetail **   <a name="drs-Type-RecoveryPlanExecution-errorDetail"></a>
Error details if the execution failed.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** tags **   <a name="drs-Type-RecoveryPlanExecution-tags"></a>
The tags associated with the Recovery Plan execution.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_RecoveryPlanExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryPlanExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryPlanExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryPlanExecution)

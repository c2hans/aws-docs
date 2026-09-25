---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryPlanStep.html
---

# RecoveryPlanStep
<a name="API_RecoveryPlanStep"></a>

A Recovery Plan Step resource.

## Contents
<a name="API_RecoveryPlanStep_Contents"></a>

 ** configuration **   <a name="drs-Type-RecoveryPlanStep-configuration"></a>
The type-specific configuration of the step.
Type: [RecoveryPlanStepConfiguration](API_RecoveryPlanStepConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="drs-Type-RecoveryPlanStep-createdAt"></a>
The timestamp when the step was created.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: Yes

 ** recoveryPlanStepArn **   <a name="drs-Type-RecoveryPlanStep-recoveryPlanStepArn"></a>
The ARN of the Recovery Plan step.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:drs:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9_/.-]+`
Required: Yes

 ** stepName **   <a name="drs-Type-RecoveryPlanStep-stepName"></a>
The name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _-]*`
Required: Yes

 ** stepOrder **   <a name="drs-Type-RecoveryPlanStep-stepOrder"></a>
The 1-based position of the step within the Recovery Plan.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: Yes

 ** updatedAt **   <a name="drs-Type-RecoveryPlanStep-updatedAt"></a>
The timestamp when the step was last updated.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: Yes

## See Also
<a name="API_RecoveryPlanStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryPlanStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryPlanStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryPlanStep)

---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryPlanSummary.html
---

# RecoveryPlanSummary
<a name="API_RecoveryPlanSummary"></a>

Summary information about a Recovery Plan.

## Contents
<a name="API_RecoveryPlanSummary_Contents"></a>

 ** createdAt **   <a name="drs-Type-RecoveryPlanSummary-createdAt"></a>
The timestamp when the Recovery Plan was created.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: Yes

 ** name **   <a name="drs-Type-RecoveryPlanSummary-name"></a>
The name of the Recovery Plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _-]*`
Required: Yes

 ** recoveryPlanArn **   <a name="drs-Type-RecoveryPlanSummary-recoveryPlanArn"></a>
The ARN of the Recovery Plan.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:drs:[a-z0-9-]+:[0-9]{12}:[a-zA-Z0-9_/.-]+`
Required: Yes

 ** status **   <a name="drs-Type-RecoveryPlanSummary-status"></a>
The status of the Recovery Plan.
Type: String
Valid Values: `ACTIVE | INVALID`
Required: Yes

 ** updatedAt **   <a name="drs-Type-RecoveryPlanSummary-updatedAt"></a>
The timestamp when the Recovery Plan was last updated.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: Yes

## See Also
<a name="API_RecoveryPlanSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryPlanSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryPlanSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryPlanSummary)

---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationStep.html
---

# RemediationStep
<a name="API_RemediationStep"></a>

A step in the remediation guidance.

## Contents
<a name="API_RemediationStep_Contents"></a>

 ** Action **   <a name="securityhub-Type-RemediationStep-Action"></a>
The action to be taken for this step.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Description **   <a name="securityhub-Type-RemediationStep-Description"></a>
A description of what the step does.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Phase **   <a name="securityhub-Type-RemediationStep-Phase"></a>
The phase of the remediation plan that this step belongs to (for example, `FIX`).
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Service **   <a name="securityhub-Type-RemediationStep-Service"></a>
Which service this step is performed in.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Inverse **   <a name="securityhub-Type-RemediationStep-Inverse"></a>
The inverse of the step, to be used if the step needs to be rolled back.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Logic **   <a name="securityhub-Type-RemediationStep-Logic"></a>
The logic behind the existence of this step.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VerifyAfter **   <a name="securityhub-Type-RemediationStep-VerifyAfter"></a>
The action to take after the step to verify its success.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RemediationStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationStep)

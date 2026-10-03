---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationGuidanceContext.html
---

# RemediationGuidanceContext
<a name="API_RemediationGuidanceContext"></a>

The context behind the remediation target's existence and guidance.

## Contents
<a name="API_RemediationGuidanceContext_Contents"></a>

 ** AffectedScope **   <a name="securityhub-Type-RemediationGuidanceContext-AffectedScope"></a>
The scope of the resources affected by the resolution of the remediation target.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Prerequisites **   <a name="securityhub-Type-RemediationGuidanceContext-Prerequisites"></a>
An array of prerequisite steps in resolving the remediation target.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Pattern: `.*\S.*`
Required: No

 ** ProblemStatement **   <a name="securityhub-Type-RemediationGuidanceContext-ProblemStatement"></a>
Explains the cause which directly created the remediation target.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RiskAssessment **   <a name="securityhub-Type-RemediationGuidanceContext-RiskAssessment"></a>
An assessment of the existing risk the remediation target creates.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RemediationGuidanceContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationGuidanceContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationGuidanceContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationGuidanceContext)

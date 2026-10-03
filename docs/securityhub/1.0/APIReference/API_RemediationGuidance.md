---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationGuidance.html
---

# RemediationGuidance
<a name="API_RemediationGuidance"></a>

A remediation guidebook outlining guidance in resolving the remediation target.

## Contents
<a name="API_RemediationGuidance_Contents"></a>

 ** Context **   <a name="securityhub-Type-RemediationGuidance-Context"></a>
The context behind the remediation target's existence and guidance.
Type: [RemediationGuidanceContext](API_RemediationGuidanceContext.md) object
Required: Yes

 ** Examples **   <a name="securityhub-Type-RemediationGuidance-Examples"></a>
Provided remediation guidance examples in different formats that can be run for remediating the target.
Type: [RemediationGuidanceExamples](API_RemediationGuidanceExamples.md) object
Required: Yes

 ** Metadata **   <a name="securityhub-Type-RemediationGuidance-Metadata"></a>
The metadata of the remediation guidance.
Type: [RemediationGuidanceMetadata](API_RemediationGuidanceMetadata.md) object
Required: Yes

 ** Pattern **   <a name="securityhub-Type-RemediationGuidance-Pattern"></a>
The remediation pattern of the remediation target.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Specification **   <a name="securityhub-Type-RemediationGuidance-Specification"></a>
The specification of the remediation target guidance. This outlines required resource parameters and permissions, remediation steps, and the end state.
Type: [RemediationGuidanceSpecification](API_RemediationGuidanceSpecification.md) object
Required: Yes

 ** TargetTypeName **   <a name="securityhub-Type-RemediationGuidance-TargetTypeName"></a>
The name of the remediation target type.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Version **   <a name="securityhub-Type-RemediationGuidance-Version"></a>
The guidance version.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_RemediationGuidance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationGuidance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationGuidance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationGuidance)

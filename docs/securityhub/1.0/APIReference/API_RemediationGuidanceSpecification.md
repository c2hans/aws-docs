---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationGuidanceSpecification.html
---

# RemediationGuidanceSpecification
<a name="API_RemediationGuidanceSpecification"></a>

The specification of the remediation target guidance. This outlines required resource parameters and permissions, remediation steps, and the end state.

## Contents
<a name="API_RemediationGuidanceSpecification_Contents"></a>

 ** ExpectedEndState **   <a name="securityhub-Type-RemediationGuidanceSpecification-ExpectedEndState"></a>
The expected end state of the associated resources after completion of the steps.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Parameters **   <a name="securityhub-Type-RemediationGuidanceSpecification-Parameters"></a>
An array of the parameters used in running the steps provided.
Type: Array of [RemediationParameter](API_RemediationParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** RequiredPermissions **   <a name="securityhub-Type-RemediationGuidanceSpecification-RequiredPermissions"></a>
An array of required permissions to run the steps.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Pattern: `.*\S.*`
Required: No

 ** Steps **   <a name="securityhub-Type-RemediationGuidanceSpecification-Steps"></a>
An array of ordered steps for resolving the remediation targets.
Type: Array of [RemediationStep](API_RemediationStep.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_RemediationGuidanceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationGuidanceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationGuidanceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationGuidanceSpecification)

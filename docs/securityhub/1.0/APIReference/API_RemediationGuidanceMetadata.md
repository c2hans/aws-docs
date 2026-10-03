---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationGuidanceMetadata.html
---

# RemediationGuidanceMetadata
<a name="API_RemediationGuidanceMetadata"></a>

The metadata of the remediation guidance.

## Contents
<a name="API_RemediationGuidanceMetadata_Contents"></a>

 ** ExposureType **   <a name="securityhub-Type-RemediationGuidanceMetadata-ExposureType"></a>
The exposure type of the related exposure findings.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** FixEffect **   <a name="securityhub-Type-RemediationGuidanceMetadata-FixEffect"></a>
When the fix takes effect, for example `Immediate` or `Deferred`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResourceType **   <a name="securityhub-Type-RemediationGuidanceMetadata-ResourceType"></a>
The resource type of the remediation target.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Reversibility **   <a name="securityhub-Type-RemediationGuidanceMetadata-Reversibility"></a>
The extent to which changes made in accordance with the guidance can be reversed, for example `Fully reversible`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** RiskLevel **   <a name="securityhub-Type-RemediationGuidanceMetadata-RiskLevel"></a>
The risk when implementing the guidance provided.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** TraitTitles **   <a name="securityhub-Type-RemediationGuidanceMetadata-TraitTitles"></a>
The titles of traits this guidance applies to.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Pattern: `.*\S.*`
Required: Yes

 ** AutomationLevel **   <a name="securityhub-Type-RemediationGuidanceMetadata-AutomationLevel"></a>
The extent to which the guidance can be automated, for example `Full`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** GeneratedAt **   <a name="securityhub-Type-RemediationGuidanceMetadata-GeneratedAt"></a>
Timestamp of when the guidance was generated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

 ** HumanReviewRequired **   <a name="securityhub-Type-RemediationGuidanceMetadata-HumanReviewRequired"></a>
Specifies whether human review is required.
Type: Boolean
Required: No

 ** VerificationStatus **   <a name="securityhub-Type-RemediationGuidanceMetadata-VerificationStatus"></a>
Verification status of the guidance.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RemediationGuidanceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationGuidanceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationGuidanceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationGuidanceMetadata)

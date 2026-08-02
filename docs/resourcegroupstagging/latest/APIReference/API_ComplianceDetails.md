---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_ComplianceDetails.html
---

# ComplianceDetails
<a name="API_ComplianceDetails"></a>

Information that shows whether a resource is compliant with the effective tag policy, including details on any noncompliant tag keys.

## Contents
<a name="API_ComplianceDetails_Contents"></a>

 ** ComplianceStatus **   <a name="resourcegrouptagging-Type-ComplianceDetails-ComplianceStatus"></a>
Whether a resource is compliant with the effective tag policy.
Type: Boolean
Required: No

 ** KeysWithNoncompliantValues **   <a name="resourcegrouptagging-Type-ComplianceDetails-KeysWithNoncompliantValues"></a>
These are keys defined in the effective policy that are on the resource with either incorrect case treatment or noncompliant values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

 ** MissingTagKeys **   <a name="resourcegrouptagging-Type-ComplianceDetails-MissingTagKeys"></a>
These tag keys are defined as required in the `report_required_tag_for` block of the effective tag policy, but are missing from the resource.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

 ** NoncompliantKeys **   <a name="resourcegrouptagging-Type-ComplianceDetails-NoncompliantKeys"></a>
These tag keys on the resource are noncompliant with the effective tag policy.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_ComplianceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/ComplianceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/ComplianceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/ComplianceDetails)

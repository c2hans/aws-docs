---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsIamGroupDetails.html
---

# AwsIamGroupDetails
<a name="API_AwsIamGroupDetails"></a>

Contains details about an IAM group.

## Contents
<a name="API_AwsIamGroupDetails_Contents"></a>

 ** AttachedManagedPolicies **   <a name="securityhub-Type-AwsIamGroupDetails-AttachedManagedPolicies"></a>
A list of the managed policies that are attached to the IAM group.
Type: Array of [AwsIamAttachedManagedPolicy](API_AwsIamAttachedManagedPolicy.md) objects
Required: No

 ** CreateDate **   <a name="securityhub-Type-AwsIamGroupDetails-CreateDate"></a>
Indicates when the IAM group was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** GroupId **   <a name="securityhub-Type-AwsIamGroupDetails-GroupId"></a>
The identifier of the IAM group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** GroupName **   <a name="securityhub-Type-AwsIamGroupDetails-GroupName"></a>
The name of the IAM group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** GroupPolicyList **   <a name="securityhub-Type-AwsIamGroupDetails-GroupPolicyList"></a>
The list of inline policies that are embedded in the group.
Type: Array of [AwsIamGroupPolicy](API_AwsIamGroupPolicy.md) objects
Required: No

 ** Path **   <a name="securityhub-Type-AwsIamGroupDetails-Path"></a>
The path to the group.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsIamGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsIamGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsIamGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsIamGroupDetails)

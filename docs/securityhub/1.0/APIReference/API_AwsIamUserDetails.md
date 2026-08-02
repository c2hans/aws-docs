---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsIamUserDetails.html
---

# AwsIamUserDetails
<a name="API_AwsIamUserDetails"></a>

Information about an IAM user.

## Contents
<a name="API_AwsIamUserDetails_Contents"></a>

 ** AttachedManagedPolicies **   <a name="securityhub-Type-AwsIamUserDetails-AttachedManagedPolicies"></a>
A list of the managed policies that are attached to the user.
Type: Array of [AwsIamAttachedManagedPolicy](API_AwsIamAttachedManagedPolicy.md) objects
Required: No

 ** CreateDate **   <a name="securityhub-Type-AwsIamUserDetails-CreateDate"></a>
Indicates when the user was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** GroupList **   <a name="securityhub-Type-AwsIamUserDetails-GroupList"></a>
A list of IAM groups that the user belongs to.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Path **   <a name="securityhub-Type-AwsIamUserDetails-Path"></a>
The path to the user.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PermissionsBoundary **   <a name="securityhub-Type-AwsIamUserDetails-PermissionsBoundary"></a>
The permissions boundary for the user.
Type: [AwsIamPermissionsBoundary](API_AwsIamPermissionsBoundary.md) object
Required: No

 ** UserId **   <a name="securityhub-Type-AwsIamUserDetails-UserId"></a>
The unique identifier for the user.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserName **   <a name="securityhub-Type-AwsIamUserDetails-UserName"></a>
The name of the user.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserPolicyList **   <a name="securityhub-Type-AwsIamUserDetails-UserPolicyList"></a>
The list of inline policies that are embedded in the user.
Type: Array of [AwsIamUserPolicy](API_AwsIamUserPolicy.md) objects
Required: No

## See Also
<a name="API_AwsIamUserDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsIamUserDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsIamUserDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsIamUserDetails)

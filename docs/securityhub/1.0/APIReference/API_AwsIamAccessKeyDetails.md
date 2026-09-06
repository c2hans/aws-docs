---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsIamAccessKeyDetails.html
---

# AwsIamAccessKeyDetails
<a name="API_AwsIamAccessKeyDetails"></a>

IAM access key details related to a finding.

## Contents
<a name="API_AwsIamAccessKeyDetails_Contents"></a>

 ** AccessKeyId **   <a name="securityhub-Type-AwsIamAccessKeyDetails-AccessKeyId"></a>
The identifier of the access key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AccountId **   <a name="securityhub-Type-AwsIamAccessKeyDetails-AccountId"></a>
The AWS account ID of the account for the key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedAt **   <a name="securityhub-Type-AwsIamAccessKeyDetails-CreatedAt"></a>
Indicates when the IAM access key was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** PrincipalId **   <a name="securityhub-Type-AwsIamAccessKeyDetails-PrincipalId"></a>
The ID of the principal associated with an access key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PrincipalName **   <a name="securityhub-Type-AwsIamAccessKeyDetails-PrincipalName"></a>
The name of the principal.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PrincipalType **   <a name="securityhub-Type-AwsIamAccessKeyDetails-PrincipalType"></a>
The type of principal associated with an access key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SessionContext **   <a name="securityhub-Type-AwsIamAccessKeyDetails-SessionContext"></a>
Information about the session that the key was used for.
Type: [AwsIamAccessKeySessionContext](API_AwsIamAccessKeySessionContext.md) object
Required: No

 ** Status **   <a name="securityhub-Type-AwsIamAccessKeyDetails-Status"></a>
The status of the IAM access key related to a finding.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** UserName **   <a name="securityhub-Type-AwsIamAccessKeyDetails-UserName"></a>
 *This member has been deprecated.*
The user associated with the IAM access key related to a finding.
The `UserName` parameter has been replaced with the `PrincipalName` parameter because access keys can also be assigned to principals that are not IAM users.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsIamAccessKeyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsIamAccessKeyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsIamAccessKeyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsIamAccessKeyDetails)

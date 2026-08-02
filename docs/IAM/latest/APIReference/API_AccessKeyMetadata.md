---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AccessKeyMetadata.html
---

# AccessKeyMetadata
<a name="API_AccessKeyMetadata"></a>

Contains information about an AWS access key, without its secret key.

This data type is used as a response element in the [ListAccessKeys](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html) operation.

## Contents
<a name="API_AccessKeyMetadata_Contents"></a>

 ** AccessKeyId **
The ID for this access key.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: No

 ** CreateDate **
The date when the access key was created.
Type: Timestamp
Required: No

 ** Status **
The status of the access key. `Active` means that the key is valid for API calls; `Inactive` means it is not.
Type: String
Valid Values: `Active | Inactive | Expired`
Required: No

 ** UserName **
The name of the IAM user that the key is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

## See Also
<a name="API_AccessKeyMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/AccessKeyMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/AccessKeyMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/AccessKeyMetadata)

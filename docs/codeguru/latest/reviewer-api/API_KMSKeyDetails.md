---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_KMSKeyDetails.html
---

# KMSKeyDetails
<a name="API_KMSKeyDetails"></a>

An object that contains:
+ The encryption option for a repository association. It is either owned by AWS Key Management Service (KMS) (`AWS_OWNED_CMK`) or customer managed (`CUSTOMER_MANAGED_CMK`).
+ The ID of the AWS KMS key that is associated with a repository association.

## Contents
<a name="API_KMSKeyDetails_Contents"></a>

 ** EncryptionOption **   <a name="reviewer-Type-KMSKeyDetails-EncryptionOption"></a>
The encryption option for a repository association. It is either owned by AWS Key Management Service (KMS) (`AWS_OWNED_CMK`) or customer managed (`CUSTOMER_MANAGED_CMK`).
Type: String
Valid Values: `AWS_OWNED_CMK | CUSTOMER_MANAGED_CMK`
Required: No

 ** KMSKeyId **   <a name="reviewer-Type-KMSKeyDetails-KMSKeyId"></a>
The ID of the AWS KMS key that is associated with a repository association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_KMSKeyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/KMSKeyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/KMSKeyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/KMSKeyDetails)

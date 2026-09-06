---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_KmsGrantConfiguration.html
---

# KmsGrantConfiguration
<a name="API_KmsGrantConfiguration"></a>

A proposed grant configuration for a KMS key. For more information, see [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html).

## Contents
<a name="API_KmsGrantConfiguration_Contents"></a>

 ** granteePrincipal **   <a name="accessanalyzer-Type-KmsGrantConfiguration-granteePrincipal"></a>
The principal that is given permission to perform the operations that the grant permits.
Type: String
Required: Yes

 ** issuingAccount **   <a name="accessanalyzer-Type-KmsGrantConfiguration-issuingAccount"></a>
 The AWS account under which the grant was issued. The account is used to propose AWS KMS grants issued by accounts other than the owner of the key.
Type: String
Required: Yes

 ** operations **   <a name="accessanalyzer-Type-KmsGrantConfiguration-operations"></a>
A list of operations that the grant permits.
Type: Array of strings
Valid Values: `CreateGrant | Decrypt | DescribeKey | Encrypt | GenerateDataKey | GenerateDataKeyPair | GenerateDataKeyPairWithoutPlaintext | GenerateDataKeyWithoutPlaintext | GetPublicKey | ReEncryptFrom | ReEncryptTo | RetireGrant | Sign | Verify`
Required: Yes

 ** constraints **   <a name="accessanalyzer-Type-KmsGrantConfiguration-constraints"></a>
Use this structure to propose allowing [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) in the grant only when the operation request includes the specified [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context).
Type: [KmsGrantConstraints](API_KmsGrantConstraints.md) object
Required: No

 ** retiringPrincipal **   <a name="accessanalyzer-Type-KmsGrantConfiguration-retiringPrincipal"></a>
The principal that is given permission to retire the grant by using [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) operation.
Type: String
Required: No

## See Also
<a name="API_KmsGrantConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/KmsGrantConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/KmsGrantConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/KmsGrantConfiguration)

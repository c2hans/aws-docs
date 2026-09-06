---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ServerCertificateMetadata.html
---

# ServerCertificateMetadata
<a name="API_ServerCertificateMetadata"></a>

Contains information about a server certificate without its certificate body, certificate chain, and private key.

 This data type is used as a response element in the [UploadServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadServerCertificate.html) and [ListServerCertificates](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServerCertificates.html) operations.

## Contents
<a name="API_ServerCertificateMetadata_Contents"></a>

 ** Arn **
 The Amazon Resource Name (ARN) specifying the server certificate. For more information about ARNs and how to use them in policies, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** Path **
 The path to the server certificate. For more information about paths, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
Required: Yes

 ** ServerCertificateId **
 The stable and unique string identifying the server certificate. For more information about IDs, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** ServerCertificateName **
The name that identifies the server certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** Expiration **
The date on which the certificate is set to expire.
Type: Timestamp
Required: No

 ** UploadDate **
The date when the server certificate was uploaded.
Type: Timestamp
Required: No

## See Also
<a name="API_ServerCertificateMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ServerCertificateMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ServerCertificateMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ServerCertificateMetadata)

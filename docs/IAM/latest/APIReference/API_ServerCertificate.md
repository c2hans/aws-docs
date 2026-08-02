---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ServerCertificate.html
---

# ServerCertificate
<a name="API_ServerCertificate"></a>

Contains information about a server certificate.

 This data type is used as a response element in the [GetServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServerCertificate.html) operation.

## Contents
<a name="API_ServerCertificate_Contents"></a>

 ** CertificateBody **
The contents of the public key certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 ** ServerCertificateMetadata **
The meta information of the server certificate, such as its name, path, ID, and ARN.
Type: [ServerCertificateMetadata](API_ServerCertificateMetadata.md) object
Required: Yes

 ** CertificateChain **
The contents of the public key certificate chain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2097152.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** Tags.member.N **
A list of tags that are attached to the server certificate. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

## See Also
<a name="API_ServerCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ServerCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ServerCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ServerCertificate)

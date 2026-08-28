---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SigningCertificate.html
---

# SigningCertificate
<a name="API_SigningCertificate"></a>

Contains information about an X.509 signing certificate.

This data type is used as a response element in the [UploadSigningCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadSigningCertificate.html) and [ListSigningCertificates](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSigningCertificates.html) operations.

## Contents
<a name="API_SigningCertificate_Contents"></a>

 ** CertificateBody **
The contents of the signing certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 ** CertificateId **
The ID for the signing certificate.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** Status **
The status of the signing certificate. `Active` means that the key is valid for API calls, while `Inactive` means it is not.
Type: String
Valid Values: `Active | Inactive | Expired`
Required: Yes

 ** UserName **
The name of the user the signing certificate is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** UploadDate **
The date when the signing certificate was uploaded.
Type: Timestamp
Required: No

## See Also
<a name="API_SigningCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SigningCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SigningCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SigningCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

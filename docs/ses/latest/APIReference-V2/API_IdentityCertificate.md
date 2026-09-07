---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_IdentityCertificate.html
---

# IdentityCertificate
<a name="API_IdentityCertificate"></a>

An object that contains information about an S/MIME certificate that's associated with an email identity.

## Contents
<a name="API_IdentityCertificate_Contents"></a>

 ** CertificateArn **   <a name="SES-Type-IdentityCertificate-CertificateArn"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager (ACM) certificate that's associated with the email identity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:[\w+=/,.@-]*:[0-9]+:certificate/[\w+=,.@-]+`
Required: No

 ** CertificateExpiryTime **   <a name="SES-Type-IdentityCertificate-CertificateExpiryTime"></a>
The timestamp after which the certificate is no longer valid.
Type: Timestamp
Required: No

 ** FromAddress **   <a name="SES-Type-IdentityCertificate-FromAddress"></a>
The email address that the certificate applies to.
Type: String
Required: No

 ** Status **   <a name="SES-Type-IdentityCertificate-Status"></a>
The status of the certificate association. A status of `ACTIVE` indicates that the certificate is ready to use for signing.
Type: String
Valid Values: `PROVISIONING | INACTIVE | DEPROVISIONING | ACTIVE | FAILED`
Required: No

## See Also
<a name="API_IdentityCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/IdentityCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/IdentityCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/IdentityCertificate)

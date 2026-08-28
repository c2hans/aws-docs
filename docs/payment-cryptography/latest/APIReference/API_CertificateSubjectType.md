---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CertificateSubjectType.html
---

# CertificateSubjectType
<a name="API_CertificateSubjectType"></a>

The metadata used to create the certificate signing request.

## Contents
<a name="API_CertificateSubjectType_Contents"></a>

 ** CommonName **   <a name="paymentcryptography-Type-CertificateSubjectType-CommonName"></a>
The name you provide to create the certificate signing request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\[;\]<>\u0080-\uFFFF]+`
Required: Yes

 ** City **   <a name="paymentcryptography-Type-CertificateSubjectType-City"></a>
The city you provide to create the certificate signing request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[^\[;\]<>\u0080-\uFFFF]+`
Required: No

 ** Country **   <a name="paymentcryptography-Type-CertificateSubjectType-Country"></a>
The country you provide to create the certificate signing request.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Za-z]+`
Required: No

 ** EmailAddress **   <a name="paymentcryptography-Type-CertificateSubjectType-EmailAddress"></a>
The email address you provide to create the certificate signing request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*`
Required: No

 ** Organization **   <a name="paymentcryptography-Type-CertificateSubjectType-Organization"></a>
The organization you provide to create the certificate signing request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\[;\]<>\u0080-\uFFFF]+`
Required: No

 ** OrganizationUnit **   <a name="paymentcryptography-Type-CertificateSubjectType-OrganizationUnit"></a>
The organization unit you provide to create the certificate signing request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\[;\]<>\u0080-\uFFFF]+`
Required: No

 ** StateOrProvince **   <a name="paymentcryptography-Type-CertificateSubjectType-StateOrProvince"></a>
The state or province you provide to create the certificate signing request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[^\[;\]<>\u0080-\uFFFF]+`
Required: No

## See Also
<a name="API_CertificateSubjectType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/CertificateSubjectType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/CertificateSubjectType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/CertificateSubjectType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

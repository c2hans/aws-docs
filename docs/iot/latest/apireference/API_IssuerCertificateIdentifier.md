---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_IssuerCertificateIdentifier.html
---

# IssuerCertificateIdentifier
<a name="API_IssuerCertificateIdentifier"></a>

The certificate issuer indentifier.

## Contents
<a name="API_IssuerCertificateIdentifier_Contents"></a>

 ** issuerCertificateSerialNumber **   <a name="iot-Type-IssuerCertificateIdentifier-issuerCertificateSerialNumber"></a>
The issuer certificate serial number.
Type: String
Length Constraints: Maximum length of 20.
Pattern: `[a-fA-F0-9:]+`
Required: No

 ** issuerCertificateSubject **   <a name="iot-Type-IssuerCertificateIdentifier-issuerCertificateSubject"></a>
The subject of the issuer certificate.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\p{Graph}\x20]*`
Required: No

 ** issuerId **   <a name="iot-Type-IssuerCertificateIdentifier-issuerId"></a>
The issuer ID.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: No

## See Also
<a name="API_IssuerCertificateIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/IssuerCertificateIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/IssuerCertificateIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/IssuerCertificateIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

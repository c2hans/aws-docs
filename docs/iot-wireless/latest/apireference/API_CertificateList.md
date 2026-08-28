---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CertificateList.html
---

# CertificateList
<a name="API_CertificateList"></a>

List of sidewalk certificates.

## Contents
<a name="API_CertificateList_Contents"></a>

 ** SigningAlg **   <a name="iotwireless-Type-CertificateList-SigningAlg"></a>
The certificate chain algorithm provided by sidewalk.
Type: String
Valid Values: `Ed25519 | P256r1`
Required: Yes

 ** Value **   <a name="iotwireless-Type-CertificateList-Value"></a>
The value of the chosen sidewalk certificate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_CertificateList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/CertificateList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/CertificateList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/CertificateList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

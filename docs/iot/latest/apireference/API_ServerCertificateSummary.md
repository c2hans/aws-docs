---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ServerCertificateSummary.html
---

# ServerCertificateSummary
<a name="API_ServerCertificateSummary"></a>

An object that contains information about a server certificate.

## Contents
<a name="API_ServerCertificateSummary_Contents"></a>

 ** serverCertificateArn **   <a name="iot-Type-ServerCertificateSummary-serverCertificateArn"></a>
The ARN of the server certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\d{1}:\d{12}:certificate/[a-zA-Z0-9/-]+`
Required: No

 ** serverCertificateStatus **   <a name="iot-Type-ServerCertificateSummary-serverCertificateStatus"></a>
The status of the server certificate.
Type: String
Valid Values: `INVALID | VALID`
Required: No

 ** serverCertificateStatusDetail **   <a name="iot-Type-ServerCertificateSummary-serverCertificateStatusDetail"></a>
Details that explain the status of the server certificate.
Type: String
Required: No

## See Also
<a name="API_ServerCertificateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ServerCertificateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ServerCertificateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ServerCertificateSummary)

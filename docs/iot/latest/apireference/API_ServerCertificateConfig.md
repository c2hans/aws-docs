---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ServerCertificateConfig.html
---

# ServerCertificateConfig
<a name="API_ServerCertificateConfig"></a>

The server certificate configuration.

## Contents
<a name="API_ServerCertificateConfig_Contents"></a>

 ** enableOCSPCheck **   <a name="iot-Type-ServerCertificateConfig-enableOCSPCheck"></a>
A Boolean value that indicates whether Online Certificate Status Protocol (OCSP) server certificate check is enabled or not.
For more information, see [ Server certificate configuration for OCSP stapling](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-cert-config.html) from AWS IoT Core Developer Guide.
Type: Boolean
Required: No

 ** ocspAuthorizedResponderArn **   <a name="iot-Type-ServerCertificateConfig-ocspAuthorizedResponderArn"></a>
The Amazon Resource Name (ARN) for an X.509 certificate stored in AWS Certificate Manager (ACM). If provided, AWS IoT Core will use this certificate to validate the signature of the received OCSP response. The OCSP responder must sign responses using either this authorized responder certificate or the issuing certificate, depending on whether the ARN is provided or not. The certificate must be in the same AWS account and region as the domain configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\d{1}:\d{12}:certificate/[a-zA-Z0-9/-]+`
Required: No

 ** ocspLambdaArn **   <a name="iot-Type-ServerCertificateConfig-ocspLambdaArn"></a>
The Amazon Resource Name (ARN) for a Lambda function that acts as a Request for Comments (RFC) 6960-compliant Online Certificate Status Protocol (OCSP) responder, supporting basic OCSP responses. The Lambda function accepts a base64-encoding of the OCSP request in the Distinguished Encoding Rules (DER) format. The Lambda function's response is also a base64-encoded OCSP response in the DER format. The response size must not exceed 4 kilobytes (KiB). The Lambda function must be in the same AWS account and region as the domain configuration. For more information, see [Configuring server certificate OCSP for private endpoints in AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-cert-config.html#iot-custom-endpoints-cert-config-ocsp-private-endpoint.html) from the AWS IoT Core developer guide.
Type: String
Length Constraints: Maximum length of 140.
Required: No

## See Also
<a name="API_ServerCertificateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ServerCertificateConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ServerCertificateConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ServerCertificateConfig)

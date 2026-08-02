---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCACertificate.html
---

# DescribeCACertificate
<a name="API_DescribeCACertificate"></a>

Describes a registered CA certificate.

Requires permission to access the [DescribeCACertificate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeCACertificate_RequestSyntax"></a>

```
GET /cacertificate/{{caCertificateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeCACertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caCertificateId](#API_DescribeCACertificate_RequestSyntax) **   <a name="iot-DescribeCACertificate-request-uri-certificateId"></a>
The CA certificate identifier.
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: Yes

## Request Body
<a name="API_DescribeCACertificate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeCACertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateDescription": {
      "autoRegistrationStatus": "string",
      "certificateArn": "string",
      "certificateId": "string",
      "certificateMode": "string",
      "certificatePem": "string",
      "creationDate": number,
      "customerVersion": number,
      "generationId": "string",
      "lastModifiedDate": number,
      "ownedBy": "string",
      "status": "string",
      "validity": {
         "notAfter": number,
         "notBefore": number
      }
   },
   "registrationConfig": {
      "roleArn": "string",
      "templateBody": "string",
      "templateName": "string"
   }
}
```

## Response Elements
<a name="API_DescribeCACertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateDescription](#API_DescribeCACertificate_ResponseSyntax) **   <a name="iot-DescribeCACertificate-response-certificateDescription"></a>
The CA certificate description.
Type: [CACertificateDescription](API_CACertificateDescription.md) object

 ** [registrationConfig](#API_DescribeCACertificate_ResponseSyntax) **   <a name="iot-DescribeCACertificate-response-registrationConfig"></a>
Information about the registration configuration.
Type: [RegistrationConfig](API_RegistrationConfig.md) object

## Errors
<a name="API_DescribeCACertificate_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DescribeCACertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeCACertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeCACertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeCACertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeCACertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeCACertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeCACertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeCACertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeCACertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeCACertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeCACertificate)

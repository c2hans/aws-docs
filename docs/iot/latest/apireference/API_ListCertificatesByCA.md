---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListCertificatesByCA.html
---

# ListCertificatesByCA
<a name="API_ListCertificatesByCA"></a>

List the device certificates signed by the specified CA certificate.

Requires permission to access the [ListCertificatesByCA](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListCertificatesByCA_RequestSyntax"></a>

```
GET /certificates-by-ca/{{caCertificateId}}?isAscendingOrder={{ascendingOrder}}&marker={{marker}}&pageSize={{pageSize}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCertificatesByCA_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ascendingOrder](#API_ListCertificatesByCA_RequestSyntax) **   <a name="iot-ListCertificatesByCA-request-uri-ascendingOrder"></a>
Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

 ** [caCertificateId](#API_ListCertificatesByCA_RequestSyntax) **   <a name="iot-ListCertificatesByCA-request-uri-caCertificateId"></a>
The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: Yes

 ** [marker](#API_ListCertificatesByCA_RequestSyntax) **   <a name="iot-ListCertificatesByCA-request-uri-marker"></a>
The marker for the next set of results.
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [pageSize](#API_ListCertificatesByCA_RequestSyntax) **   <a name="iot-ListCertificatesByCA-request-uri-pageSize"></a>
The result page size.
Valid Range: Minimum value of 1. Maximum value of 250.

## Request Body
<a name="API_ListCertificatesByCA_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCertificatesByCA_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificates": [
      {
         "certificateArn": "string",
         "certificateId": "string",
         "certificateMode": "string",
         "creationDate": number,
         "status": "string"
      }
   ],
   "nextMarker": "string"
}
```

## Response Elements
<a name="API_ListCertificatesByCA_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificates](#API_ListCertificatesByCA_ResponseSyntax) **   <a name="iot-ListCertificatesByCA-response-certificates"></a>
The device certificates signed by the specified CA certificate.
Type: Array of [Certificate](API_Certificate.md) objects

 ** [nextMarker](#API_ListCertificatesByCA_ResponseSyntax) **   <a name="iot-ListCertificatesByCA-response-nextMarker"></a>
The marker for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

## Errors
<a name="API_ListCertificatesByCA_Errors"></a>

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
<a name="API_ListCertificatesByCA_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListCertificatesByCA)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListCertificatesByCA)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListCertificatesByCA)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListCertificatesByCA)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListCertificatesByCA)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListCertificatesByCA)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListCertificatesByCA)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListCertificatesByCA)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListCertificatesByCA)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListCertificatesByCA)

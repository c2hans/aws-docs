---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetServiceEndpoint.html
---

# GetServiceEndpoint
<a name="API_GetServiceEndpoint"></a>

Gets the account-specific endpoint for Configuration and Update Server (CUPS) protocol or LoRaWAN Network Server (LNS) connections.

## Request Syntax
<a name="API_GetServiceEndpoint_RequestSyntax"></a>

```
GET /service-endpoint?serviceType={{ServiceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetServiceEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ServiceType](#API_GetServiceEndpoint_RequestSyntax) **   <a name="iotwireless-GetServiceEndpoint-request-uri-ServiceType"></a>
The service type for which to get endpoint information about. Can be `CUPS` for the Configuration and Update Server endpoint, or `LNS` for the LoRaWAN Network Server endpoint.
Valid Values: `CUPS | LNS`

## Request Body
<a name="API_GetServiceEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetServiceEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ServerTrust": "string",
   "ServiceEndpoint": "string",
   "ServiceType": "string"
}
```

## Response Elements
<a name="API_GetServiceEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServerTrust](#API_GetServiceEndpoint_ResponseSyntax) **   <a name="iotwireless-GetServiceEndpoint-response-ServerTrust"></a>
The Root CA of the server trust certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[^-A-Za-z0-9+/=]|=[^=]|={3,}${1,4096}`

 ** [ServiceEndpoint](#API_GetServiceEndpoint_ResponseSyntax) **   <a name="iotwireless-GetServiceEndpoint-response-ServiceEndpoint"></a>
The service endpoint value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ServiceType](#API_GetServiceEndpoint_ResponseSyntax) **   <a name="iotwireless-GetServiceEndpoint-response-ServiceType"></a>
The endpoint's service type.
Type: String
Valid Values: `CUPS | LNS`

## Errors
<a name="API_GetServiceEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_GetServiceEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetServiceEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetServiceEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetServiceEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetServiceEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetServiceEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetServiceEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetServiceEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetServiceEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetServiceEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetServiceEndpoint)

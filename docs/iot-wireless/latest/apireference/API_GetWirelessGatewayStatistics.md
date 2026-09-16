---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessGatewayStatistics.html
---

# GetWirelessGatewayStatistics
<a name="API_GetWirelessGatewayStatistics"></a>

Gets operating information about a wireless gateway.

## Request Syntax
<a name="API_GetWirelessGatewayStatistics_RequestSyntax"></a>

```
GET /wireless-gateways/{{Id}}/statistics HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWirelessGatewayStatistics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetWirelessGatewayStatistics_RequestSyntax) **   <a name="iotwireless-GetWirelessGatewayStatistics-request-uri-WirelessGatewayId"></a>
The ID of the wireless gateway for which to get the data.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetWirelessGatewayStatistics_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWirelessGatewayStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectionStatus": "string",
   "LastUplinkReceivedAt": "string",
   "WirelessGatewayId": "string"
}
```

## Response Elements
<a name="API_GetWirelessGatewayStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionStatus](#API_GetWirelessGatewayStatistics_ResponseSyntax) **   <a name="iotwireless-GetWirelessGatewayStatistics-response-ConnectionStatus"></a>
The connection status of the wireless gateway.
Type: String
Valid Values: `Connected | Disconnected`

 ** [LastUplinkReceivedAt](#API_GetWirelessGatewayStatistics_ResponseSyntax) **   <a name="iotwireless-GetWirelessGatewayStatistics-response-LastUplinkReceivedAt"></a>
The date and time when the most recent uplink was received.
This value is only valid for 3 months.
Type: String
Pattern: `^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`

 ** [WirelessGatewayId](#API_GetWirelessGatewayStatistics_ResponseSyntax) **   <a name="iotwireless-GetWirelessGatewayStatistics-response-WirelessGatewayId"></a>
The ID of the wireless gateway.
Type: String
Length Constraints: Maximum length of 256.

## Errors
<a name="API_GetWirelessGatewayStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_GetWirelessGatewayStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetWirelessGatewayStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetWirelessGatewayStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetWirelessGatewayStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetWirelessGatewayStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetWirelessGatewayStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetWirelessGatewayStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetWirelessGatewayStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetWirelessGatewayStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetWirelessGatewayStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetWirelessGatewayStatistics)

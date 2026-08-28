---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessGateway.html
---

# GetWirelessGateway
<a name="API_GetWirelessGateway"></a>

Gets information about a wireless gateway.

## Request Syntax
<a name="API_GetWirelessGateway_RequestSyntax"></a>

```
GET /wireless-gateways/{{Identifier}}?identifierType={{IdentifierType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWirelessGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetWirelessGateway_RequestSyntax) **   <a name="iotwireless-GetWirelessGateway-request-uri-Identifier"></a>
The identifier of the wireless gateway to get.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [IdentifierType](#API_GetWirelessGateway_RequestSyntax) **   <a name="iotwireless-GetWirelessGateway-request-uri-IdentifierType"></a>
The type of identifier used in `identifier`.
Valid Values: `GatewayEui | WirelessGatewayId | ThingName`
Required: Yes

## Request Body
<a name="API_GetWirelessGateway_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWirelessGateway_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Description": "string",
   "Id": "string",
   "LoRaWAN": {
      "Beaconing": {
         "DataRate": number,
         "Frequencies": [ number ]
      },
      "GatewayEui": "string",
      "JoinEuiFilters": [
         [ "string" ]
      ],
      "MaxEirp": number,
      "NetIdFilters": [ "string" ],
      "RfRegion": "string",
      "SubBands": [ number ]
   },
   "Name": "string",
   "ThingArn": "string",
   "ThingName": "string"
}
```

## Response Elements
<a name="API_GetWirelessGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetWirelessGateway_ResponseSyntax) **   <a name="iotwireless-GetWirelessGateway-response-Arn"></a>
The Amazon Resource Name of the resource.
Type: String

 ** [Description](#API_GetWirelessGateway_ResponseSyntax) **   <a name="iotwireless-GetWirelessGateway-response-Description"></a>
The description of the resource.
Type: String
Length Constraints: Maximum length of 2048.

 ** [Id](#API_GetWirelessGateway_ResponseSyntax) **   <a name="iotwireless-GetWirelessGateway-response-Id"></a>
The ID of the wireless gateway.
Type: String
Length Constraints: Maximum length of 256.

 ** [LoRaWAN](#API_GetWirelessGateway_ResponseSyntax) **   <a name="iotwireless-GetWirelessGateway-response-LoRaWAN"></a>
Information about the wireless gateway.
Type: [LoRaWANGateway](API_LoRaWANGateway.md) object

 ** [Name](#API_GetWirelessGateway_ResponseSyntax) **   <a name="iotwireless-GetWirelessGateway-response-Name"></a>
The name of the resource.
Type: String
Length Constraints: Maximum length of 256.

 ** [ThingArn](#API_GetWirelessGateway_ResponseSyntax) **   <a name="iotwireless-GetWirelessGateway-response-ThingArn"></a>
The ARN of the thing associated with the wireless gateway.
Type: String

 ** [ThingName](#API_GetWirelessGateway_ResponseSyntax) **   <a name="iotwireless-GetWirelessGateway-response-ThingName"></a>
The name of the thing associated with the wireless gateway. The value is empty if a thing isn't associated with the gateway.
Type: String

## Errors
<a name="API_GetWirelessGateway_Errors"></a>

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
<a name="API_GetWirelessGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetWirelessGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetWirelessGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetWirelessGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetWirelessGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetWirelessGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetWirelessGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetWirelessGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetWirelessGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetWirelessGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetWirelessGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

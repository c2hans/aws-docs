---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGateway.html
---

# CreateWirelessGateway
<a name="API_CreateWirelessGateway"></a>

Provisions a wireless gateway.

**Note**
When provisioning a wireless gateway, you might run into duplication errors for the following reasons.
If you specify a `GatewayEui` value that already exists.
If you used a `ClientRequestToken` with the same parameters within the last 10 minutes.
To avoid this error, make sure that you use unique identifiers and parameters for each request within the specified time period.

## Request Syntax
<a name="API_CreateWirelessGateway_RequestSyntax"></a>

```
POST /wireless-gateways HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "LoRaWAN": {
      "Beaconing": {
         "DataRate": {{number}},
         "Frequencies": [ {{number}} ]
      },
      "GatewayEui": "{{string}}",
      "JoinEuiFilters": [
         [ "{{string}}" ]
      ],
      "MaxEirp": {{number}},
      "NetIdFilters": [ "{{string}}" ],
      "RfRegion": "{{string}}",
      "SubBands": [ {{number}} ]
   },
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateWirelessGateway_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWirelessGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateWirelessGateway_RequestSyntax) **   <a name="iotwireless-CreateWirelessGateway-request-ClientRequestToken"></a>
Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [Description](#API_CreateWirelessGateway_RequestSyntax) **   <a name="iotwireless-CreateWirelessGateway-request-Description"></a>
The description of the new resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [LoRaWAN](#API_CreateWirelessGateway_RequestSyntax) **   <a name="iotwireless-CreateWirelessGateway-request-LoRaWAN"></a>
The gateway configuration information to use to create the wireless gateway.
Type: [LoRaWANGateway](API_LoRaWANGateway.md) object
Required: Yes

 ** [Name](#API_CreateWirelessGateway_RequestSyntax) **   <a name="iotwireless-CreateWirelessGateway-request-Name"></a>
The name of the new resource.
The following special characters aren't accepted: `<>^#~$`
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Tags](#API_CreateWirelessGateway_RequestSyntax) **   <a name="iotwireless-CreateWirelessGateway-request-Tags"></a>
The tags to attach to the new wireless gateway. Tags are metadata that you can use to manage a resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateWirelessGateway_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateWirelessGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateWirelessGateway_ResponseSyntax) **   <a name="iotwireless-CreateWirelessGateway-response-Arn"></a>
The Amazon Resource Name of the new resource.
Type: String

 ** [Id](#API_CreateWirelessGateway_ResponseSyntax) **   <a name="iotwireless-CreateWirelessGateway-response-Id"></a>
The ID of the new wireless gateway.
Type: String
Length Constraints: Maximum length of 256.

## Errors
<a name="API_CreateWirelessGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Adding, updating, or deleting the resource can cause an inconsistent state.
 ** ResourceId **
Id of the resource in the conflicting operation.
 ** ResourceType **
Type of the resource in the conflicting operation.
HTTP Status Code: 409

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
<a name="API_CreateWirelessGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/CreateWirelessGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/CreateWirelessGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/CreateWirelessGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/CreateWirelessGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/CreateWirelessGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/CreateWirelessGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/CreateWirelessGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/CreateWirelessGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/CreateWirelessGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/CreateWirelessGateway)

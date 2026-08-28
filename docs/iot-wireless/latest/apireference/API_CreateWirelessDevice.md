---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessDevice.html
---

# CreateWirelessDevice
<a name="API_CreateWirelessDevice"></a>

Provisions a wireless device.

## Request Syntax
<a name="API_CreateWirelessDevice_RequestSyntax"></a>

```
POST /wireless-devices HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "DestinationName": "{{string}}",
   "LoRaWAN": {
      "AbpV1\_0\_x": {
         "DevAddr": "{{string}}",
         "FCntStart": {{number}},
         "SessionKeys": {
            "AppSKey": "{{string}}",
            "NwkSKey": "{{string}}"
         }
      },
      "AbpV1\_1": {
         "DevAddr": "{{string}}",
         "FCntStart": {{number}},
         "SessionKeys": {
            "AppSKey": "{{string}}",
            "FNwkSIntKey": "{{string}}",
            "NwkSEncKey": "{{string}}",
            "SNwkSIntKey": "{{string}}"
         }
      },
      "DevEui": "{{string}}",
      "DeviceProfileId": "{{string}}",
      "FPorts": {
         "Applications": [
            {
               "DestinationName": "{{string}}",
               "FPort": {{number}},
               "Type": "{{string}}"
            }
         ],
         "ClockSync": {{number}},
         "Fuota": {{number}},
         "Multicast": {{number}},
         "Positioning": {
            "ClockSync": {{number}},
            "Gnss": {{number}},
            "Stream": {{number}}
         }
      },
      "OtaaV1\_0\_x": {
         "AppEui": "{{string}}",
         "AppKey": "{{string}}",
         "GenAppKey": "{{string}}",
         "JoinEui": "{{string}}"
      },
      "OtaaV1\_1": {
         "AppKey": "{{string}}",
         "JoinEui": "{{string}}",
         "NwkKey": "{{string}}"
      },
      "ServiceProfileId": "{{string}}"
   },
   "Name": "{{string}}",
   "Positioning": "{{string}}",
   "Sidewalk": {
      "DeviceProfileId": "{{string}}",
      "Positioning": {
         "DestinationName": "{{string}}"
      },
      "SidewalkManufacturingSn": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWirelessDevice_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWirelessDevice_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateWirelessDevice_RequestSyntax) **   <a name="iotwireless-CreateWirelessDevice-request-ClientRequestToken"></a>
Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [Description](#API_CreateWirelessDevice_RequestSyntax) **   <a name="iotwireless-CreateWirelessDevice-request-Description"></a>
The description of the new resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [DestinationName](#API_CreateWirelessDevice_RequestSyntax) **   <a name="iotwireless-CreateWirelessDevice-request-DestinationName"></a>
The name of the destination to assign to the new wireless device.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** [LoRaWAN](#API_CreateWirelessDevice_RequestSyntax) **   <a name="iotwireless-CreateWirelessDevice-request-LoRaWAN"></a>
The device configuration information to use to create the wireless device.
Type: [LoRaWANDevice](API_LoRaWANDevice.md) object
Required: No

 ** [Name](#API_CreateWirelessDevice_RequestSyntax) **   <a name="iotwireless-CreateWirelessDevice-request-Name"></a>
The name of the new resource.
The following special characters aren't accepted: `<>^#~$`
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Positioning](#API_CreateWirelessDevice_RequestSyntax) **   <a name="iotwireless-CreateWirelessDevice-request-Positioning"></a>
The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [Sidewalk](#API_CreateWirelessDevice_RequestSyntax) **   <a name="iotwireless-CreateWirelessDevice-request-Sidewalk"></a>
The device configuration information to use to create the Sidewalk device.
Type: [SidewalkCreateWirelessDevice](API_SidewalkCreateWirelessDevice.md) object
Required: No

 ** [Tags](#API_CreateWirelessDevice_RequestSyntax) **   <a name="iotwireless-CreateWirelessDevice-request-Tags"></a>
The tags to attach to the new wireless device. Tags are metadata that you can use to manage a resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Type](#API_CreateWirelessDevice_RequestSyntax) **   <a name="iotwireless-CreateWirelessDevice-request-Type"></a>
The wireless device type.
Type: String
Valid Values: `Sidewalk | LoRaWAN`
Required: Yes

## Response Syntax
<a name="API_CreateWirelessDevice_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateWirelessDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateWirelessDevice_ResponseSyntax) **   <a name="iotwireless-CreateWirelessDevice-response-Arn"></a>
The Amazon Resource Name of the new resource.
Type: String

 ** [Id](#API_CreateWirelessDevice_ResponseSyntax) **   <a name="iotwireless-CreateWirelessDevice-response-Id"></a>
The ID of the new wireless device.
Type: String
Length Constraints: Maximum length of 256.

## Errors
<a name="API_CreateWirelessDevice_Errors"></a>

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
<a name="API_CreateWirelessDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/CreateWirelessDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/CreateWirelessDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/CreateWirelessDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/CreateWirelessDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/CreateWirelessDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/CreateWirelessDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/CreateWirelessDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/CreateWirelessDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/CreateWirelessDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/CreateWirelessDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetDeviceDiscovery.html
---

# GetDeviceDiscovery
<a name="API_GetDeviceDiscovery"></a>

 Get the current state of a device discovery.

## Request Syntax
<a name="API_GetDeviceDiscovery_RequestSyntax"></a>

```
GET /device-discoveries/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDeviceDiscovery_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-request-uri-Identifier"></a>
The id of the device discovery job request.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetDeviceDiscovery_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDeviceDiscovery_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountAssociationId": "string",
   "Arn": "string",
   "ConnectorAssociationId": "string",
   "ControllerId": "string",
   "DiscoveryType": "string",
   "FinishedAt": number,
   "Id": "string",
   "StartedAt": number,
   "Status": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetDeviceDiscovery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountAssociationId](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-AccountAssociationId"></a>
The identifier of the account association used for the device discovery.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`

 ** [Arn](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-Arn"></a>
The Amazon Resource Name (ARN) of the device discovery job request.
Type: String
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:device-discovery/[0-9a-zA-Z]+`

 ** [ConnectorAssociationId](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-ConnectorAssociationId"></a>
 *This parameter has been deprecated.*
The ID tracking the current discovery process for one connector association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`

 ** [ControllerId](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-ControllerId"></a>
The id of the end-user's IoT hub.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`

 ** [DiscoveryType](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-DiscoveryType"></a>
The discovery type supporting the type of device to be discovered in the device discovery job request.
Type: String
Valid Values: `ZWAVE | ZIGBEE | CLOUD | CUSTOM | CONTROLLER_CAPABILITY_REDISCOVERY`

 ** [FinishedAt](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-FinishedAt"></a>
The timestamp value for the completion time of the device discovery.
Type: Timestamp

 ** [Id](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-Id"></a>
The id of the device discovery job request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`

 ** [StartedAt](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-StartedAt"></a>
The timestamp value for the start time of the device discovery.
Type: Timestamp

 ** [Status](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-Status"></a>
The status of the device discovery job request.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT`

 ** [Tags](#API_GetDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-GetDeviceDiscovery-response-Tags"></a>
 *This parameter has been deprecated.*
A set of key/value pairs that are used to manage the device discovery request.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetDeviceDiscovery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
HTTP Status Code: 401

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_GetDeviceDiscovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetDeviceDiscovery)

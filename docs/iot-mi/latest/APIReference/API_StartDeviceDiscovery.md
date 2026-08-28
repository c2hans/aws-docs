---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_StartDeviceDiscovery.html
---

# StartDeviceDiscovery
<a name="API_StartDeviceDiscovery"></a>

 This API is used to start device discovery for hub-connected and third-party-connected devices. The authentication material (install code) is delivered as a message to the controller instructing it to start the discovery.

## Request Syntax
<a name="API_StartDeviceDiscovery_RequestSyntax"></a>

```
POST /device-discoveries HTTP/1.1
Content-type: application/json

{
   "AccountAssociationId": "{{string}}",
   "AuthenticationMaterial": "{{string}}",
   "AuthenticationMaterialType": "{{string}}",
   "ClientToken": "{{string}}",
   "ConnectorAssociationIdentifier": "{{string}}",
   "ConnectorDeviceIdList": [ "{{string}}" ],
   "ControllerIdentifier": "{{string}}",
   "CustomProtocolDetail": {
      "{{string}}" : "{{string}}"
   },
   "DiscoveryType": "{{string}}",
   "EndDeviceIdentifier": "{{string}}",
   "Protocol": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartDeviceDiscovery_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartDeviceDiscovery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountAssociationId](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-AccountAssociationId"></a>
The identifier of the cloud-to-cloud account association to use for discovery of third-party devices.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: No

 ** [AuthenticationMaterial](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-AuthenticationMaterial"></a>
The authentication material required to start the local device discovery job request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9A-Za-z_\-\+=\/:; ]+`
Required: No

 ** [AuthenticationMaterialType](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-AuthenticationMaterialType"></a>
The type of authentication material used for device discovery jobs.
Type: String
Valid Values: `ZWAVE_INSTALL_CODE`
Required: No

 ** [ClientToken](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [ConnectorAssociationIdentifier](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-ConnectorAssociationIdentifier"></a>
 *This parameter has been deprecated.*
The id of the connector association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: No

 ** [ConnectorDeviceIdList](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-ConnectorDeviceIdList"></a>
Used as a filter for PLA discoveries.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.,@-]+`
Required: No

 ** [ControllerIdentifier](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-ControllerIdentifier"></a>
The id of the end-user's IoT hub.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: No

 ** [CustomProtocolDetail](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-CustomProtocolDetail"></a>
Additional protocol-specific details required for device discovery, which vary based on the discovery type.
For a `DiscoveryType` of `CUSTOM`, the string-to-string map must have a key value of `Name` set to a non-empty-string.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z0-9 _.-]+`
Value Length Constraints: Minimum length of 1. Maximum length of 512.
Value Pattern: `[a-zA-Z0-9 _.{}:"-]+`
Required: No

 ** [DiscoveryType](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-DiscoveryType"></a>
The discovery type supporting the type of device to be discovered in the device discovery task request.
Type: String
Valid Values: `ZWAVE | ZIGBEE | CLOUD | CUSTOM | CONTROLLER_CAPABILITY_REDISCOVERY`
Required: Yes

 ** [EndDeviceIdentifier](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-EndDeviceIdentifier"></a>
The unique id of the end device for capability rediscovery.
This parameter is only available when the discovery type is CONTROLLER\_CAPABILITY\_REDISCOVERY.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: No

 ** [Protocol](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-Protocol"></a>
The protocol type for capability rediscovery (ZWAVE, ZIGBEE, or CUSTOM).
This parameter is only available when the discovery type is CONTROLLER\_CAPABILITY\_REDISCOVERY.
Type: String
Valid Values: `ZWAVE | ZIGBEE | CUSTOM`
Required: No

 ** [Tags](#API_StartDeviceDiscovery_RequestSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-request-Tags"></a>
 *This parameter has been deprecated.*
A set of key/value pairs that are used to manage the device discovery request.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartDeviceDiscovery_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Id": "string",
   "StartedAt": number
}
```

## Response Elements
<a name="API_StartDeviceDiscovery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_StartDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-response-Id"></a>
The id of the device discovery job request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`

 ** [StartedAt](#API_StartDeviceDiscovery_ResponseSyntax) **   <a name="managedintegrations-StartDeviceDiscovery-response-StartedAt"></a>
The timestamp value for the start time of the device discovery.
Type: Timestamp

## Errors
<a name="API_StartDeviceDiscovery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict with the request.
HTTP Status Code: 409

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
<a name="API_StartDeviceDiscovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/StartDeviceDiscovery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

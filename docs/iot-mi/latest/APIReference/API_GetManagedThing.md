---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetManagedThing.html
---

# GetManagedThing
<a name="API_GetManagedThing"></a>

 Get details of a managed thing including its attributes and capabilities.

## Request Syntax
<a name="API_GetManagedThing_RequestSyntax"></a>

```
GET /managed-things/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetManagedThing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetManagedThing_RequestSyntax) **   <a name="managedintegrations-GetManagedThing-request-uri-Identifier"></a>
The id of the managed thing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Request Body
<a name="API_GetManagedThing_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetManagedThing_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ActivatedAt": number,
   "AdvertisedProductId": "string",
   "Arn": "string",
   "Brand": "string",
   "Classification": "string",
   "ConnectorDestinationId": "string",
   "ConnectorDeviceId": "string",
   "ConnectorPolicyId": "string",
   "CreatedAt": number,
   "CredentialLockerId": "string",
   "DeviceSpecificKey": "string",
   "HubNetworkMode": "string",
   "Id": "string",
   "InternationalArticleNumber": "string",
   "MacAddress": "string",
   "MetaData": {
      "string" : "string"
   },
   "Model": "string",
   "Name": "string",
   "Owner": "string",
   "ParentControllerId": "string",
   "ProvisioningStatus": "string",
   "Role": "string",
   "SerialNumber": "string",
   "Tags": {
      "string" : "string"
   },
   "UniversalProductCode": "string",
   "UpdatedAt": number,
   "WiFiSimpleSetupConfiguration": {
      "EnableAsProvisionee": boolean,
      "EnableAsProvisioner": boolean,
      "TimeoutInMinutes": number
   }
}
```

## Response Elements
<a name="API_GetManagedThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActivatedAt](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-ActivatedAt"></a>
The timestampe value of when the device was activated.
Type: Timestamp

 ** [AdvertisedProductId](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-AdvertisedProductId"></a>
The id of the advertised product.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `([A-Za-z0-9!#$%&()*\+\-;<=>?@^_`{|}~])+`

 ** [Arn](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-Arn"></a>
The Amazon Resource Name (ARN) of the managed thing.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:managed-thing/([0-9a-zA-Z:_-])+`

 ** [Brand](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-Brand"></a>
The brand of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [Classification](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-Classification"></a>
The classification of the managed thing such as light bulb or thermostat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [ConnectorDestinationId](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-ConnectorDestinationId"></a>
The identifier of the connector destination associated with this managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [ConnectorDeviceId](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-ConnectorDeviceId"></a>
The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).
This parameter is used for cloud-to-cloud devices only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.,@-]+`

 ** [ConnectorPolicyId](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-ConnectorPolicyId"></a>
 *This parameter has been deprecated.*
The id of the connector policy.
This parameter is used for cloud-to-cloud devices only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [CreatedAt](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-CreatedAt"></a>
The timestamp value of when the device creation request occurred.
Type: Timestamp

 ** [CredentialLockerId](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-CredentialLockerId"></a>
The identifier of the credential locker for the managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`

 ** [DeviceSpecificKey](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-DeviceSpecificKey"></a>
A Zwave device-specific key used during device activation.
This parameter is used for Zwave devices only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9=_.,@\+\-]+`

 ** [HubNetworkMode](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-HubNetworkMode"></a>
The network mode for the hub-connected device.
Type: String
Valid Values: `STANDARD | NETWORK_WIDE_EXCLUSION`

 ** [Id](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-Id"></a>
The id of the managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`

 ** [InternationalArticleNumber](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-InternationalArticleNumber"></a>
The unique 13 digit number that identifies the managed thing.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 13.
Pattern: `[0-9]+`

 ** [MacAddress](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-MacAddress"></a>
The media access control (MAC) address for the device represented by the managed thing.
This parameter is used for Zigbee devices only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [MetaData](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-MetaData"></a>
The metadata for the managed thing.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*[a-zA-Z0-9_.,@/:#-]+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 800.
Value Pattern: `.*[a-zA-Z0-9_.,@/:#-]*.*`

 ** [Model](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-Model"></a>
The model of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [Name](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-Name"></a>
The name of the managed thing representing the physical device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`

 ** [Owner](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-Owner"></a>
Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.,@-]+`

 ** [ParentControllerId](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-ParentControllerId"></a>
Id of the controller device used for the discovery job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9]+`

 ** [ProvisioningStatus](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-ProvisioningStatus"></a>
The provisioning status of the device in the provisioning workflow for onboarding to IoT managed integrations. For more information, see [Device Provisioning](https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html).
Type: String
Valid Values: `UNASSOCIATED | PRE_ASSOCIATED | DISCOVERED | ACTIVATED | DELETION_FAILED | DELETE_IN_PROGRESS | ISOLATED | DELETED`

 ** [Role](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-Role"></a>
The type of device used. This will be the AWS hub controller, cloud device, or AWS IoT device.
Type: String
Valid Values: `CONTROLLER | DEVICE`

 ** [SerialNumber](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-SerialNumber"></a>
The serial number of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [Tags](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-Tags"></a>
A set of key/value pairs that are used to manage the managed thing.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [UniversalProductCode](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-UniversalProductCode"></a>
The universal product code (UPC) of the device model. The UPC is typically used in the United States of America and Canada.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`

 ** [UpdatedAt](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-UpdatedAt"></a>
The timestamp value of when the managed thing was last updated at.
Type: Timestamp

 ** [WiFiSimpleSetupConfiguration](#API_GetManagedThing_ResponseSyntax) **   <a name="managedintegrations-GetManagedThing-response-WiFiSimpleSetupConfiguration"></a>
The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.
Type: [WiFiSimpleSetupConfiguration](API_WiFiSimpleSetupConfiguration.md) object

## Errors
<a name="API_GetManagedThing_Errors"></a>

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
<a name="API_GetManagedThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetManagedThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetManagedThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetManagedThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetManagedThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetManagedThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetManagedThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetManagedThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetManagedThing)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetManagedThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetManagedThing)

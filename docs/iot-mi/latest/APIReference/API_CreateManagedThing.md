---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateManagedThing.html
---

# CreateManagedThing
<a name="API_CreateManagedThing"></a>

Creates a managed thing. A managed thing contains the device identifier, protocol supported, and capabilities of the device in a data model format defined by Managed integrations.

## Request Syntax
<a name="API_CreateManagedThing_RequestSyntax"></a>

```
POST /managed-things HTTP/1.1
Content-type: application/json

{
   "AuthenticationMaterial": "{{string}}",
   "AuthenticationMaterialType": "{{string}}",
   "Brand": "{{string}}",
   "Capabilities": "{{string}}",
   "CapabilityReport": {
      "endpoints": [
         {
            "capabilities": [
               {
                  "actions": [ "{{string}}" ],
                  "events": [ "{{string}}" ],
                  "id": "{{string}}",
                  "name": "{{string}}",
                  "properties": [ "{{string}}" ],
                  "version": "{{string}}"
               }
            ],
            "deviceTypes": [ "{{string}}" ],
            "id": "{{string}}"
         }
      ],
      "nodeId": "{{string}}",
      "version": "{{string}}"
   },
   "CapabilitySchemas": [
      {
         "CapabilityId": "{{string}}",
         "ExtrinsicId": "{{string}}",
         "ExtrinsicVersion": {{number}},
         "Format": "{{string}}",
         "Schema": {{JSON value}}
      }
   ],
   "Classification": "{{string}}",
   "ClientToken": "{{string}}",
   "CredentialLockerId": "{{string}}",
   "MetaData": {
      "{{string}}" : "{{string}}"
   },
   "Model": "{{string}}",
   "Name": "{{string}}",
   "Owner": "{{string}}",
   "Role": "{{string}}",
   "SerialNumber": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "WiFiSimpleSetupConfiguration": {
      "EnableAsProvisionee": {{boolean}},
      "EnableAsProvisioner": {{boolean}},
      "TimeoutInMinutes": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateManagedThing_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateManagedThing_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AuthenticationMaterial](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-AuthenticationMaterial"></a>
The authentication material defining the device connectivity setup requests. The authorization materials used are the device bar code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[0-9A-Za-z!#$%&()*\+\-;<=>?@^_`{|}~\/: {},\\"]+`
Required: Yes

 ** [AuthenticationMaterialType](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-AuthenticationMaterialType"></a>
The type of authentication material used for device connectivity setup requests.
Type: String
Valid Values: `CUSTOM_PROTOCOL_QR_BAR_CODE | WIFI_SETUP_QR_BAR_CODE | ZWAVE_QR_BAR_CODE | ZIGBEE_QR_BAR_CODE | DISCOVERED_DEVICE | PRE_ONBOARDED_CLOUD`
Required: Yes

 ** [Brand](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-Brand"></a>
The brand of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [Capabilities](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-Capabilities"></a>
 *This parameter has been deprecated.*
The capabilities of the device such as light bulb.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9\s'\x{0022},.:\\\/{$}\[\]=_\-\+]+`
Required: No

 ** [CapabilityReport](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-CapabilityReport"></a>
A report of the capabilities for the managed thing.
Type: [CapabilityReport](API_CapabilityReport.md) object
Required: No

 ** [CapabilitySchemas](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-CapabilitySchemas"></a>
The capability schemas that define the functionality and features supported by the managed thing, including device capabilities and their associated properties.
Type: Array of [CapabilitySchemaItem](API_CapabilitySchemaItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

 ** [Classification](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-Classification"></a>
The classification of the managed thing such as light bulb or thermostat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [ClientToken](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [CredentialLockerId](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-CredentialLockerId"></a>
The identifier of the credential for the managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** [MetaData](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-MetaData"></a>
The metadata for the managed thing.
The `managedThing` `metadata` parameter is used for associating attributes with a `managedThing` that can be used for grouping over-the-air (OTA) tasks. Name value pairs in `metadata` can be used in the `OtaTargetQueryString` parameter for the `CreateOtaTask` API operation.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*[a-zA-Z0-9_.,@/:#-]+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 800.
Value Pattern: `.*[a-zA-Z0-9_.,@/:#-]*.*`
Required: No

 ** [Model](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-Model"></a>
The model of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [Name](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-Name"></a>
The name of the managed thing representing the physical device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`
Required: No

 ** [Owner](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-Owner"></a>
Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.,@-]+`
Required: No

 ** [Role](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-Role"></a>
The type of device used. This will be the hub controller, cloud device, or AWS IoT device.
Type: String
Valid Values: `CONTROLLER | DEVICE`
Required: Yes

 ** [SerialNumber](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-SerialNumber"></a>
The serial number of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [Tags](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-Tags"></a>
A set of key/value pairs that are used to manage the managed thing.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [WiFiSimpleSetupConfiguration](#API_CreateManagedThing_RequestSyntax) **   <a name="managedintegrations-CreateManagedThing-request-WiFiSimpleSetupConfiguration"></a>
The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.
Type: [WiFiSimpleSetupConfiguration](API_WiFiSimpleSetupConfiguration.md) object
Required: No

## Response Syntax
<a name="API_CreateManagedThing_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "CreatedAt": number,
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateManagedThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateManagedThing_ResponseSyntax) **   <a name="managedintegrations-CreateManagedThing-response-Arn"></a>
The Amazon Resource Name (ARN) of the managed thing.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:managed-thing/([0-9a-zA-Z:_-])+`

 ** [CreatedAt](#API_CreateManagedThing_ResponseSyntax) **   <a name="managedintegrations-CreateManagedThing-response-CreatedAt"></a>
The timestamp value of when the device creation request occurred.
Type: Timestamp

 ** [Id](#API_CreateManagedThing_ResponseSyntax) **   <a name="managedintegrations-CreateManagedThing-response-Id"></a>
The id of the managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`

## Errors
<a name="API_CreateManagedThing_Errors"></a>

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
<a name="API_CreateManagedThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateManagedThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateManagedThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateManagedThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateManagedThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateManagedThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateManagedThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateManagedThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateManagedThing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateManagedThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateManagedThing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_UpdateManagedThing.html
---

# UpdateManagedThing
<a name="API_UpdateManagedThing"></a>

Update the attributes and capabilities associated with a managed thing.

## Request Syntax
<a name="API_UpdateManagedThing_RequestSyntax"></a>

```
PUT /managed-things/{{Identifier}} HTTP/1.1
Content-type: application/json

{
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
   "CredentialLockerId": "{{string}}",
   "HubNetworkMode": "{{string}}",
   "MetaData": {
      "{{string}}" : "{{string}}"
   },
   "Model": "{{string}}",
   "Name": "{{string}}",
   "Owner": "{{string}}",
   "SerialNumber": "{{string}}",
   "WiFiSimpleSetupConfiguration": {
      "EnableAsProvisionee": {{boolean}},
      "EnableAsProvisioner": {{boolean}},
      "TimeoutInMinutes": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateManagedThing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-uri-Identifier"></a>
The id of the managed thing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Request Body
<a name="API_UpdateManagedThing_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Brand](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-Brand"></a>
The brand of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [Capabilities](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-Capabilities"></a>
 *This parameter has been deprecated.*
The capabilities of the device such as light bulb.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9\s'\x{0022},.:\\\/{$}\[\]=_\-\+]+`
Required: No

 ** [CapabilityReport](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-CapabilityReport"></a>
A report of the capabilities for the managed thing.
Type: [CapabilityReport](API_CapabilityReport.md) object
Required: No

 ** [CapabilitySchemas](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-CapabilitySchemas"></a>
The updated capability schemas that define the functionality and features supported by the managed thing.
Type: Array of [CapabilitySchemaItem](API_CapabilitySchemaItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

 ** [Classification](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-Classification"></a>
The classification of the managed thing such as light bulb or thermostat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [CredentialLockerId](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-CredentialLockerId"></a>
The identifier of the credential for the managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** [HubNetworkMode](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-HubNetworkMode"></a>
The network mode for the hub-connected device.
Type: String
Valid Values: `STANDARD | NETWORK_WIDE_EXCLUSION`
Required: No

 ** [MetaData](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-MetaData"></a>
The metadata for the managed thing.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*[a-zA-Z0-9_.,@/:#-]+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 800.
Value Pattern: `.*[a-zA-Z0-9_.,@/:#-]*.*`
Required: No

 ** [Model](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-Model"></a>
The model of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [Name](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-Name"></a>
The name of the managed thing representing the physical device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`
Required: No

 ** [Owner](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-Owner"></a>
Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.,@-]+`
Required: No

 ** [SerialNumber](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-SerialNumber"></a>
The serial number of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [WiFiSimpleSetupConfiguration](#API_UpdateManagedThing_RequestSyntax) **   <a name="managedintegrations-UpdateManagedThing-request-WiFiSimpleSetupConfiguration"></a>
The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.
Type: [WiFiSimpleSetupConfiguration](API_WiFiSimpleSetupConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateManagedThing_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateManagedThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateManagedThing_Errors"></a>

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
<a name="API_UpdateManagedThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/UpdateManagedThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/UpdateManagedThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/UpdateManagedThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/UpdateManagedThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/UpdateManagedThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/UpdateManagedThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/UpdateManagedThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/UpdateManagedThing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/UpdateManagedThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/UpdateManagedThing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

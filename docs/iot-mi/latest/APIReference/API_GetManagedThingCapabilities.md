---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetManagedThingCapabilities.html
---

# GetManagedThingCapabilities
<a name="API_GetManagedThingCapabilities"></a>

Get the capabilities for a managed thing using the device ID.

## Request Syntax
<a name="API_GetManagedThingCapabilities_RequestSyntax"></a>

```
GET /managed-things-capabilities/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetManagedThingCapabilities_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetManagedThingCapabilities_RequestSyntax) **   <a name="managedintegrations-GetManagedThingCapabilities-request-uri-Identifier"></a>
The id of the device.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Request Body
<a name="API_GetManagedThingCapabilities_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetManagedThingCapabilities_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Capabilities": "string",
   "CapabilityReport": {
      "endpoints": [
         {
            "capabilities": [
               {
                  "actions": [ "string" ],
                  "events": [ "string" ],
                  "id": "string",
                  "name": "string",
                  "properties": [ "string" ],
                  "version": "string"
               }
            ],
            "deviceTypes": [ "string" ],
            "id": "string"
         }
      ],
      "nodeId": "string",
      "version": "string"
   },
   "ManagedThingId": "string"
}
```

## Response Elements
<a name="API_GetManagedThingCapabilities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Capabilities](#API_GetManagedThingCapabilities_ResponseSyntax) **   <a name="managedintegrations-GetManagedThingCapabilities-response-Capabilities"></a>
 *This parameter has been deprecated.*
The capabilities of the device such as light bulb.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9\s'\x{0022},.:\\\/{$}\[\]=_\-\+]+`

 ** [CapabilityReport](#API_GetManagedThingCapabilities_ResponseSyntax) **   <a name="managedintegrations-GetManagedThingCapabilities-response-CapabilityReport"></a>
A report of the capabilities for the managed thing.
Type: [CapabilityReport](API_CapabilityReport.md) object

 ** [ManagedThingId](#API_GetManagedThingCapabilities_ResponseSyntax) **   <a name="managedintegrations-GetManagedThingCapabilities-response-ManagedThingId"></a>
The id of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`

## Errors
<a name="API_GetManagedThingCapabilities_Errors"></a>

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
<a name="API_GetManagedThingCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetManagedThingCapabilities)

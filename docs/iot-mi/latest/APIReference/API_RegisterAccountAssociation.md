---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RegisterAccountAssociation.html
---

# RegisterAccountAssociation
<a name="API_RegisterAccountAssociation"></a>

Registers an account association with a managed thing, establishing a connection between a device and a third-party account.

## Request Syntax
<a name="API_RegisterAccountAssociation_RequestSyntax"></a>

```
PUT /managed-thing-associations/register HTTP/1.1
Content-type: application/json

{
   "AccountAssociationId": "{{string}}",
   "DeviceDiscoveryId": "{{string}}",
   "ManagedThingId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterAccountAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterAccountAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountAssociationId](#API_RegisterAccountAssociation_RequestSyntax) **   <a name="managedintegrations-RegisterAccountAssociation-request-AccountAssociationId"></a>
The identifier of the account association to register with the managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

 ** [DeviceDiscoveryId](#API_RegisterAccountAssociation_RequestSyntax) **   <a name="managedintegrations-RegisterAccountAssociation-request-DeviceDiscoveryId"></a>
The identifier of the device discovery job associated with this registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** [ManagedThingId](#API_RegisterAccountAssociation_RequestSyntax) **   <a name="managedintegrations-RegisterAccountAssociation-request-ManagedThingId"></a>
The identifier of the managed thing to register with the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Response Syntax
<a name="API_RegisterAccountAssociation_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "AccountAssociationId": "string",
   "DeviceDiscoveryId": "string",
   "ManagedThingId": "string"
}
```

## Response Elements
<a name="API_RegisterAccountAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [AccountAssociationId](#API_RegisterAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-RegisterAccountAssociation-response-AccountAssociationId"></a>
The identifier of the account association that was registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`

 ** [DeviceDiscoveryId](#API_RegisterAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-RegisterAccountAssociation-response-DeviceDiscoveryId"></a>
The identifier of the device discovery job associated with this registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`

 ** [ManagedThingId](#API_RegisterAccountAssociation_ResponseSyntax) **   <a name="managedintegrations-RegisterAccountAssociation-response-ManagedThingId"></a>
The identifier of the managed thing that was registered with the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`

## Errors
<a name="API_RegisterAccountAssociation_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_RegisterAccountAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/RegisterAccountAssociation)

---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_DeleteManagedThing.html
---

# DeleteManagedThing
<a name="API_DeleteManagedThing"></a>

Delete a managed thing. For direct-connected and hub-connected devices connecting with Managed integrations via a controller, all of the devices connected to it will have their status changed to `PENDING`. It is not possible to remove a cloud-to-cloud device.

## Request Syntax
<a name="API_DeleteManagedThing_RequestSyntax"></a>

```
DELETE /managed-things/{{Identifier}}?Force={{Force}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteManagedThing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Force](#API_DeleteManagedThing_RequestSyntax) **   <a name="managedintegrations-DeleteManagedThing-request-uri-Force"></a>
When set to `TRUE`, a forceful deteletion of the managed thing will occur. When set to `FALSE`, a non-forceful deletion of the managed thing will occur.

 ** [Identifier](#API_DeleteManagedThing_RequestSyntax) **   <a name="managedintegrations-DeleteManagedThing-request-uri-Identifier"></a>
The id of the managed thing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Request Body
<a name="API_DeleteManagedThing_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteManagedThing_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteManagedThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteManagedThing_Errors"></a>

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
<a name="API_DeleteManagedThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/DeleteManagedThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/DeleteManagedThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/DeleteManagedThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/DeleteManagedThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/DeleteManagedThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/DeleteManagedThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/DeleteManagedThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/DeleteManagedThing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/DeleteManagedThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/DeleteManagedThing)

---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetManagedThingMetaData.html
---

# GetManagedThingMetaData
<a name="API_GetManagedThingMetaData"></a>

Get the metadata information for a managed thing.

**Note**
The `managedThing` `metadata` parameter is used for associating attributes with a `managedThing` that can be used for grouping over-the-air (OTA) tasks. Name value pairs in `metadata` can be used in the `OtaTargetQueryString` parameter for the `CreateOtaTask` API operation.

## Request Syntax
<a name="API_GetManagedThingMetaData_RequestSyntax"></a>

```
GET /managed-things-metadata/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetManagedThingMetaData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetManagedThingMetaData_RequestSyntax) **   <a name="managedintegrations-GetManagedThingMetaData-request-uri-Identifier"></a>
The managed thing id.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Request Body
<a name="API_GetManagedThingMetaData_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetManagedThingMetaData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ManagedThingId": "string",
   "MetaData": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetManagedThingMetaData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagedThingId](#API_GetManagedThingMetaData_ResponseSyntax) **   <a name="managedintegrations-GetManagedThingMetaData-response-ManagedThingId"></a>
The managed thing id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`

 ** [MetaData](#API_GetManagedThingMetaData_ResponseSyntax) **   <a name="managedintegrations-GetManagedThingMetaData-response-MetaData"></a>
The metadata for the managed thing.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*[a-zA-Z0-9_.,@/:#-]+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 800.
Value Pattern: `.*[a-zA-Z0-9_.,@/:#-]*.*`

## Errors
<a name="API_GetManagedThingMetaData_Errors"></a>

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
<a name="API_GetManagedThingMetaData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetManagedThingMetaData)

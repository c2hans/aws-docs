---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetSchemaVersion.html
---

# GetSchemaVersion
<a name="API_GetSchemaVersion"></a>

Gets a schema version with the provided information.

## Request Syntax
<a name="API_GetSchemaVersion_RequestSyntax"></a>

```
GET /schema-versions/{{Type}}/{{SchemaVersionedId}}?Format={{Format}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSchemaVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Format](#API_GetSchemaVersion_RequestSyntax) **   <a name="managedintegrations-GetSchemaVersion-request-uri-Format"></a>
The format of the schema version.
Valid Values: `AWS | ZCL | CONNECTOR`

 ** [SchemaVersionedId](#API_GetSchemaVersion_RequestSyntax) **   <a name="managedintegrations-GetSchemaVersion-request-uri-SchemaVersionedId"></a>
Schema id with a version specified. If the version is missing, it defaults to latest version.
Length Constraints: Minimum length of 7. Maximum length of 128.
Pattern: `[a-zA-Z0-9.]+@(\d+\.\d+(\.\d+)?|\$latest)`
Required: Yes

 ** [Type](#API_GetSchemaVersion_RequestSyntax) **   <a name="managedintegrations-GetSchemaVersion-request-uri-Type"></a>
The type of schema version.
Valid Values: `capability | definition`
Required: Yes

## Request Body
<a name="API_GetSchemaVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSchemaVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Description": "string",
   "Namespace": "string",
   "Schema": JSON value,
   "SchemaId": "string",
   "SemanticVersion": "string",
   "Type": "string",
   "Visibility": "string"
}
```

## Response Elements
<a name="API_GetSchemaVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_GetSchemaVersion_ResponseSyntax) **   <a name="managedintegrations-GetSchemaVersion-response-Description"></a>
The description of the schema version.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 2048.
Pattern: `[a-zA-Z0-9.,/ -]+`

 ** [Namespace](#API_GetSchemaVersion_ResponseSyntax) **   <a name="managedintegrations-GetSchemaVersion-response-Namespace"></a>
The name of the schema version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 12.
Pattern: `[a-z0-9]+`

 ** [Schema](#API_GetSchemaVersion_ResponseSyntax) **   <a name="managedintegrations-GetSchemaVersion-response-Schema"></a>
The schema of the schema version.
Type: JSON value

 ** [SchemaId](#API_GetSchemaVersion_ResponseSyntax) **   <a name="managedintegrations-GetSchemaVersion-response-SchemaId"></a>
The id of the schema version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9.]+`

 ** [SemanticVersion](#API_GetSchemaVersion_ResponseSyntax) **   <a name="managedintegrations-GetSchemaVersion-response-SemanticVersion"></a>
The schema version. If this is left blank, it defaults to the latest version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 12.
Pattern: `(\d+\.\d+(\.\d+)?|\$latest)`

 ** [Type](#API_GetSchemaVersion_ResponseSyntax) **   <a name="managedintegrations-GetSchemaVersion-response-Type"></a>
The type of schema version.
Type: String
Valid Values: `capability | definition`

 ** [Visibility](#API_GetSchemaVersion_ResponseSyntax) **   <a name="managedintegrations-GetSchemaVersion-response-Visibility"></a>
The visibility of the schema version.
Type: String
Valid Values: `PUBLIC | PRIVATE`

## Errors
<a name="API_GetSchemaVersion_Errors"></a>

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

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_GetSchemaVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetSchemaVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetSchemaVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetSchemaVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetSchemaVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetSchemaVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetSchemaVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetSchemaVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetSchemaVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetSchemaVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetSchemaVersion)

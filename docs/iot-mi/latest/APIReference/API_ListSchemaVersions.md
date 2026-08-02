---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListSchemaVersions.html
---

# ListSchemaVersions
<a name="API_ListSchemaVersions"></a>

Lists schema versions with the provided information.

## Request Syntax
<a name="API_ListSchemaVersions_RequestSyntax"></a>

```
GET /schema-versions/{{Type}}?MaxResults={{MaxResults}}&NamespaceFilter={{Namespace}}&NextToken={{NextToken}}&SchemaIdFilter={{SchemaId}}&SemanticVersionFilter={{SemanticVersion}}&VisibilityFilter={{Visibility}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSchemaVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListSchemaVersions_RequestSyntax) **   <a name="managedintegrations-ListSchemaVersions-request-uri-MaxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [Namespace](#API_ListSchemaVersions_RequestSyntax) **   <a name="managedintegrations-ListSchemaVersions-request-uri-Namespace"></a>
Filter on the name of the schema version.
Length Constraints: Minimum length of 3. Maximum length of 12.
Pattern: `[a-z0-9]+`

 ** [NextToken](#API_ListSchemaVersions_RequestSyntax) **   <a name="managedintegrations-ListSchemaVersions-request-uri-NextToken"></a>
A token that can be used to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

 ** [SchemaId](#API_ListSchemaVersions_RequestSyntax) **   <a name="managedintegrations-ListSchemaVersions-request-uri-SchemaId"></a>
Filter on the id of the schema version.
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9.]+`

 ** [SemanticVersion](#API_ListSchemaVersions_RequestSyntax) **   <a name="managedintegrations-ListSchemaVersions-request-uri-SemanticVersion"></a>
The schema version. If this is left blank, it defaults to the latest version.
Length Constraints: Minimum length of 3. Maximum length of 12.
Pattern: `(\d+\.\d+(\.\d+)?|\$latest)`

 ** [Type](#API_ListSchemaVersions_RequestSyntax) **   <a name="managedintegrations-ListSchemaVersions-request-uri-Type"></a>
Filter on the type of schema version.
Valid Values: `capability | definition`
Required: Yes

 ** [Visibility](#API_ListSchemaVersions_RequestSyntax) **   <a name="managedintegrations-ListSchemaVersions-request-uri-Visibility"></a>
The visibility of the schema version.
Valid Values: `PUBLIC | PRIVATE`

## Request Body
<a name="API_ListSchemaVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSchemaVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Description": "string",
         "Namespace": "string",
         "SchemaId": "string",
         "SemanticVersion": "string",
         "Type": "string",
         "Visibility": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListSchemaVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListSchemaVersions_ResponseSyntax) **   <a name="managedintegrations-ListSchemaVersions-response-Items"></a>
The list of schema versions.
Type: Array of [SchemaVersionListItem](API_SchemaVersionListItem.md) objects

 ** [NextToken](#API_ListSchemaVersions_ResponseSyntax) **   <a name="managedintegrations-ListSchemaVersions-response-NextToken"></a>
A token that can be used to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Errors
<a name="API_ListSchemaVersions_Errors"></a>

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
<a name="API_ListSchemaVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/ListSchemaVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/ListSchemaVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ListSchemaVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/ListSchemaVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ListSchemaVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/ListSchemaVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/ListSchemaVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/ListSchemaVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/ListSchemaVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ListSchemaVersions)

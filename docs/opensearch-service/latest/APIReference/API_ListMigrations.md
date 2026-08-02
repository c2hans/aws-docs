---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListMigrations.html
---

# ListMigrations
<a name="API_ListMigrations"></a>

Lists migration jobs for an Amazon OpenSearch Service application. You can filter results by migration status. Use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListMigrations_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/app-migrations?applicationId={{applicationId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMigrations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListMigrations_RequestSyntax) **   <a name="opensearchservice-ListMigrations-request-uri-applicationId"></a>
The unique identifier of the OpenSearch application to list migrations for.
Pattern: `[a-z0-9]{3,30}`
Required: Yes

 ** [maxResults](#API_ListMigrations_RequestSyntax) **   <a name="opensearchservice-ListMigrations-request-uri-maxResults"></a>
The maximum number of results to return in a single call.

 ** [nextToken](#API_ListMigrations_RequestSyntax) **   <a name="opensearchservice-ListMigrations-request-uri-nextToken"></a>
The pagination token from a previous call to retrieve the next set of results.

 ** [status](#API_ListMigrations_RequestSyntax) **   <a name="opensearchservice-ListMigrations-request-uri-status"></a>
Filters the results by migration status. Valid values are `PENDING`, `IN_PROGRESS`, `SUCCEEDED`, and `FAILED`.

## Request Body
<a name="API_ListMigrations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMigrations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "migrations": [
      {
         "applicationId": "string",
         "createdAt": number,
         "error": {
            "code": "string",
            "message": "string"
         },
         "exportedCount": number,
         "importedCount": number,
         "migrationId": "string",
         "source": {
            "datasourceArn": "string"
         },
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMigrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [migrations](#API_ListMigrations_ResponseSyntax) **   <a name="opensearchservice-ListMigrations-response-migrations"></a>
A list of migration job summaries for the specified application.
Type: Array of [MigrationSummary](API_MigrationSummary.md) objects

 ** [nextToken](#API_ListMigrations_ResponseSyntax) **   <a name="opensearchservice-ListMigrations-response-nextToken"></a>
The pagination token to use in a subsequent call to retrieve the next set of results.
Type: String

## Errors
<a name="API_ListMigrations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_ListMigrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListMigrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListMigrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListMigrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListMigrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListMigrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListMigrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListMigrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListMigrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListMigrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListMigrations)

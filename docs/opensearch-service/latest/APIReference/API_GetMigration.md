---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetMigration.html
---

# GetMigration
<a name="API_GetMigration"></a>

Retrieves the current status and progress of a migration job, including the number of exported and imported objects and error details if the migration failed.

## Request Syntax
<a name="API_GetMigration_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/app-migrations/{{migrationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMigration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [migrationId](#API_GetMigration_RequestSyntax) **   <a name="opensearchservice-GetMigration-request-uri-migrationId"></a>
The unique identifier of the migration job to retrieve.
Required: Yes

## Request Body
<a name="API_GetMigration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMigration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetMigration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_GetMigration_ResponseSyntax) **   <a name="opensearchservice-GetMigration-response-applicationId"></a>
The unique identifier of the OpenSearch application associated with the migration.
Type: String
Pattern: `[a-z0-9]{3,30}`

 ** [createdAt](#API_GetMigration_ResponseSyntax) **   <a name="opensearchservice-GetMigration-response-createdAt"></a>
The date and time when the migration job was created.
Type: Timestamp

 ** [error](#API_GetMigration_ResponseSyntax) **   <a name="opensearchservice-GetMigration-response-error"></a>
Error details if the migration failed or completed with errors.
Type: [MigrationError](API_MigrationError.md) object

 ** [exportedCount](#API_GetMigration_ResponseSyntax) **   <a name="opensearchservice-GetMigration-response-exportedCount"></a>
The number of saved objects exported from the source data source.
Type: Integer

 ** [importedCount](#API_GetMigration_ResponseSyntax) **   <a name="opensearchservice-GetMigration-response-importedCount"></a>
The number of saved objects successfully imported into the target workspace.
Type: Integer

 ** [migrationId](#API_GetMigration_ResponseSyntax) **   <a name="opensearchservice-GetMigration-response-migrationId"></a>
The unique identifier of the migration job.
Type: String

 ** [source](#API_GetMigration_ResponseSyntax) **   <a name="opensearchservice-GetMigration-response-source"></a>
The source configuration for the migration, including the data source ARN.
Type: [MigrationSource](API_MigrationSource.md) object

 ** [status](#API_GetMigration_ResponseSyntax) **   <a name="opensearchservice-GetMigration-response-status"></a>
The current status of the migration job. Valid values are `PENDING`, `IN_PROGRESS`, `SUCCEEDED`, and `FAILED`.
Type: String

 ** [updatedAt](#API_GetMigration_ResponseSyntax) **   <a name="opensearchservice-GetMigration-response-updatedAt"></a>
The date and time when the migration job was last updated.
Type: Timestamp

## Errors
<a name="API_GetMigration_Errors"></a>

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

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetMigration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetMigration)

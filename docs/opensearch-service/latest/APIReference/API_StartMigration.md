---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartMigration.html
---

# StartMigration
<a name="API_StartMigration"></a>

Initiates a migration job to migrate saved objects from a data source to an Amazon OpenSearch Service application workspace. Saved objects include dashboards, visualizations, index patterns, and searches. You can specify export filters to control the scope of the migration and a conflict resolution strategy for handling existing objects in the target workspace.

## Request Syntax
<a name="API_StartMigration_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/app-migrations HTTP/1.1
Content-type: application/json

{
   "applicationId": "{{string}}",
   "clientToken": "{{string}}",
   "migrationOptions": {
      "conflictResolution": "{{string}}",
      "exportOptions": {
         "includeReferencesDeep": {{boolean}},
         "objects": [
            {
               "id": "{{string}}",
               "type": "{{string}}"
            }
         ],
         "types": [ "{{string}}" ]
      },
      "source": {
         "datasourceArn": "{{string}}"
      },
      "workspace": {
         "createWorkspace": {{boolean}},
         "name": "{{string}}",
         "type": "{{string}}",
         "workspaceId": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_StartMigration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartMigration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationId](#API_StartMigration_RequestSyntax) **   <a name="opensearchservice-StartMigration-request-applicationId"></a>
The unique identifier of the OpenSearch application to migrate saved objects into.
Type: String
Pattern: `[a-z0-9]{3,30}`
Required: Yes

 ** [clientToken](#API_StartMigration_RequestSyntax) **   <a name="opensearchservice-StartMigration-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon OpenSearch Service ignores the request but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [migrationOptions](#API_StartMigration_RequestSyntax) **   <a name="opensearchservice-StartMigration-request-migrationOptions"></a>
The configuration options for the migration, including the source data source, target workspace, export filters, and conflict resolution strategy.
Type: [MigrationOptions](API_MigrationOptions.md) object
Required: Yes

## Response Syntax
<a name="API_StartMigration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "migrationId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StartMigration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [migrationId](#API_StartMigration_ResponseSyntax) **   <a name="opensearchservice-StartMigration-response-migrationId"></a>
The unique identifier of the migration job.
Type: String

 ** [status](#API_StartMigration_ResponseSyntax) **   <a name="opensearchservice-StartMigration-response-status"></a>
The initial status of the migration job. The status is `PENDING` when a migration is first created.
Type: String

## Errors
<a name="API_StartMigration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

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
<a name="API_StartMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/StartMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/StartMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/StartMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/StartMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/StartMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/StartMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/StartMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/StartMigration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/StartMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/StartMigration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

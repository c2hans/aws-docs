---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListWorkflows.html
---

# ListWorkflows
<a name="API_ListWorkflows"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

List the migration workflows.

## Request Syntax
<a name="API_ListWorkflows_RequestSyntax"></a>

```
GET /migrationworkflows?adsApplicationConfigurationName={{adsApplicationConfigurationName}}&maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&status={{status}}&templateId={{templateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWorkflows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [adsApplicationConfigurationName](#API_ListWorkflows_RequestSyntax) **   <a name="migrationhuborchestrator-ListWorkflows-request-uri-adsApplicationConfigurationName"></a>
The name of the application configured in Application Discovery Service.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`

 ** [maxResults](#API_ListWorkflows_RequestSyntax) **   <a name="migrationhuborchestrator-ListWorkflows-request-uri-maxResults"></a>
The maximum number of results that can be returned.
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [name](#API_ListWorkflows_RequestSyntax) **   <a name="migrationhuborchestrator-ListWorkflows-request-uri-name"></a>
The name of the migration workflow.

 ** [nextToken](#API_ListWorkflows_RequestSyntax) **   <a name="migrationhuborchestrator-ListWorkflows-request-uri-nextToken"></a>
The pagination token.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`

 ** [status](#API_ListWorkflows_RequestSyntax) **   <a name="migrationhuborchestrator-ListWorkflows-request-uri-status"></a>
The status of the migration workflow.
Valid Values: `CREATING | NOT_STARTED | CREATION_FAILED | STARTING | IN_PROGRESS | WORKFLOW_FAILED | PAUSED | PAUSING | PAUSING_FAILED | USER_ATTENTION_REQUIRED | DELETING | DELETION_FAILED | DELETED | COMPLETED`

 ** [templateId](#API_ListWorkflows_RequestSyntax) **   <a name="migrationhuborchestrator-ListWorkflows-request-uri-templateId"></a>
The ID of the template.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`

## Request Body
<a name="API_ListWorkflows_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWorkflows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "migrationWorkflowSummary": [
      {
         "adsApplicationConfigurationName": "string",
         "completedSteps": number,
         "creationTime": number,
         "endTime": number,
         "id": "string",
         "name": "string",
         "status": "string",
         "statusMessage": "string",
         "templateId": "string",
         "totalSteps": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListWorkflows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [migrationWorkflowSummary](#API_ListWorkflows_ResponseSyntax) **   <a name="migrationhuborchestrator-ListWorkflows-response-migrationWorkflowSummary"></a>
The summary of the migration workflow.
Type: Array of [MigrationWorkflowSummary](API_MigrationWorkflowSummary.md) objects

 ** [nextToken](#API_ListWorkflows_ResponseSyntax) **   <a name="migrationhuborchestrator-ListWorkflows-response-nextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`

## Errors
<a name="API_ListWorkflows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource is not available.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListWorkflows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/ListWorkflows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/ListWorkflows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/ListWorkflows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/ListWorkflows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/ListWorkflows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/ListWorkflows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/ListWorkflows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/ListWorkflows)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/ListWorkflows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/ListWorkflows)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

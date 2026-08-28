---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListWorkflowDefinitions.html
---

# ListWorkflowDefinitions
<a name="API_ListWorkflowDefinitions"></a>

Lists all workflow definitions in your account with optional filtering and pagination.

## Request Syntax
<a name="API_ListWorkflowDefinitions_RequestSyntax"></a>

```
POST /workflow-definitions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "sortOrder": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkflowDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListWorkflowDefinitions_RequestSyntax) **   <a name="novaact-ListWorkflowDefinitions-request-uri-maxResults"></a>
The maximum number of workflow definitions to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListWorkflowDefinitions_RequestSyntax) **   <a name="novaact-ListWorkflowDefinitions-request-uri-nextToken"></a>
The token for retrieving the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

## Request Body
<a name="API_ListWorkflowDefinitions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sortOrder](#API_ListWorkflowDefinitions_RequestSyntax) **   <a name="novaact-ListWorkflowDefinitions-request-sortOrder"></a>
The sort order for the returned workflow definitions (ascending or descending).
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListWorkflowDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "workflowDefinitionSummaries": [
      {
         "createdAt": "string",
         "status": "string",
         "workflowDefinitionArn": "string",
         "workflowDefinitionName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkflowDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkflowDefinitions_ResponseSyntax) **   <a name="novaact-ListWorkflowDefinitions-response-nextToken"></a>
The token for retrieving the next page of results, if available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [workflowDefinitionSummaries](#API_ListWorkflowDefinitions_ResponseSyntax) **   <a name="novaact-ListWorkflowDefinitions-response-workflowDefinitionSummaries"></a>
A list of summary information for workflow definitions.
Type: Array of [WorkflowDefinitionSummary](API_WorkflowDefinitionSummary.md) objects

## Errors
<a name="API_ListWorkflowDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient permissions to perform this action.
 ** message **
You don't have sufficient permissions to perform this action. Verify your IAM permissions and try again.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
An internal server error occurred. Please try again later.
 ** message **
The service encountered an internal error. Try again later.
 ** reason **
The reason for the internal server error.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 [ThrottlingException](API_ThrottlingException.md)
The request was throttled due to too many requests. Please try again later.
 ** message **
The request was denied due to request throttling.
 ** quotaCode **
The quota code related to the throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the throttled request.
 ** serviceCode **
The service code where throttling occurred.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input parameters for the request are invalid.
 ** fieldList **
The list of fields that failed validation.
 ** message **
The input fails to satisfy the constraints specified by the service.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListWorkflowDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/nova-act-2025-08-22/ListWorkflowDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/nova-act-2025-08-22/ListWorkflowDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/ListWorkflowDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/nova-act-2025-08-22/ListWorkflowDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/ListWorkflowDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/nova-act-2025-08-22/ListWorkflowDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/nova-act-2025-08-22/ListWorkflowDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/nova-act-2025-08-22/ListWorkflowDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/nova-act-2025-08-22/ListWorkflowDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ListWorkflowDefinitions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

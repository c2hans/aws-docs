---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListWorkflowVersions.html
---

# ListWorkflowVersions
<a name="API_ListWorkflowVersions"></a>

Lists the workflow versions for the specified workflow. For more information, see [Workflow versioning in AWS HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_ListWorkflowVersions_RequestSyntax"></a>

```
GET /workflow/{{workflowId}}/version?maxResults={{maxResults}}&startingToken={{startingToken}}&type={{type}}&workflowOwnerId={{workflowOwnerId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWorkflowVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListWorkflowVersions_RequestSyntax) **   <a name="omics-ListWorkflowVersions-request-uri-maxResults"></a>
The maximum number of workflows to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [startingToken](#API_ListWorkflowVersions_RequestSyntax) **   <a name="omics-ListWorkflowVersions-request-uri-startingToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [type](#API_ListWorkflowVersions_RequestSyntax) **   <a name="omics-ListWorkflowVersions-request-uri-type"></a>
The workflow type.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`

 ** [workflowId](#API_ListWorkflowVersions_RequestSyntax) **   <a name="omics-ListWorkflowVersions-request-uri-workflowId"></a>
The workflow's ID. The `workflowId` is not the UUID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

 ** [workflowOwnerId](#API_ListWorkflowVersions_RequestSyntax) **   <a name="omics-ListWorkflowVersions-request-uri-workflowOwnerId"></a>
The 12-digit account ID of the workflow owner. The workflow owner ID can be retrieved using the `GetShare` API operation. If you are the workflow owner, you do not need to include this ID.
Pattern: `[0-9]{12}`

## Request Body
<a name="API_ListWorkflowVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWorkflowVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "creationTime": "string",
         "description": "string",
         "digest": "string",
         "metadata": {
            "string" : "string"
         },
         "status": "string",
         "type": "string",
         "versionName": "string",
         "workflowId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListWorkflowVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListWorkflowVersions_ResponseSyntax) **   <a name="omics-ListWorkflowVersions-response-items"></a>
A list of workflow version items.
Type: Array of [WorkflowVersionListItem](API_WorkflowVersionListItem.md) objects

 ** [nextToken](#API_ListWorkflowVersions_ResponseSyntax) **   <a name="omics-ListWorkflowVersions-response-nextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_ListWorkflowVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListWorkflowVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListWorkflowVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListWorkflowVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListWorkflowVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListWorkflowVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListWorkflowVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListWorkflowVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListWorkflowVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListWorkflowVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListWorkflowVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListWorkflowVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

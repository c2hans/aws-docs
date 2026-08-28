---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListNotebookRuns.html
---

# ListNotebookRuns
<a name="API_ListNotebookRuns"></a>

Lists [notebook runs](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html) in Amazon SageMaker Unified Studio.

## Request Syntax
<a name="API_ListNotebookRuns_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/notebook-runs?maxResults={{maxResults}}&nextToken={{nextToken}}&notebookIdentifier={{notebookIdentifier}}&owningProjectIdentifier={{owningProjectIdentifier}}&scheduleIdentifier={{scheduleIdentifier}}&sortOrder={{sortOrder}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNotebookRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListNotebookRuns_RequestSyntax) **   <a name="datazone-ListNotebookRuns-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which to list notebook runs.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListNotebookRuns_RequestSyntax) **   <a name="datazone-ListNotebookRuns-request-uri-maxResults"></a>
The maximum number of notebook runs to return in a single call. When the number of notebook runs exceeds the value of `MaxResults`, the response contains a `NextToken` value.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListNotebookRuns_RequestSyntax) **   <a name="datazone-ListNotebookRuns-request-uri-nextToken"></a>
When the number of notebook runs is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of notebook runs, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListNotebookRuns` to list the next set of notebook runs.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [notebookIdentifier](#API_ListNotebookRuns_RequestSyntax) **   <a name="datazone-ListNotebookRuns-request-uri-notebookIdentifier"></a>
The identifier of the notebook to filter runs by.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectIdentifier](#API_ListNotebookRuns_RequestSyntax) **   <a name="datazone-ListNotebookRuns-request-uri-owningProjectIdentifier"></a>
The identifier of the project that owns the notebook runs.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [scheduleIdentifier](#API_ListNotebookRuns_RequestSyntax) **   <a name="datazone-ListNotebookRuns-request-uri-scheduleIdentifier"></a>
The identifier of the schedule to filter notebook runs by.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [sortOrder](#API_ListNotebookRuns_RequestSyntax) **   <a name="datazone-ListNotebookRuns-request-uri-sortOrder"></a>
The sort order for the results.
Valid Values: `ASCENDING | DESCENDING`

 ** [status](#API_ListNotebookRuns_RequestSyntax) **   <a name="datazone-ListNotebookRuns-request-uri-status"></a>
The status to filter notebook runs by.
Valid Values: `QUEUED | STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED`

## Request Body
<a name="API_ListNotebookRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNotebookRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "completedAt": number,
         "createdAt": number,
         "createdBy": "string",
         "domainId": "string",
         "id": "string",
         "notebookId": "string",
         "owningProjectId": "string",
         "scheduleId": "string",
         "startedAt": number,
         "status": "string",
         "triggerSource": {
            "name": "string",
            "type": "string"
         },
         "updatedAt": number,
         "updatedBy": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListNotebookRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListNotebookRuns_ResponseSyntax) **   <a name="datazone-ListNotebookRuns-response-items"></a>
The results of the `ListNotebookRuns` action.
Type: Array of [NotebookRunSummary](API_NotebookRunSummary.md) objects

 ** [nextToken](#API_ListNotebookRuns_ResponseSyntax) **   <a name="datazone-ListNotebookRuns-response-nextToken"></a>
When the number of notebook runs is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of notebook runs, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListNotebookRuns` to list the next set of notebook runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListNotebookRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListNotebookRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListNotebookRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListNotebookRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListNotebookRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListNotebookRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListNotebookRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListNotebookRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListNotebookRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListNotebookRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListNotebookRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListNotebookRuns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

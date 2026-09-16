---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListPipelineExecutions.html
---

# ListPipelineExecutions
<a name="API_ListPipelineExecutions"></a>

Lists pipeline executions for a specific pipeline in a workspace. Supports filtering by state and time range. State can be combined with either startTime or endTime filters. Time range filters are grouped: use startTime filters (startTimeAfter, startTimeBefore) or endTime filters (endTimeAfter, endTimeBefore), but not both. Combining startTime and endTime filters returns an InvalidRequestException. Note: endTime filters only return executions in terminal states, as in-progress executions have no endTime.

## Request Syntax
<a name="API_ListPipelineExecutions_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/pipelines/{{pipelineName}}/executions?endTimeAfter={{endTimeAfter}}&endTimeBefore={{endTimeBefore}}&maxResults={{maxResults}}&nextToken={{nextToken}}&startTimeAfter={{startTimeAfter}}&startTimeBefore={{startTimeBefore}}&state={{state}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPipelineExecutions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTimeAfter](#API_ListPipelineExecutions_RequestSyntax) **   <a name="iotsitewise-ListPipelineExecutions-request-uri-endTimeAfter"></a>
Inclusive lower bound on execution end time (ISO-8601). Only executions with endTime >= endTimeAfter are returned. Cannot be combined with startTimeAfter or startTimeBefore. Only matches executions in terminal states.

 ** [endTimeBefore](#API_ListPipelineExecutions_RequestSyntax) **   <a name="iotsitewise-ListPipelineExecutions-request-uri-endTimeBefore"></a>
Exclusive upper bound on execution end time (ISO-8601). Only executions with endTime < endTimeBefore are returned. Cannot be combined with startTimeAfter or startTimeBefore. Only matches executions in terminal states.

 ** [maxResults](#API_ListPipelineExecutions_RequestSyntax) **   <a name="iotsitewise-ListPipelineExecutions-request-uri-maxResults"></a>
The maximum number of results to return per request. This is an upper bound; the actual number of results may be less. Default: 50.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListPipelineExecutions_RequestSyntax) **   <a name="iotsitewise-ListPipelineExecutions-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [pipelineName](#API_ListPipelineExecutions_RequestSyntax) **   <a name="iotsitewise-ListPipelineExecutions-request-uri-pipelineName"></a>
The name of the pipeline.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [startTimeAfter](#API_ListPipelineExecutions_RequestSyntax) **   <a name="iotsitewise-ListPipelineExecutions-request-uri-startTimeAfter"></a>
Inclusive lower bound on execution start time (ISO-8601). Only executions with startTime >= startTimeAfter are returned. Cannot be combined with endTimeAfter or endTimeBefore.

 ** [startTimeBefore](#API_ListPipelineExecutions_RequestSyntax) **   <a name="iotsitewise-ListPipelineExecutions-request-uri-startTimeBefore"></a>
Exclusive upper bound on execution start time (ISO-8601). Only executions with startTime < startTimeBefore are returned. Cannot be combined with endTimeAfter or endTimeBefore.

 ** [state](#API_ListPipelineExecutions_RequestSyntax) **   <a name="iotsitewise-ListPipelineExecutions-request-uri-state"></a>
Filter by execution state. If not specified, executions in all states are returned.
Valid Values: `NOT_STARTED | RUNNING | SUCCEEDED | FAILED | CANCELLING | CANCELLED`

 ** [workspaceName](#API_ListPipelineExecutions_RequestSyntax) **   <a name="iotsitewise-ListPipelineExecutions-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_ListPipelineExecutions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPipelineExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "pipelineExecutionSummaries": [
      {
         "endTime": number,
         "executionPriority": number,
         "pipelineExecutionId": "string",
         "pipelineVersion": "string",
         "startTime": number,
         "status": {
            "state": "string",
            "stateDetails": {
               "code": "string",
               "details": [
                  {
                     "code": "string",
                     "message": "string"
                  }
               ],
               "message": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelineExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPipelineExecutions_ResponseSyntax) **   <a name="iotsitewise-ListPipelineExecutions-response-nextToken"></a>
The token to be used for the next set of paginated results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [pipelineExecutionSummaries](#API_ListPipelineExecutions_ResponseSyntax) **   <a name="iotsitewise-ListPipelineExecutions-response-pipelineExecutionSummaries"></a>
A list that summarizes each pipeline execution.
Type: Array of [PipelineExecutionSummary](API_PipelineExecutionSummary.md) objects

## Errors
<a name="API_ListPipelineExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_ListPipelineExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListPipelineExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListPipelineExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListPipelineExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListPipelineExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListPipelineExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListPipelineExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListPipelineExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListPipelineExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListPipelineExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListPipelineExecutions)

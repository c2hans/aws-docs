---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListPipelines.html
---

# ListPipelines
<a name="API_ListPipelines"></a>

Lists pipelines in a workspace. To get complete details about a pipeline, use [DescribePipeline](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePipeline.html).

## Request Syntax
<a name="API_ListPipelines_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/pipelines?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPipelines_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPipelines_RequestSyntax) **   <a name="iotsitewise-ListPipelines-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request. Default: 50.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListPipelines_RequestSyntax) **   <a name="iotsitewise-ListPipelines-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [workspaceName](#API_ListPipelines_RequestSyntax) **   <a name="iotsitewise-ListPipelines-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_ListPipelines_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPipelines_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "pipelineSummaries": [
      {
         "createdAt": number,
         "description": "string",
         "pipelineArn": "string",
         "pipelineName": "string",
         "status": {
            "error": {
               "code": "string",
               "message": "string"
            },
            "state": "string"
         },
         "updatedAt": number,
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPipelines_ResponseSyntax) **   <a name="iotsitewise-ListPipelines-response-nextToken"></a>
The token to be used for the next set of paginated results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [pipelineSummaries](#API_ListPipelines_ResponseSyntax) **   <a name="iotsitewise-ListPipelines-response-pipelineSummaries"></a>
A list that summarizes each pipeline in the workspace.
Type: Array of [PipelineSummary](API_PipelineSummary.md) objects

## Errors
<a name="API_ListPipelines_Errors"></a>

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
<a name="API_ListPipelines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListPipelines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListPipelines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListPipelines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListPipelines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListPipelines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListPipelines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListPipelines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListPipelines)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListPipelines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListPipelines)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

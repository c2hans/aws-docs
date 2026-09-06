---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePipelineExecution.html
---

# DescribePipelineExecution
<a name="API_DescribePipelineExecution"></a>

Retrieves detailed information about a specific pipeline execution, including the overall execution status and the status of each individual compute node. Use this operation to monitor execution progress and inspect per-node results, environment variables, and error details.

## Request Syntax
<a name="API_DescribePipelineExecution_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/pipelines/{{pipelineName}}/executions/{{pipelineExecutionId}}?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePipelineExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_DescribePipelineExecution_RequestSyntax) **   <a name="iotsitewise-DescribePipelineExecution-request-uri-maxResults"></a>
The maximum number of compute nodes to return per request. This is an upper bound; the actual number of results may be less. Default: 50.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_DescribePipelineExecution_RequestSyntax) **   <a name="iotsitewise-DescribePipelineExecution-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [pipelineExecutionId](#API_DescribePipelineExecution_RequestSyntax) **   <a name="iotsitewise-DescribePipelineExecution-request-uri-pipelineExecutionId"></a>
The unique identifier of the pipeline execution.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [pipelineName](#API_DescribePipelineExecution_RequestSyntax) **   <a name="iotsitewise-DescribePipelineExecution-request-uri-pipelineName"></a>
The name of the pipeline.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [workspaceName](#API_DescribePipelineExecution_RequestSyntax) **   <a name="iotsitewise-DescribePipelineExecution-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_DescribePipelineExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePipelineExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "computeNodeExecutionDetails": [
      {
         "computeNodeName": "string",
         "dependsOn": [ "string" ],
         "endTime": number,
         "executionEnvironmentVariables": {
            "string" : "string"
         },
         "executionMounts": [
            {
               "name": "string",
               "relativePath": "string",
               "source": { ... },
               "storageType": "string"
            }
         ],
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
         },
         "taskArn": "string",
         "taskName": "string",
         "taskVersion": "string"
      }
   ],
   "endTime": number,
   "executionPriority": number,
   "nextToken": "string",
   "pipelineExecutionId": "string",
   "pipelineName": "string",
   "pipelineVersion": "string",
   "requestEnvironmentVariables": {
      "computeNodes": {
         "string" : {
            "string" : "string"
         }
      },
      "global": {
         "string" : "string"
      }
   },
   "requestMountOverrides": {
      "computeNodes": {
         "string" : [
            {
               "name": "string",
               "relativePath": "string",
               "source": { ... },
               "storageType": "string"
            }
         ]
      }
   },
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
   },
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_DescribePipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [computeNodeExecutionDetails](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-computeNodeExecutionDetails"></a>
A list of compute node execution details within this pipeline execution.
Type: Array of [ComputeNodeExecutionDetails](API_ComputeNodeExecutionDetails.md) objects

 ** [endTime](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-endTime"></a>
The time the pipeline execution completed, in Unix epoch time.
Type: Timestamp

 ** [executionPriority](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-executionPriority"></a>
Scheduling priority for the execution. When not specified, defaults to lowest priority.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.

 ** [nextToken](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-nextToken"></a>
The token to be used for the next set of paginated results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [pipelineExecutionId](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-pipelineExecutionId"></a>
The unique identifier of the pipeline execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [pipelineName](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-pipelineName"></a>
The name of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [pipelineVersion](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-pipelineVersion"></a>
The pipeline version this execution ran against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [requestEnvironmentVariables](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-requestEnvironmentVariables"></a>
The environment variables provided as input for the pipeline execution.
Type: [ExecutionEnvironmentVariables](API_ExecutionEnvironmentVariables.md) object

 ** [requestMountOverrides](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-requestMountOverrides"></a>
The mount overrides provided as input for the pipeline execution. Present when mount overrides were supplied at execution time.
Type: [MountOverrides](API_MountOverrides.md) object

 ** [startTime](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-startTime"></a>
The time the pipeline execution started, in Unix epoch time.
Type: Timestamp

 ** [status](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-status"></a>
The current execution status of the pipeline.
Type: [PipelineExecutionStatus](API_PipelineExecutionStatus.md) object

 ** [workspaceName](#API_DescribePipelineExecution_ResponseSyntax) **   <a name="iotsitewise-DescribePipelineExecution-response-workspaceName"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_DescribePipelineExecution_Errors"></a>

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
<a name="API_DescribePipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribePipelineExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribePipelineExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribePipelineExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribePipelineExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribePipelineExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribePipelineExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribePipelineExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribePipelineExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribePipelineExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribePipelineExecution)

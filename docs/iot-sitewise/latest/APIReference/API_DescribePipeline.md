---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePipeline.html
---

# DescribePipeline
<a name="API_DescribePipeline"></a>

Retrieves detailed information about a specific pipeline in a workspace.

## Request Syntax
<a name="API_DescribePipeline_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/pipelines/{{pipelineName}}?version={{pipelineVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePipeline_RequestParameters"></a>

The request uses the following URI parameters.

 ** [pipelineName](#API_DescribePipeline_RequestSyntax) **   <a name="iotsitewise-DescribePipeline-request-uri-pipelineName"></a>
The name of the pipeline.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [pipelineVersion](#API_DescribePipeline_RequestSyntax) **   <a name="iotsitewise-DescribePipeline-request-uri-pipelineVersion"></a>
The version number of the pipeline to retrieve. If not specified, returns the latest version.
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [workspaceName](#API_DescribePipeline_RequestSyntax) **   <a name="iotsitewise-DescribePipeline-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_DescribePipeline_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "computations": [
      {
         "computeNodeName": "string",
         "dependsOn": [ "string" ],
         "environmentVariables": {
            "string" : "string"
         },
         "taskName": "string"
      }
   ],
   "createdAt": number,
   "description": "string",
   "environmentVariables": {
      "string" : "string"
   },
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
   "version": "string",
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_DescribePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [computations](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-computations"></a>
The list of compute nodes that form the pipeline DAG.
Type: Array of [ComputeNode](API_ComputeNode.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [createdAt](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-createdAt"></a>
The time the pipeline was created, in Unix epoch time.
Type: Timestamp

 ** [description](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-description"></a>
The description of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [environmentVariables](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-environmentVariables"></a>
The environment variables shared across all compute nodes in the pipeline.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `(?!(?i)AWS_)[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [pipelineArn](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-pipelineArn"></a>
The ARN of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [pipelineName](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-pipelineName"></a>
A unique name of the pipeline within the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [status](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-status"></a>
The current lifecycle status of the pipeline.
Type: [ResourceStatus](API_ResourceStatus.md) object

 ** [updatedAt](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-updatedAt"></a>
The time the pipeline was last updated, in Unix epoch time.
Type: Timestamp

 ** [version](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-version"></a>
The version of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [workspaceName](#API_DescribePipeline_ResponseSyntax) **   <a name="iotsitewise-DescribePipeline-response-workspaceName"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_DescribePipeline_Errors"></a>

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
<a name="API_DescribePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribePipeline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribePipeline)

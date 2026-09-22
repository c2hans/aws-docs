---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowExecutions.html
---

# ListWorkflowExecutions
<a name="API_ListWorkflowExecutions"></a>

Returns a list of workflow runtime instance metadata objects for a specific image build version.

## Request Syntax
<a name="API_ListWorkflowExecutions_RequestSyntax"></a>

```
POST /ListWorkflowExecutions HTTP/1.1
Content-type: application/json

{
   "imageBuildVersionArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkflowExecutions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWorkflowExecutions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [imageBuildVersionArn](#API_ListWorkflowExecutions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowExecutions-request-imageBuildVersionArn"></a>
List all workflow runtime instances for the specified image build version resource ARN.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: Yes

 ** [maxResults](#API_ListWorkflowExecutions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowExecutions-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListWorkflowExecutions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowExecutions-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListWorkflowExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imageBuildVersionArn": "string",
   "message": "string",
   "nextToken": "string",
   "requestId": "string",
   "workflowExecutions": [
      {
         "endTime": "string",
         "message": "string",
         "parallelGroup": "string",
         "retried": boolean,
         "startTime": "string",
         "status": "string",
         "totalStepCount": number,
         "totalStepsFailed": number,
         "totalStepsSkipped": number,
         "totalStepsSucceeded": number,
         "type": "string",
         "workflowBuildVersionArn": "string",
         "workflowExecutionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkflowExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageBuildVersionArn](#API_ListWorkflowExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowExecutions-response-imageBuildVersionArn"></a>
The resource Amazon Resource Name (ARN) of the image build version for which you requested a list of workflow runtime details.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [message](#API_ListWorkflowExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowExecutions-response-message"></a>
The failure reason for the image build version, if it's in a failed state. This comes from the image itself, not from an individual workflow, so it's available even when no workflow executions remain for the image.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [nextToken](#API_ListWorkflowExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowExecutions-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListWorkflowExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowExecutions-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [workflowExecutions](#API_ListWorkflowExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowExecutions-response-workflowExecutions"></a>
An array of runtime details that represents each time a workflow ran for the requested image build version. Image Builder retains workflow execution records for a limited time, so this array can be empty for older image build versions.
Type: Array of [WorkflowExecutionMetadata](API_WorkflowExecutionMetadata.md) objects

## Errors
<a name="API_ListWorkflowExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_ListWorkflowExecutions_Examples"></a>

### List the workflow runtime instances for an image build version
<a name="API_ListWorkflowExecutions_Example_1"></a>

The following example lists the workflow runtime instances that ran for the specified image build version, which was built with the Image Builder default build and test workflows.

#### Sample Request
<a name="API_ListWorkflowExecutions_Example_1_Request"></a>

```
POST /ListWorkflowExecutions HTTP/1.1
Content-type: application/json

{
    "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1"
}
```

#### Sample Response
<a name="API_ListWorkflowExecutions_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "c78ef9a3-cce8-4e7d-ae96-426fb7e59f5d",
    "workflowExecutions": [
        {
            "workflowBuildVersionArn": "arn:aws:imagebuilder:us-west-2:aws:workflow/build/build-image/1.0.3/1",
            "workflowExecutionId": "wf-165b1cb6-3a62-4618-a021-94ddcbe32908",
            "type": "BUILD",
            "status": "COMPLETED",
            "totalStepCount": 7,
            "totalStepsSucceeded": 5,
            "totalStepsFailed": 0,
            "totalStepsSkipped": 2,
            "startTime": "2026-09-09T19:12:23.175Z",
            "endTime": "2026-09-09T19:19:06.158Z",
            "retried": false
        },
        {
            "workflowBuildVersionArn": "arn:aws:imagebuilder:us-west-2:aws:workflow/test/test-image/1.0.3/1",
            "workflowExecutionId": "wf-1a3639b8-1366-4b73-8347-706874020dad",
            "type": "TEST",
            "status": "COMPLETED",
            "totalStepCount": 4,
            "totalStepsSucceeded": 2,
            "totalStepsFailed": 0,
            "totalStepsSkipped": 2,
            "startTime": "2026-09-09T19:19:11.709Z",
            "endTime": "2026-09-09T19:21:47.830Z",
            "retried": false
        }
    ],
    "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1"
}
```

## See Also
<a name="API_ListWorkflowExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListWorkflowExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListWorkflowExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListWorkflowExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListWorkflowExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListWorkflowExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListWorkflowExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListWorkflowExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListWorkflowExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListWorkflowExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListWorkflowExecutions)

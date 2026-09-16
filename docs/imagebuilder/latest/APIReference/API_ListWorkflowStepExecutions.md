---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowStepExecutions.html
---

# ListWorkflowStepExecutions
<a name="API_ListWorkflowStepExecutions"></a>

Returns runtime data for each step in a runtime instance of the workflow that you specify in the request.

## Request Syntax
<a name="API_ListWorkflowStepExecutions_RequestSyntax"></a>

```
POST /ListWorkflowStepExecutions HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "workflowExecutionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkflowStepExecutions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWorkflowStepExecutions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListWorkflowStepExecutions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListWorkflowStepExecutions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [workflowExecutionId](#API_ListWorkflowStepExecutions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-request-workflowExecutionId"></a>
The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.
Type: String
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_ListWorkflowStepExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imageBuildVersionArn": "string",
   "message": "string",
   "nextToken": "string",
   "requestId": "string",
   "steps": [
      {
         "action": "string",
         "attemptNumber": number,
         "description": "string",
         "endTime": "string",
         "inputs": "string",
         "maxAttempts": number,
         "message": "string",
         "name": "string",
         "outputs": "string",
         "rollbackStatus": "string",
         "startTime": "string",
         "status": "string",
         "stepExecutionId": "string"
      }
   ],
   "workflowBuildVersionArn": "string",
   "workflowExecutionId": "string"
}
```

## Response Elements
<a name="API_ListWorkflowStepExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageBuildVersionArn](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-imageBuildVersionArn"></a>
The image build version resource Amazon Resource Name (ARN) that's associated with the specified runtime instance of the workflow.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [message](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-message"></a>
The output message from the list action, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [nextToken](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [steps](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-steps"></a>
Contains an array of runtime details that represents each step in this runtime instance of the workflow.
Type: Array of [WorkflowStepMetadata](API_WorkflowStepMetadata.md) objects

 ** [workflowBuildVersionArn](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-workflowBuildVersionArn"></a>
The build version Amazon Resource Name (ARN) for the Image Builder workflow resource that defines the steps for this runtime instance of the workflow.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [workflowExecutionId](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-workflowExecutionId"></a>
The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.
Type: String
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

## Errors
<a name="API_ListWorkflowStepExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_ListWorkflowStepExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListWorkflowStepExecutions)

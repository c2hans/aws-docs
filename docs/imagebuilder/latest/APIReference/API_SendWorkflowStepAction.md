---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_SendWorkflowStepAction.html
---

# SendWorkflowStepAction
<a name="API_SendWorkflowStepAction"></a>

Pauses or resumes image creation when the associated workflow runs a `WaitForAction` step.

## Request Syntax
<a name="API_SendWorkflowStepAction_RequestSyntax"></a>

```
PUT /SendWorkflowStepAction HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "clientToken": "{{string}}",
   "imageBuildVersionArn": "{{string}}",
   "reason": "{{string}}",
   "stepExecutionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendWorkflowStepAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendWorkflowStepAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_SendWorkflowStepAction_RequestSyntax) **   <a name="imagebuilder-SendWorkflowStepAction-request-action"></a>
The action to perform on the paused workflow step. The workflow step must be in a waiting state to accept an action. The request fails if the step has already timed out or been actioned.
Type: String
Valid Values: `RESUME | STOP`
Required: Yes

 ** [clientToken](#API_SendWorkflowStepAction_RequestSyntax) **   <a name="imagebuilder-SendWorkflowStepAction-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [imageBuildVersionArn](#API_SendWorkflowStepAction_RequestSyntax) **   <a name="imagebuilder-SendWorkflowStepAction-request-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image build version associated with the workflow step execution. This value must match the image that owns the waiting step. If the ARN does not correspond to the image running the workflow, then the request fails with a validation error.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: Yes

 ** [reason](#API_SendWorkflowStepAction_RequestSyntax) **   <a name="imagebuilder-SendWorkflowStepAction-request-reason"></a>
The reason for the action. This value is stored with the step execution record and is accessible in subsequent workflow steps via step output references.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [stepExecutionId](#API_SendWorkflowStepAction_RequestSyntax) **   <a name="imagebuilder-SendWorkflowStepAction-request-stepExecutionId"></a>
Uniquely identifies the workflow step that sent the step action.
Type: String
Pattern: `^step-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_SendWorkflowStepAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "imageBuildVersionArn": "string",
   "stepExecutionId": "string"
}
```

## Response Elements
<a name="API_SendWorkflowStepAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_SendWorkflowStepAction_ResponseSyntax) **   <a name="imagebuilder-SendWorkflowStepAction-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [imageBuildVersionArn](#API_SendWorkflowStepAction_ResponseSyntax) **   <a name="imagebuilder-SendWorkflowStepAction-response-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image build version that received the action request.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [stepExecutionId](#API_SendWorkflowStepAction_ResponseSyntax) **   <a name="imagebuilder-SendWorkflowStepAction-response-stepExecutionId"></a>
The workflow step that sent the step action.
Type: String
Pattern: `^step-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

## Errors
<a name="API_SendWorkflowStepAction_Errors"></a>

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

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value that you provided for the specified parameter is invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
At least one of the resources referenced by your request does not exist.
HTTP Status Code: 404

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_SendWorkflowStepAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/SendWorkflowStepAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/SendWorkflowStepAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/SendWorkflowStepAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/SendWorkflowStepAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/SendWorkflowStepAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/SendWorkflowStepAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/SendWorkflowStepAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/SendWorkflowStepAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/SendWorkflowStepAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/SendWorkflowStepAction)

---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_PutLifecycleEventHookExecutionStatus.html
---

# PutLifecycleEventHookExecutionStatus
<a name="API_PutLifecycleEventHookExecutionStatus"></a>

 Sets the result of a Lambda validation function. The function validates lifecycle hooks during a deployment that uses the AWS Lambda or Amazon ECS compute platform. For AWS Lambda deployments, the available lifecycle hooks are `BeforeAllowTraffic` and `AfterAllowTraffic`. For Amazon ECS deployments, the available lifecycle hooks are `BeforeInstall`, `AfterInstall`, `AfterAllowTestTraffic`, `BeforeAllowTraffic`, and `AfterAllowTraffic`. Lambda validation functions return `Succeeded` or `Failed`. For more information, see [AppSpec 'hooks' Section for an AWS Lambda Deployment ](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#appspec-hooks-lambda) and [AppSpec 'hooks' Section for an Amazon ECS Deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#appspec-hooks-ecs).

## Request Syntax
<a name="API_PutLifecycleEventHookExecutionStatus_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "lifecycleEventHookExecutionId": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_PutLifecycleEventHookExecutionStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_PutLifecycleEventHookExecutionStatus_RequestSyntax) **   <a name="CodeDeploy-PutLifecycleEventHookExecutionStatus-request-deploymentId"></a>
 The unique ID of a deployment. Pass this ID to a Lambda function that validates a deployment lifecycle event.
Type: String
Required: No

 ** [lifecycleEventHookExecutionId](#API_PutLifecycleEventHookExecutionStatus_RequestSyntax) **   <a name="CodeDeploy-PutLifecycleEventHookExecutionStatus-request-lifecycleEventHookExecutionId"></a>
 The execution ID of a deployment's lifecycle hook. A deployment lifecycle hook is specified in the `hooks` section of the AppSpec file.
Type: String
Required: No

 ** [status](#API_PutLifecycleEventHookExecutionStatus_RequestSyntax) **   <a name="CodeDeploy-PutLifecycleEventHookExecutionStatus-request-status"></a>
The result of a Lambda function that validates a deployment lifecycle event. The values listed in **Valid Values** are valid for lifecycle statuses in general; however, only `Succeeded` and `Failed` can be passed successfully in your API call.
Type: String
Valid Values: `Pending | InProgress | Succeeded | Failed | Skipped | Unknown`
Required: No

## Response Syntax
<a name="API_PutLifecycleEventHookExecutionStatus_ResponseSyntax"></a>

```
{
   "lifecycleEventHookExecutionId": "string"
}
```

## Response Elements
<a name="API_PutLifecycleEventHookExecutionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecycleEventHookExecutionId](#API_PutLifecycleEventHookExecutionStatus_ResponseSyntax) **   <a name="CodeDeploy-PutLifecycleEventHookExecutionStatus-response-lifecycleEventHookExecutionId"></a>
The execution ID of the lifecycle event hook. A hook is specified in the `hooks` section of the deployment's AppSpec file.
Type: String

## Errors
<a name="API_PutLifecycleEventHookExecutionStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeploymentDoesNotExistException **
The deployment with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentIdRequiredException **
At least one deployment ID must be specified.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidLifecycleEventHookExecutionIdException **
A lifecycle event hook is invalid. Review the `hooks` section in your AppSpec file to ensure the lifecycle events and `hooks` functions are valid.
HTTP Status Code: 400

 ** InvalidLifecycleEventHookExecutionStatusException **
The result of a Lambda validation function that verifies a lifecycle event is invalid. It should return `Succeeded` or `Failed`.
HTTP Status Code: 400

 ** LifecycleEventAlreadyCompletedException **
An attempt to return the status of an already completed lifecycle event occurred.
HTTP Status Code: 400

 ** UnsupportedActionForDeploymentTypeException **
A call was submitted that is not supported for the specified deployment type.
HTTP Status Code: 400

## See Also
<a name="API_PutLifecycleEventHookExecutionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

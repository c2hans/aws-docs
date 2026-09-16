---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExecuteCommand.html
---

# ExecuteCommand
<a name="API_ExecuteCommand"></a>

Runs a command remotely on a container within a task.

If you use a condition key in your IAM policy to refine the conditions for the policy statement, for example limit the actions to a specific cluster, you receive an `AccessDeniedException` when there is a mismatch between the condition key value and the corresponding parameter value.

For information about required permissions and considerations, see [Using Amazon ECS Exec for debugging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html) in the *Amazon ECS Developer Guide*.

## Request Syntax
<a name="API_ExecuteCommand_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "command": "{{string}}",
   "container": "{{string}}",
   "interactive": {{boolean}},
   "task": "{{string}}"
}
```

## Request Parameters
<a name="API_ExecuteCommand_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_ExecuteCommand_RequestSyntax) **   <a name="ECS-ExecuteCommand-request-cluster"></a>
The Amazon Resource Name (ARN) or short name of the cluster the task is running in. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [command](#API_ExecuteCommand_RequestSyntax) **   <a name="ECS-ExecuteCommand-request-command"></a>
The command to run on the container.
Type: String
Required: Yes

 ** [container](#API_ExecuteCommand_RequestSyntax) **   <a name="ECS-ExecuteCommand-request-container"></a>
The name of the container to execute the command on. A container name only needs to be specified for tasks containing multiple containers.
Type: String
Required: No

 ** [interactive](#API_ExecuteCommand_RequestSyntax) **   <a name="ECS-ExecuteCommand-request-interactive"></a>
Use this flag to run your command in interactive mode.
Type: Boolean
Required: Yes

 ** [task](#API_ExecuteCommand_RequestSyntax) **   <a name="ECS-ExecuteCommand-request-task"></a>
The Amazon Resource Name (ARN) or ID of the task the container is part of.
Type: String
Required: Yes

## Response Syntax
<a name="API_ExecuteCommand_ResponseSyntax"></a>

```
{
   "clusterArn": "string",
   "containerArn": "string",
   "containerName": "string",
   "interactive": boolean,
   "session": {
      "sessionId": "string",
      "streamUrl": "string",
      "tokenValue": "string"
   },
   "taskArn": "string"
}
```

## Response Elements
<a name="API_ExecuteCommand_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clusterArn](#API_ExecuteCommand_ResponseSyntax) **   <a name="ECS-ExecuteCommand-response-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster.
Type: String

 ** [containerArn](#API_ExecuteCommand_ResponseSyntax) **   <a name="ECS-ExecuteCommand-response-containerArn"></a>
The Amazon Resource Name (ARN) of the container.
Type: String

 ** [containerName](#API_ExecuteCommand_ResponseSyntax) **   <a name="ECS-ExecuteCommand-response-containerName"></a>
The name of the container.
Type: String

 ** [interactive](#API_ExecuteCommand_ResponseSyntax) **   <a name="ECS-ExecuteCommand-response-interactive"></a>
Determines whether the execute command session is running in interactive mode. Amazon ECS only supports initiating interactive sessions, so you must specify `true` for this value.
Type: Boolean

 ** [session](#API_ExecuteCommand_ResponseSyntax) **   <a name="ECS-ExecuteCommand-response-session"></a>
The details of the SSM session that was created for this instance of execute-command.
Type: [Session](API_Session.md) object

 ** [taskArn](#API_ExecuteCommand_ResponseSyntax) **   <a name="ECS-ExecuteCommand-response-taskArn"></a>
The Amazon Resource Name (ARN) of the task.
Type: String

## Errors
<a name="API_ExecuteCommand_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterNotFoundException **
The specified cluster wasn't found. You can view your available clusters with [ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html). Amazon ECS clusters are Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

 ** TargetNotConnectedException **
The execute command cannot run. This error can be caused by any of the following configuration issues:
+ Incorrect IAM permissions
+ The SSM agent is not installed or is not running
+  There is an interface Amazon VPC endpoint for Amazon ECS, but there is not one for Systems Manager Session Manager
For information about how to troubleshoot the issues, see [Troubleshooting issues with ECS Exec](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html) in the *Amazon Elastic Container Service Developer Guide*.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## See Also
<a name="API_ExecuteCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ExecuteCommand)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ExecuteCommand)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ExecuteCommand)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ExecuteCommand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ExecuteCommand)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ExecuteCommand)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ExecuteCommand)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ExecuteCommand)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ExecuteCommand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ExecuteCommand)

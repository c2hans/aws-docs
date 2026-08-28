---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_SubmitTaskStateChange.html
---

# SubmitTaskStateChange
<a name="API_SubmitTaskStateChange"></a>

**Note**
This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.

Sent to acknowledge that a task changed states.

## Request Syntax
<a name="API_SubmitTaskStateChange_RequestSyntax"></a>

```
{
   "attachments": [
      {
         "attachmentArn": "{{string}}",
         "status": "{{string}}"
      }
   ],
   "cluster": "{{string}}",
   "containers": [
      {
         "containerName": "{{string}}",
         "exitCode": {{number}},
         "imageDigest": "{{string}}",
         "networkBindings": [
            {
               "bindIP": "{{string}}",
               "containerPort": {{number}},
               "containerPortRange": "{{string}}",
               "hostPort": {{number}},
               "hostPortRange": "{{string}}",
               "protocol": "{{string}}"
            }
         ],
         "reason": "{{string}}",
         "runtimeId": "{{string}}",
         "status": "{{string}}"
      }
   ],
   "executionStoppedAt": {{number}},
   "managedAgents": [
      {
         "containerName": "{{string}}",
         "managedAgentName": "{{string}}",
         "reason": "{{string}}",
         "status": "{{string}}"
      }
   ],
   "pullStartedAt": {{number}},
   "pullStoppedAt": {{number}},
   "reason": "{{string}}",
   "status": "{{string}}",
   "task": "{{string}}"
}
```

## Request Parameters
<a name="API_SubmitTaskStateChange_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attachments](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-attachments"></a>
Any attachments associated with the state change request.
Type: Array of [AttachmentStateChange](API_AttachmentStateChange.md) objects
Required: No

 ** [cluster](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task.
Type: String
Required: No

 ** [containers](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-containers"></a>
Any containers that's associated with the state change request.
Type: Array of [ContainerStateChange](API_ContainerStateChange.md) objects
Required: No

 ** [executionStoppedAt](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-executionStoppedAt"></a>
The Unix timestamp for the time when the task execution stopped.
Type: Timestamp
Required: No

 ** [managedAgents](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-managedAgents"></a>
The details for the managed agent that's associated with the task.
Type: Array of [ManagedAgentStateChange](API_ManagedAgentStateChange.md) objects
Required: No

 ** [pullStartedAt](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-pullStartedAt"></a>
The Unix timestamp for the time when the container image pull started.
Type: Timestamp
Required: No

 ** [pullStoppedAt](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-pullStoppedAt"></a>
The Unix timestamp for the time when the container image pull completed.
Type: Timestamp
Required: No

 ** [reason](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-reason"></a>
The reason for the state change request.
Type: String
Required: No

 ** [status](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-status"></a>
The status of the state change request.
Type: String
Required: No

 ** [task](#API_SubmitTaskStateChange_RequestSyntax) **   <a name="ECS-SubmitTaskStateChange-request-task"></a>
The task ID or full ARN of the task in the state change request.
Type: String
Required: No

## Response Syntax
<a name="API_SubmitTaskStateChange_ResponseSyntax"></a>

```
{
   "acknowledgment": "string"
}
```

## Response Elements
<a name="API_SubmitTaskStateChange_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [acknowledgment](#API_SubmitTaskStateChange_ResponseSyntax) **   <a name="ECS-SubmitTaskStateChange-response-acknowledgment"></a>
Acknowledgement of the state change.
Type: String

## Errors
<a name="API_SubmitTaskStateChange_Errors"></a>

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

## See Also
<a name="API_SubmitTaskStateChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/SubmitTaskStateChange)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/SubmitTaskStateChange)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/SubmitTaskStateChange)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/SubmitTaskStateChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/SubmitTaskStateChange)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/SubmitTaskStateChange)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/SubmitTaskStateChange)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/SubmitTaskStateChange)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/SubmitTaskStateChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/SubmitTaskStateChange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

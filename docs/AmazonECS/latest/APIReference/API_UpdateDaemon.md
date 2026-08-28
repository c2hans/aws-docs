---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateDaemon.html
---

# UpdateDaemon
<a name="API_UpdateDaemon"></a>

Updates the specified daemon. When you update a daemon, a new deployment is triggered that progressively rolls out the changes to the container instances associated with the daemon's capacity providers. For more information, see [Daemon deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-deployments.html) in the *Amazon Elastic Container Service Developer Guide*.

Amazon ECS drains existing container instances and provisions new instances with the updated daemon. Amazon ECS automatically launches replacement tasks for your services.

**Important**
Updating a daemon triggers a rolling deployment that drains and replaces container instances. Plan updates during maintenance windows to minimize impact on running services.

**Note**
ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.

## Request Syntax
<a name="API_UpdateDaemon_RequestSyntax"></a>

```
{
   "capacityProviderArns": [ "{{string}}" ],
   "daemonArn": "{{string}}",
   "daemonTaskDefinitionArn": "{{string}}",
   "deploymentConfiguration": {
      "alarms": {
         "alarmNames": [ "{{string}}" ],
         "enable": {{boolean}}
      },
      "bakeTimeInMinutes": {{number}},
      "drainPercent": {{number}}
   },
   "enableECSManagedTags": {{boolean}},
   "enableExecuteCommand": {{boolean}},
   "propagateTags": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDaemon_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capacityProviderArns](#API_UpdateDaemon_RequestSyntax) **   <a name="ECS-UpdateDaemon-request-capacityProviderArns"></a>
The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon.
Type: Array of strings
Required: Yes

 ** [daemonArn](#API_UpdateDaemon_RequestSyntax) **   <a name="ECS-UpdateDaemon-request-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon to update.
Type: String
Required: Yes

 ** [daemonTaskDefinitionArn](#API_UpdateDaemon_RequestSyntax) **   <a name="ECS-UpdateDaemon-request-daemonTaskDefinitionArn"></a>
The Amazon Resource Name (ARN) of the daemon task definition to use for the updated daemon.
Type: String
Required: Yes

 ** [deploymentConfiguration](#API_UpdateDaemon_RequestSyntax) **   <a name="ECS-UpdateDaemon-request-deploymentConfiguration"></a>
Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.
Type: [DaemonDeploymentConfiguration](API_DaemonDeploymentConfiguration.md) object
Required: No

 ** [enableECSManagedTags](#API_UpdateDaemon_RequestSyntax) **   <a name="ECS-UpdateDaemon-request-enableECSManagedTags"></a>
Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see [Tagging your Amazon ECS resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: Boolean
Required: No

 ** [enableExecuteCommand](#API_UpdateDaemon_RequestSyntax) **   <a name="ECS-UpdateDaemon-request-enableExecuteCommand"></a>
If `true`, the execute command functionality is turned on for all tasks in the daemon. If `false`, the execute command functionality is turned off.
Type: Boolean
Required: No

 ** [propagateTags](#API_UpdateDaemon_RequestSyntax) **   <a name="ECS-UpdateDaemon-request-propagateTags"></a>
Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation.
Type: String
Valid Values: `DAEMON | NONE`
Required: No

## Response Syntax
<a name="API_UpdateDaemon_ResponseSyntax"></a>

```
{
   "createdAt": number,
   "daemonArn": "string",
   "deploymentArn": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateDaemon_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateDaemon_ResponseSyntax) **   <a name="ECS-UpdateDaemon-response-createdAt"></a>
The Unix timestamp for the time when the daemon was created.
Type: Timestamp

 ** [daemonArn](#API_UpdateDaemon_ResponseSyntax) **   <a name="ECS-UpdateDaemon-response-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon.
Type: String

 ** [deploymentArn](#API_UpdateDaemon_ResponseSyntax) **   <a name="ECS-UpdateDaemon-response-deploymentArn"></a>
The Amazon Resource Name (ARN) of the daemon deployment that was triggered by the update.
Type: String

 ** [status](#API_UpdateDaemon_ResponseSyntax) **   <a name="ECS-UpdateDaemon-response-status"></a>
The status of the daemon.
Type: String
Valid Values: `ACTIVE | DELETE_IN_PROGRESS`

 ** [updatedAt](#API_UpdateDaemon_ResponseSyntax) **   <a name="ECS-UpdateDaemon-response-updatedAt"></a>
The Unix timestamp for the time when the daemon was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateDaemon_Errors"></a>

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

 ** DaemonNotActiveException **
The specified daemon isn't active. You can't update a daemon that's inactive. If you have previously deleted a daemon, you can re-create it with [CreateDaemon](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** DaemonNotFoundException **
The specified daemon wasn't found. You can view your available daemons with [ListDaemons](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html). Amazon ECS daemons are cluster specific and Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** PlatformUnknownException **
The specified platform version doesn't exist.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_UpdateDaemon_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_UpdateDaemon_Example_1"></a>

This example updates the my-monitoring-daemon daemon to use a new daemon task definition revision.

#### Sample Request
<a name="API_UpdateDaemon_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 405
X-Amz-Target: AmazonEC2ContainerServiceV20141113.UpdateDaemon
X-Amz-Date: 20250320T153000Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon",
  "daemonTaskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:2",
  "capacityProviderArns": [
    "arn:aws:ecs:us-east-1:123456789012:capacity-provider/my-capacity-provider"
  ],
  "deploymentConfiguration": {
    "drainPercent": 10.0,
    "bakeTimeInMinutes": 5
  }
}
```

#### Sample Response
<a name="API_UpdateDaemon_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 20 Mar 2025 15:30:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 326
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon",
  "status": "ACTIVE",
  "createdAt": "2025-03-15T12:00:00.000Z",
  "updatedAt": "2025-03-20T15:30:00.000Z",
  "deploymentArn": "arn:aws:ecs:us-east-1:123456789012:daemon-deployment/my-cluster/my-monitoring-daemon/xY9zA8bC7dE6fG5h"
}
```

## See Also
<a name="API_UpdateDaemon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/UpdateDaemon)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/UpdateDaemon)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateDaemon)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/UpdateDaemon)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateDaemon)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/UpdateDaemon)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/UpdateDaemon)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/UpdateDaemon)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/UpdateDaemon)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateDaemon)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

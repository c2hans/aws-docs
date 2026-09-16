---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html
---

# CreateDaemon
<a name="API_CreateDaemon"></a>

Creates a new daemon in the specified cluster and capacity providers. A daemon deploys cross-cutting software agents such as security monitoring, telemetry, and logging independently across your Amazon ECS infrastructure.

Amazon ECS deploys exactly one daemon task on each container instance of the specified capacity providers. When a container instance registers with the cluster, Amazon ECS automatically starts daemon tasks. Amazon ECS starts a daemon task before scheduling other tasks.

Daemons are essential for instance health - if a daemon task stops, Amazon ECS automatically drains and replaces that container instance.

**Note**
ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.

## Request Syntax
<a name="API_CreateDaemon_RequestSyntax"></a>

```
{
   "capacityProviderArns": [ "{{string}}" ],
   "clientToken": "{{string}}",
   "clusterArn": "{{string}}",
   "critical": {{boolean}},
   "daemonName": "{{string}}",
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
   "propagateTags": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDaemon_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capacityProviderArns](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-capacityProviderArns"></a>
The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon. The daemon deploys tasks on container instances managed by these capacity providers.
Type: Array of strings
Required: Yes

 ** [clientToken](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-clientToken"></a>
An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.
Type: String
Required: No

 ** [clusterArn](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster to create the daemon in.
Type: String
Required: No

 ** [critical](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-critical"></a>
If the `critical` parameter of a daemon is `true`, and the daemon task fails, stops, or becomes unhealthy, Amazon ECS drains the container instance and stops the other tasks running on it. If the `critical` parameter is `false`, the daemon task failure doesn't affect the other tasks on the instance. The default value is `true`.
A non-critical daemon doesn't block instance registration. The container instance becomes active and continues to run your other tasks, whether the daemon task fails during scale-out or during a deployment.
Amazon ECS emits an EventBridge event when a daemon task fails to start, for both critical and non-critical daemons.
Daemon task launch failures during a deployment are still counted by the deployment circuit breaker. The circuit breaker can roll back an unstable target revision.
Type: Boolean
Required: No

 ** [daemonName](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-daemonName"></a>
The name of the daemon. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.
Type: String
Required: Yes

 ** [daemonTaskDefinitionArn](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-daemonTaskDefinitionArn"></a>
The Amazon Resource Name (ARN) of the daemon task definition to use for the daemon.
Type: String
Required: Yes

 ** [deploymentConfiguration](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-deploymentConfiguration"></a>
Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.
Type: [DaemonDeploymentConfiguration](API_DaemonDeploymentConfiguration.md) object
Required: No

 ** [enableECSManagedTags](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-enableECSManagedTags"></a>
Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see [Tagging your Amazon ECS resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: Boolean
Required: No

 ** [enableExecuteCommand](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-enableExecuteCommand"></a>
Determines whether the execute command functionality is turned on for the daemon. If `true`, the execute command functionality is turned on for all tasks in the daemon.
Type: Boolean
Required: No

 ** [propagateTags](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-propagateTags"></a>
Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation. To add tags to a task after task creation, use the [TagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html) API action.
Type: String
Valid Values: `DAEMON | NONE`
Required: No

 ** [tags](#API_CreateDaemon_RequestSyntax) **   <a name="ECS-CreateDaemon-request-tags"></a>
The metadata that you apply to the daemon to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateDaemon_ResponseSyntax"></a>

```
{
   "createdAt": number,
   "daemonArn": "string",
   "deploymentArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateDaemon_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateDaemon_ResponseSyntax) **   <a name="ECS-CreateDaemon-response-createdAt"></a>
The Unix timestamp for the time when the daemon was created.
Type: Timestamp

 ** [daemonArn](#API_CreateDaemon_ResponseSyntax) **   <a name="ECS-CreateDaemon-response-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon.
Type: String

 ** [deploymentArn](#API_CreateDaemon_ResponseSyntax) **   <a name="ECS-CreateDaemon-response-deploymentArn"></a>
The Amazon Resource Name (ARN) of the initial daemon deployment. This deployment places daemon tasks on each container instance of the specified capacity providers.
Type: String

 ** [status](#API_CreateDaemon_ResponseSyntax) **   <a name="ECS-CreateDaemon-response-status"></a>
The status of the daemon.
Type: String
Valid Values: `ACTIVE | DELETE_IN_PROGRESS`

## Errors
<a name="API_CreateDaemon_Errors"></a>

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
<a name="API_CreateDaemon_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Create a monitoring daemon in a cluster
<a name="API_CreateDaemon_Example_1"></a>

This example creates a daemon named my-monitoring-daemon in the specified cluster using the monitoring-agent daemon task definition.

#### Sample Request
<a name="API_CreateDaemon_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 426
X-Amz-Target: AmazonEC2ContainerServiceV20141113.CreateDaemon
X-Amz-Date: 20250315T120000Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "daemonName": "my-monitoring-daemon",
  "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
  "daemonTaskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:1",
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
<a name="API_CreateDaemon_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 15 Mar 2025 12:00:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 283
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon",
  "status": "ACTIVE",
  "createdAt": "2025-03-15T12:00:00.000Z",
  "deploymentArn": "arn:aws:ecs:us-east-1:123456789012:daemon-deployment/my-cluster/my-monitoring-daemon/aB1cD2eF3gH4iJ5k"
}
```

## See Also
<a name="API_CreateDaemon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/CreateDaemon)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/CreateDaemon)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CreateDaemon)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/CreateDaemon)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CreateDaemon)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/CreateDaemon)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/CreateDaemon)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/CreateDaemon)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/CreateDaemon)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CreateDaemon)

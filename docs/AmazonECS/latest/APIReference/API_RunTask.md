---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html
---

# RunTask
<a name="API_RunTask"></a>

Starts a new task using the specified task definition.

**Note**
On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.

**Note**
Amazon Elastic Inference (EI) is no longer available to customers.

You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see [Scheduling Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html) in the *Amazon Elastic Container Service Developer Guide*.

Alternatively, you can use `StartTask` to use your own scheduler or place tasks manually on specific container instances.

You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more information, see [Amazon EBS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types) in the *Amazon Elastic Container Service Developer Guide*.

The Amazon ECS API follows an eventual consistency model. This is because of the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. Keep this in mind when you carry out an API command that immediately follows a previous API command.

To manage eventual consistency, you can do the following:
+ Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time.
+ Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time.

If you get a `ConflictException` error, the `RunTask` request could not be processed due to conflicts. The provided `clientToken` is already in use with a different `RunTask` request. The `resourceIds` are the existing task ARNs which are already associated with the `clientToken`.

To fix this issue:
+ Run `RunTask` with a unique `clientToken`.
+ Run `RunTask` with the `clientToken` and the original set of parameters

If you get a `ClientException`error, the `RunTask` could not be processed because you use managed scaling and there is a capacity error because the quota of tasks in the `PROVISIONING` per cluster has been reached. For information about the service quotas, see [Amazon ECS service quotas](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html).

## Request Syntax
<a name="API_RunTask_RequestSyntax"></a>

```
{
   "capacityProviderStrategy": [
      {
         "base": {{number}},
         "capacityProvider": "{{string}}",
         "weight": {{number}}
      }
   ],
   "clientToken": "{{string}}",
   "cluster": "{{string}}",
   "count": {{number}},
   "enableECSManagedTags": {{boolean}},
   "enableExecuteCommand": {{boolean}},
   "group": "{{string}}",
   "launchType": "{{string}}",
   "networkConfiguration": {
      "awsvpcConfiguration": {
         "assignPublicIp": "{{string}}",
         "securityGroups": [ "{{string}}" ],
         "subnets": [ "{{string}}" ]
      }
   },
   "overrides": {
      "containerOverrides": [
         {
            "command": [ "{{string}}" ],
            "cpu": {{number}},
            "environment": [
               {
                  "name": "{{string}}",
                  "value": "{{string}}"
               }
            ],
            "environmentFiles": [
               {
                  "type": "{{string}}",
                  "value": "{{string}}"
               }
            ],
            "memory": {{number}},
            "memoryReservation": {{number}},
            "name": "{{string}}",
            "resourceRequirements": [
               {
                  "type": "{{string}}",
                  "value": "{{string}}"
               }
            ]
         }
      ],
      "cpu": "{{string}}",
      "ephemeralStorage": {
         "sizeInGiB": {{number}}
      },
      "executionRoleArn": "{{string}}",
      "inferenceAcceleratorOverrides": [
         {
            "deviceName": "{{string}}",
            "deviceType": "{{string}}"
         }
      ],
      "memory": "{{string}}",
      "taskRoleArn": "{{string}}"
   },
   "placementConstraints": [
      {
         "expression": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "placementStrategy": [
      {
         "field": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "platformVersion": "{{string}}",
   "propagateTags": "{{string}}",
   "referenceId": "{{string}}",
   "startedBy": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "taskDefinition": "{{string}}",
   "volumeConfigurations": [
      {
         "managedEBSVolume": {
            "encrypted": {{boolean}},
            "filesystemType": "{{string}}",
            "iops": {{number}},
            "kmsKeyId": "{{string}}",
            "roleArn": "{{string}}",
            "sizeInGiB": {{number}},
            "snapshotId": "{{string}}",
            "tagSpecifications": [
               {
                  "propagateTags": "{{string}}",
                  "resourceType": "{{string}}",
                  "tags": [
                     {
                        "key": "{{string}}",
                        "value": "{{string}}"
                     }
                  ]
               }
            ],
            "terminationPolicy": {
               "deleteOnTermination": {{boolean}}
            },
            "throughput": {{number}},
            "volumeInitializationRate": {{number}},
            "volumeType": "{{string}}"
         },
         "name": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_RunTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capacityProviderStrategy](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-capacityProviderStrategy"></a>
The capacity provider strategy to use for the task.
If you want to use Amazon ECS Managed Instances, you must use the `capacityProviderStrategy` request parameter and omit the `launchType` request parameter.
If a `capacityProviderStrategy` is specified, the `launchType` parameter must be omitted. If no `capacityProviderStrategy` or `launchType` is specified, the `defaultCapacityProviderStrategy` for the cluster is used.
When you use cluster auto scaling, you must specify `capacityProviderStrategy` and not `launchType`.
A capacity provider strategy can contain a maximum of 20 capacity providers.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Required: No

 ** [clientToken](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-clientToken"></a>
An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 64 characters are allowed. The valid characters are characters in the range of 33-126, inclusive. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/ECS_Idempotency.html).
Type: String
Required: No

 ** [cluster](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster to run your task on. If you do not specify a cluster, the default cluster is assumed.
Each account receives a default cluster the first time you use the service, but you may also create other clusters.
Type: String
Required: No

 ** [count](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-count"></a>
The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks for each call.
Type: Integer
Required: No

 ** [enableECSManagedTags](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-enableECSManagedTags"></a>
Specifies whether to use Amazon ECS managed tags for the task. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: Boolean
Required: No

 ** [enableExecuteCommand](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-enableExecuteCommand"></a>
Determines whether to use the execute command functionality for the containers in this task. If `true`, this enables execute command functionality on all containers in the task.
If `true`, then the task definition must have a task role, or you must provide one as an override.
Type: Boolean
Required: No

 ** [group](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-group"></a>
The name of the task group to associate with the task. The default value is the family name of the task definition (for example, `family:my-family-name`).
Type: String
Required: No

 ** [launchType](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-launchType"></a>
The infrastructure to run your standalone task on. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.
If you want to use Amazon ECS Managed Instances, you must use the `capacityProviderStrategy` request parameter and omit the `launchType` request parameter.
The `FARGATE` launch type runs your tasks on AWS Fargate On-Demand infrastructure.
Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see [AWS Fargate capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html) in the *Amazon ECS Developer Guide*.
The `EC2` launch type runs your tasks on Amazon EC2 instances registered to your cluster.
The `EXTERNAL` launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.
A task can use either a launch type or a capacity provider strategy. If a `launchType` is specified, the `capacityProviderStrategy` parameter must be omitted.
When you use cluster auto scaling, you must specify `capacityProviderStrategy` and not `launchType`.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** [networkConfiguration](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-networkConfiguration"></a>
The network configuration for the task. This parameter is required for task definitions that use the `awsvpc` network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see [Task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [overrides](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-overrides"></a>
A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that's specified in the task definition or Docker image) with a `command` override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an `environment` override.
A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.
Type: [TaskOverride](API_TaskOverride.md) object
Required: No

 ** [placementConstraints](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-placementConstraints"></a>
An array of placement constraint objects to use for the task. You can specify up to 10 constraints for each task (including constraints in the task definition and those specified at runtime).
Type: Array of [PlacementConstraint](API_PlacementConstraint.md) objects
Required: No

 ** [placementStrategy](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-placementStrategy"></a>
The placement strategy objects to use for the task. You can specify a maximum of 5 strategy rules for each task.
Type: Array of [PlacementStrategy](API_PlacementStrategy.md) objects
Required: No

 ** [platformVersion](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-platformVersion"></a>
The platform version the task uses. A platform version is only specified for tasks hosted on Fargate. If one isn't specified, the `LATEST` platform version is used. For more information, see [AWS Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** [propagateTags](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-propagateTags"></a>
Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the[TagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html) API action.
An error will be received if you specify the `SERVICE` option when running a task.
Type: String
Valid Values: `TASK_DEFINITION | SERVICE | NONE`
Required: No

 ** [referenceId](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-referenceId"></a>
This parameter is only used by Amazon ECS. It is not intended for use by customers.
Type: String
Required: No

 ** [startedBy](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-startedBy"></a>
An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the `startedBy` parameter. You can then identify which tasks belong to that job by filtering the results of a [ListTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html) call with the `startedBy` value. Up to 128 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (\_) are allowed.
If a task is started by an Amazon ECS service, then the `startedBy` parameter contains the deployment ID of the service that starts it.
Type: String
Required: No

 ** [tags](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-tags"></a>
The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.
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

 ** [taskDefinition](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-taskDefinition"></a>
The `family` and `revision` (`family:revision`) or full ARN of the task definition to run. If a `revision` isn't specified, the latest `ACTIVE` revision is used.
The full ARN value must match the value that you specified as the `Resource` of the principal's permissions policy.
When you specify a task definition, you must either specify a specific revision, or all revisions in the ARN.
To specify a specific revision, include the revision number in the ARN. For example, to specify revision 2, use `arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:2`.
To specify all revisions, use the wildcard (\*) in the ARN. For example, to specify all revisions, use `arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:*`.
For more information, see [Policy Resources for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) in the Amazon Elastic Container Service Developer Guide.
Type: String
Required: Yes

 ** [volumeConfigurations](#API_RunTask_RequestSyntax) **   <a name="ECS-RunTask-request-volumeConfigurations"></a>
The details of the volume that was `configuredAtLaunch`. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in [TaskManagedEBSVolumeConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html). The `name` of the volume must match the `name` from the task definition.
Type: Array of [TaskVolumeConfiguration](API_TaskVolumeConfiguration.md) objects
Required: No

## Response Syntax
<a name="API_RunTask_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "arn": "string",
         "detail": "string",
         "reason": "string"
      }
   ],
   "tasks": [
      {
         "attachments": [
            {
               "details": [
                  {
                     "name": "string",
                     "value": "string"
                  }
               ],
               "id": "string",
               "status": "string",
               "type": "string"
            }
         ],
         "attributes": [
            {
               "name": "string",
               "targetId": "string",
               "targetType": "string",
               "value": "string"
            }
         ],
         "availabilityZone": "string",
         "capacityProviderName": "string",
         "clusterArn": "string",
         "connectivity": "string",
         "connectivityAt": number,
         "containerInstanceArn": "string",
         "containers": [
            {
               "containerArn": "string",
               "cpu": "string",
               "exitCode": number,
               "gpuIds": [ "string" ],
               "healthStatus": "string",
               "image": "string",
               "imageDigest": "string",
               "lastStatus": "string",
               "managedAgents": [
                  {
                     "lastStartedAt": number,
                     "lastStatus": "string",
                     "name": "string",
                     "reason": "string"
                  }
               ],
               "memory": "string",
               "memoryReservation": "string",
               "name": "string",
               "networkBindings": [
                  {
                     "bindIP": "string",
                     "containerPort": number,
                     "containerPortRange": "string",
                     "hostPort": number,
                     "hostPortRange": "string",
                     "protocol": "string"
                  }
               ],
               "networkInterfaces": [
                  {
                     "attachmentId": "string",
                     "ipv6Address": "string",
                     "privateIpv4Address": "string"
                  }
               ],
               "neuronDeviceIds": [ "string" ],
               "reason": "string",
               "runtimeId": "string",
               "taskArn": "string"
            }
         ],
         "cpu": "string",
         "createdAt": number,
         "desiredStatus": "string",
         "enableExecuteCommand": boolean,
         "ephemeralStorage": {
            "sizeInGiB": number
         },
         "executionStoppedAt": number,
         "fargateEphemeralStorage": {
            "kmsKeyId": "string",
            "sizeInGiB": number
         },
         "group": "string",
         "healthStatus": "string",
         "inferenceAccelerators": [
            {
               "deviceName": "string",
               "deviceType": "string"
            }
         ],
         "lastStatus": "string",
         "launchType": "string",
         "memory": "string",
         "overrides": {
            "containerOverrides": [
               {
                  "command": [ "string" ],
                  "cpu": number,
                  "environment": [
                     {
                        "name": "string",
                        "value": "string"
                     }
                  ],
                  "environmentFiles": [
                     {
                        "type": "string",
                        "value": "string"
                     }
                  ],
                  "memory": number,
                  "memoryReservation": number,
                  "name": "string",
                  "resourceRequirements": [
                     {
                        "type": "string",
                        "value": "string"
                     }
                  ]
               }
            ],
            "cpu": "string",
            "ephemeralStorage": {
               "sizeInGiB": number
            },
            "executionRoleArn": "string",
            "inferenceAcceleratorOverrides": [
               {
                  "deviceName": "string",
                  "deviceType": "string"
               }
            ],
            "memory": "string",
            "taskRoleArn": "string"
         },
         "platformFamily": "string",
         "platformVersion": "string",
         "pullStartedAt": number,
         "pullStoppedAt": number,
         "startedAt": number,
         "startedBy": "string",
         "stopCode": "string",
         "stoppedAt": number,
         "stoppedReason": "string",
         "stoppingAt": number,
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "taskArn": "string",
         "taskDefinitionArn": "string",
         "version": number
      }
   ]
}
```

## Response Elements
<a name="API_RunTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_RunTask_ResponseSyntax) **   <a name="ECS-RunTask-response-failures"></a>
Any failures associated with the call.
For information about how to address failures, see [Service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages.html#service-event-messages-list) and [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: Array of [Failure](API_Failure.md) objects

 ** [tasks](#API_RunTask_ResponseSyntax) **   <a name="ECS-RunTask-response-tasks"></a>
A full description of the tasks that were run. The tasks that were successfully placed on your cluster are described here.
Type: Array of [Task](API_Task.md) objects

## Errors
<a name="API_RunTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** BlockedException **
Your AWS account was blocked. For more information, contact [AWS Support](http://aws.amazon.com/contact-us/).
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

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
 ** message **
 Message that describes the cause of the exception.
 ** resourceIds **
The existing task ARNs which are already associated with the `clientToken`.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** PlatformTaskDefinitionIncompatibilityException **
The specified platform version doesn't satisfy the required capabilities of the task definition.
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
<a name="API_RunTask_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_RunTask_Example_1"></a>

This example request runs the latest `ACTIVE` revision of the `hello_world` task definition family in the default cluster.

#### Sample Request
<a name="API_RunTask_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: AmazonEC2ContainerServiceV20141113.RunTask
X-Amz-Date: 20161121T215740Z
User-Agent: aws-cli/1.11.13 Python/2.7.12 Darwin/16.1.0 botocore/1.4.66
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "count": 1,
  "taskDefinition": "hello_world",
  "clientToken": "550e8400-e29b-41d4-a716-446655440000"
}
```

#### Sample Response
<a name="API_RunTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 21 Nov 2016 21:57:40 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 1025
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "failures": [],
  "tasks": [
    {
      "clusterArn": "arn:aws:ecs:us-east-1:012345678910:cluster/default",
      "containerInstanceArn": "arn:aws:ecs:us-east-1:012345678910:container-instance/default/4c543eed-f83f-47da-b1d8-3d23f1da4c64",
      "containers": [
        {
          "containerArn": "arn:aws:ecs:us-east-1:012345678910:container/default/e76594d4-27e1-4c74-98b5-46a6435eb769",
          "lastStatus": "PENDING",
          "name": "wordpress",
          "taskArn": "arn:aws:ecs:us-east-1:012345678910:task/default/fdf2c302-468c-4e55-b884-5331d816e7fb"
        },
        {
          "containerArn": "arn:aws:ecs:us-east-1:012345678910:container/b19106ea-4fa8-4f1d-9767-96922c82b070",
          "lastStatus": "PENDING",
          "name": "mysql",
          "taskArn": "arn:aws:ecs:us-east-1:012345678910:task/default/fdf2c302-468c-4e55-b884-5331d816e7fb"
        }
      ],
      "createdAt": 1479765460.842,
      "desiredStatus": "RUNNING",
      "lastStatus": "PENDING",
      "overrides": {
        "containerOverrides": [
          {
            "name": "wordpress"
          },
          {
            "name": "mysql"
          }
        ]
      },
      "taskArn": "arn:aws:ecs:us-east-1:012345678910:task/default/fdf2c302-468c-4e55-b884-5331d816e7fb",
      "taskDefinitionArn": "arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:6",
      "version": 1
    }
  ]
}
```

## See Also
<a name="API_RunTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/RunTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/RunTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/RunTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/RunTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/RunTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/RunTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/RunTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/RunTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/RunTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/RunTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

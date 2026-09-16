---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StartTask.html
---

# StartTask
<a name="API_StartTask"></a>

Starts a new task from the specified task definition on the specified container instance or instances.

**Note**
On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.

**Note**
Amazon Elastic Inference (EI) is no longer available to customers.

Alternatively, you can use`RunTask` to place tasks for you. For more information, see [Scheduling Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html) in the *Amazon Elastic Container Service Developer Guide*.

You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more information, see [Amazon EBS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types) in the *Amazon Elastic Container Service Developer Guide*.

## Request Syntax
<a name="API_StartTask_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "containerInstances": [ "{{string}}" ],
   "enableECSManagedTags": {{boolean}},
   "enableExecuteCommand": {{boolean}},
   "group": "{{string}}",
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
<a name="API_StartTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster where to start your task. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [containerInstances](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-containerInstances"></a>
The container instance IDs or full ARN entries for the container instances where you would like to place your task. You can specify up to 10 container instances.
Type: Array of strings
Required: Yes

 ** [enableECSManagedTags](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-enableECSManagedTags"></a>
Specifies whether to use Amazon ECS managed tags for the task. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: Boolean
Required: No

 ** [enableExecuteCommand](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-enableExecuteCommand"></a>
Whether or not the execute command functionality is turned on for the task. If `true`, this turns on the execute command functionality on all containers in the task.
Type: Boolean
Required: No

 ** [group](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-group"></a>
The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).
Type: String
Required: No

 ** [networkConfiguration](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-networkConfiguration"></a>
The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the `awsvpc` networking mode.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [overrides](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-overrides"></a>
A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it receives. You can override the default command for a container (that's specified in the task definition or Docker image) with a `command` override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an `environment` override.
A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.
Type: [TaskOverride](API_TaskOverride.md) object
Required: No

 ** [propagateTags](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-propagateTags"></a>
Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.
Type: String
Valid Values: `TASK_DEFINITION | SERVICE | NONE`
Required: No

 ** [referenceId](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-referenceId"></a>
This parameter is only used by Amazon ECS. It is not intended for use by customers.
Type: String
Required: No

 ** [startedBy](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-startedBy"></a>
An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the `startedBy` parameter. You can then identify which tasks belong to that job by filtering the results of a [ListTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html) call with the `startedBy` value. Up to 36 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (\_) are allowed.
If a task is started by an Amazon ECS service, the `startedBy` parameter contains the deployment ID of the service that starts it.
Type: String
Required: No

 ** [tags](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-tags"></a>
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

 ** [taskDefinition](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-taskDefinition"></a>
The `family` and `revision` (`family:revision`) or full ARN of the task definition to start. If a `revision` isn't specified, the latest `ACTIVE` revision is used.
Type: String
Required: Yes

 ** [volumeConfigurations](#API_StartTask_RequestSyntax) **   <a name="ECS-StartTask-request-volumeConfigurations"></a>
The details of the volume that was `configuredAtLaunch`. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in [TaskManagedEBSVolumeConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html). The `name` of the volume must match the `name` from the task definition.
Type: Array of [TaskVolumeConfiguration](API_TaskVolumeConfiguration.md) objects
Required: No

## Response Syntax
<a name="API_StartTask_ResponseSyntax"></a>

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
<a name="API_StartTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_StartTask_ResponseSyntax) **   <a name="ECS-StartTask-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

 ** [tasks](#API_StartTask_ResponseSyntax) **   <a name="ECS-StartTask-response-tasks"></a>
A full description of the tasks that were started. Each task that was successfully placed on your container instances is described.
Type: Array of [Task](API_Task.md) objects

## Errors
<a name="API_StartTask_Errors"></a>

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

 ** NamespaceNotFoundException **
The specified namespace wasn't found.
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
<a name="API_StartTask_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_StartTask_Example_1"></a>

This example request starts the latest `ACTIVE` revision of the `hello_world` task definition family in the default cluster on the container instance with the ID `4c543eed-f83f-47da-b1d8-3d23f1da4c64`.

#### Sample Request
<a name="API_StartTask_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 97
X-Amz-Target: AmazonEC2ContainerServiceV20141113.StartTask
X-Amz-Date: 20161121T220032Z
User-Agent: aws-cli/1.11.13 Python/2.7.12 Darwin/16.1.0 botocore/1.4.66
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "containerInstances": [
    "4c543eed-f83f-47da-b1d8-3d23f1da4c64"
  ],
  "taskDefinition": "hello_world"
}
```

#### Sample Response
<a name="API_StartTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 21 Nov 2016 22:00:32 GMT
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
          "containerArn": "arn:aws:ecs:us-east-1:012345678910:container/e76594d4-27e1-4c74-98b5-46a6435eb769",
          "lastStatus": "PENDING",
          "name": "wordpress",
          "taskArn": "arn:aws:ecs:us-east-1:012345678910:task/default/fdf2c302-468c-4e55-b884-5331d816e7fb"
        },
        {
          "containerArn": "arn:aws:ecs:us-east-1:012345678910:container/default/b19106ea-4fa8-4f1d-9767-96922c82b070",
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
<a name="API_StartTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/StartTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/StartTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/StartTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/StartTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/StartTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/StartTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/StartTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/StartTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/StartTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/StartTask)

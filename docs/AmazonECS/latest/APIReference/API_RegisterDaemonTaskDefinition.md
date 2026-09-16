---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterDaemonTaskDefinition.html
---

# RegisterDaemonTaskDefinition
<a name="API_RegisterDaemonTaskDefinition"></a>

Registers a new daemon task definition from the supplied `family` and `containerDefinitions`. Optionally, you can add data volumes to your containers with the `volumes` parameter. For more information, see [Daemon task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-task-definitions.html) in the *Amazon Elastic Container Service Developer Guide*.

A daemon task definition is a template that describes the containers that form a daemon. Daemons deploy cross-cutting software agents such as security monitoring, telemetry, and logging across your Amazon ECS infrastructure.

Each time you call `RegisterDaemonTaskDefinition`, a new revision of the daemon task definition is created. You can't modify a revision after you register it.

## Request Syntax
<a name="API_RegisterDaemonTaskDefinition_RequestSyntax"></a>

```
{
   "containerDefinitions": [
      {
         "command": [ "{{string}}" ],
         "cpu": {{number}},
         "dependsOn": [
            {
               "condition": "{{string}}",
               "containerName": "{{string}}"
            }
         ],
         "entryPoint": [ "{{string}}" ],
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
         "essential": {{boolean}},
         "firelensConfiguration": {
            "options": {
               "{{string}}" : "{{string}}"
            },
            "type": "{{string}}"
         },
         "healthCheck": {
            "command": [ "{{string}}" ],
            "interval": {{number}},
            "retries": {{number}},
            "startPeriod": {{number}},
            "timeout": {{number}}
         },
         "image": "{{string}}",
         "interactive": {{boolean}},
         "linuxParameters": {
            "capabilities": {
               "add": [ "{{string}}" ],
               "drop": [ "{{string}}" ]
            },
            "devices": [
               {
                  "containerPath": "{{string}}",
                  "hostPath": "{{string}}",
                  "permissions": [ "{{string}}" ]
               }
            ],
            "initProcessEnabled": {{boolean}},
            "tmpfs": [
               {
                  "containerPath": "{{string}}",
                  "mountOptions": [ "{{string}}" ],
                  "size": {{number}}
               }
            ]
         },
         "logConfiguration": {
            "logDriver": "{{string}}",
            "options": {
               "{{string}}" : "{{string}}"
            },
            "secretOptions": [
               {
                  "name": "{{string}}",
                  "valueFrom": "{{string}}"
               }
            ]
         },
         "memory": {{number}},
         "memoryReservation": {{number}},
         "mountPoints": [
            {
               "containerPath": "{{string}}",
               "readOnly": {{boolean}},
               "sourceVolume": "{{string}}"
            }
         ],
         "name": "{{string}}",
         "privileged": {{boolean}},
         "pseudoTerminal": {{boolean}},
         "readonlyRootFilesystem": {{boolean}},
         "repositoryCredentials": {
            "credentialsParameter": "{{string}}"
         },
         "restartPolicy": {
            "enabled": {{boolean}},
            "ignoredExitCodes": [ {{number}} ],
            "restartAttemptPeriod": {{number}}
         },
         "secrets": [
            {
               "name": "{{string}}",
               "valueFrom": "{{string}}"
            }
         ],
         "startTimeout": {{number}},
         "stopTimeout": {{number}},
         "systemControls": [
            {
               "namespace": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "ulimits": [
            {
               "hardLimit": {{number}},
               "name": "{{string}}",
               "softLimit": {{number}}
            }
         ],
         "user": "{{string}}",
         "workingDirectory": "{{string}}"
      }
   ],
   "cpu": "{{string}}",
   "executionRoleArn": "{{string}}",
   "family": "{{string}}",
   "ipcMode": "{{string}}",
   "memory": "{{string}}",
   "pidMode": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "taskRoleArn": "{{string}}",
   "volumes": [
      {
         "host": {
            "sourcePath": "{{string}}"
         },
         "name": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_RegisterDaemonTaskDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [containerDefinitions](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-containerDefinitions"></a>
A list of container definitions in JSON format that describe the containers that make up your daemon task.
Type: Array of [DaemonContainerDefinition](API_DaemonContainerDefinition.md) objects
Required: Yes

 ** [cpu](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-cpu"></a>
The number of CPU units used by the daemon task. It can be expressed as an integer using CPU units (for example, `1024`).
Type: String
Required: No

 ** [executionRoleArn](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. The task execution role is required for daemon tasks that pull container images from Amazon ECR or send container logs to CloudWatch.
Type: String
Required: No

 ** [family](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-family"></a>
You must specify a `family` for a daemon task definition. This family is used as a name for your daemon task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.
Type: String
Required: Yes

 ** [ipcMode](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-ipcMode"></a>
The IPC namespace mode for the daemon. The valid values are `none` and `shared`. The default is `none`.
If `none` is specified or no value is provided, the daemon runs with its own IPC namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host IPC namespace, making it accessible to non-daemon tasks that use `ipcMode: "host"` or other daemons that use `ipcMode: "shared"`.
Type: String
Valid Values: `none | shared`
Required: No

 ** [memory](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-memory"></a>
The amount of memory (in MiB) used by the daemon task. It can be expressed as an integer using MiB (for example, `1024`).
Type: String
Required: No

 ** [pidMode](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-pidMode"></a>
The PID namespace mode for the daemon. The valid values are `none` and `shared`. The default is `none`.
If `none` is specified or no value is provided, the daemon runs with its own PID namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host PID namespace, making it accessible to non-daemon tasks that use `pidMode: "host"` or other daemons that use `pidMode: "shared"`.
Type: String
Valid Values: `none | shared`
Required: No

 ** [tags](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-tags"></a>
The metadata that you apply to the daemon task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.
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

 ** [taskRoleArn](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-taskRoleArn"></a>
The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this daemon task can assume. All containers in this daemon task are granted the permissions that are specified in this role.
Type: String
Required: No

 ** [volumes](#API_RegisterDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-request-volumes"></a>
A list of volume definitions in JSON format that containers in your daemon task can use.
Type: Array of [DaemonVolume](API_DaemonVolume.md) objects
Required: No

## Response Syntax
<a name="API_RegisterDaemonTaskDefinition_ResponseSyntax"></a>

```
{
   "daemonTaskDefinitionArn": "string"
}
```

## Response Elements
<a name="API_RegisterDaemonTaskDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [daemonTaskDefinitionArn](#API_RegisterDaemonTaskDefinition_ResponseSyntax) **   <a name="ECS-RegisterDaemonTaskDefinition-response-daemonTaskDefinitionArn"></a>
The full Amazon Resource Name (ARN) of the registered daemon task definition.
Type: String

## Errors
<a name="API_RegisterDaemonTaskDefinition_Errors"></a>

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

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The limit for the resource was exceeded.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

## Examples
<a name="API_RegisterDaemonTaskDefinition_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_RegisterDaemonTaskDefinition_Example_1"></a>

This example registers a daemon task definition in the monitoring-agent family with a single container that runs a CloudWatch agent.

#### Sample Request
<a name="API_RegisterDaemonTaskDefinition_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerServiceV20141113.RegisterDaemonTaskDefinition
X-Amz-Date: 20250315T103000Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "family": "monitoring-agent",
  "containerDefinitions": [
    {
      "name": "cloudwatch-agent",
      "image": "public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest",
      "memory": 256,
      "cpu": 128,
      "essential": true,
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/daemon/monitoring-agent",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "environment": [
        {
          "name": "USE_DEFAULT_CONFIG",
          "value": "true"
        }
      ]
    }
  ],
  "cpu": "128",
  "memory": "256",
  "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
  "taskRoleArn": "arn:aws:iam::123456789012:role/ecsDaemonTaskRole"
}
```

#### Sample Response
<a name="API_RegisterDaemonTaskDefinition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 15 Mar 2025 10:30:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 97
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemonTaskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:1"
}
```

## See Also
<a name="API_RegisterDaemonTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/RegisterDaemonTaskDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/RegisterDaemonTaskDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/RegisterDaemonTaskDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/RegisterDaemonTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/RegisterDaemonTaskDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/RegisterDaemonTaskDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/RegisterDaemonTaskDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/RegisterDaemonTaskDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/RegisterDaemonTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/RegisterDaemonTaskDefinition)

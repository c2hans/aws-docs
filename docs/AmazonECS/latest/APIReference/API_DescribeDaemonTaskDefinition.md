---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemonTaskDefinition.html
---

# DescribeDaemonTaskDefinition
<a name="API_DescribeDaemonTaskDefinition"></a>

Describes a daemon task definition. You can specify a `family` and `revision` to find information about a specific daemon task definition, or you can simply specify the family to find the latest `ACTIVE` revision in that family.

## Request Syntax
<a name="API_DescribeDaemonTaskDefinition_RequestSyntax"></a>

```
{
   "daemonTaskDefinition": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDaemonTaskDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [daemonTaskDefinition](#API_DescribeDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-DescribeDaemonTaskDefinition-request-daemonTaskDefinition"></a>
The `family` for the latest `ACTIVE` revision, `family` and `revision` (`family:revision`) for a specific revision in the family, or full Amazon Resource Name (ARN) of the daemon task definition to describe.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeDaemonTaskDefinition_ResponseSyntax"></a>

```
{
   "daemonTaskDefinition": {
      "containerDefinitions": [
         {
            "command": [ "string" ],
            "cpu": number,
            "dependsOn": [
               {
                  "condition": "string",
                  "containerName": "string"
               }
            ],
            "entryPoint": [ "string" ],
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
            "essential": boolean,
            "firelensConfiguration": {
               "options": {
                  "string" : "string"
               },
               "type": "string"
            },
            "healthCheck": {
               "command": [ "string" ],
               "interval": number,
               "retries": number,
               "startPeriod": number,
               "timeout": number
            },
            "image": "string",
            "interactive": boolean,
            "linuxParameters": {
               "capabilities": {
                  "add": [ "string" ],
                  "drop": [ "string" ]
               },
               "devices": [
                  {
                     "containerPath": "string",
                     "hostPath": "string",
                     "permissions": [ "string" ]
                  }
               ],
               "initProcessEnabled": boolean,
               "tmpfs": [
                  {
                     "containerPath": "string",
                     "mountOptions": [ "string" ],
                     "size": number
                  }
               ]
            },
            "logConfiguration": {
               "logDriver": "string",
               "options": {
                  "string" : "string"
               },
               "secretOptions": [
                  {
                     "name": "string",
                     "valueFrom": "string"
                  }
               ]
            },
            "memory": number,
            "memoryReservation": number,
            "mountPoints": [
               {
                  "containerPath": "string",
                  "readOnly": boolean,
                  "sourceVolume": "string"
               }
            ],
            "name": "string",
            "privileged": boolean,
            "pseudoTerminal": boolean,
            "readonlyRootFilesystem": boolean,
            "repositoryCredentials": {
               "credentialsParameter": "string"
            },
            "restartPolicy": {
               "enabled": boolean,
               "ignoredExitCodes": [ number ],
               "restartAttemptPeriod": number
            },
            "secrets": [
               {
                  "name": "string",
                  "valueFrom": "string"
               }
            ],
            "startTimeout": number,
            "stopTimeout": number,
            "systemControls": [
               {
                  "namespace": "string",
                  "value": "string"
               }
            ],
            "ulimits": [
               {
                  "hardLimit": number,
                  "name": "string",
                  "softLimit": number
               }
            ],
            "user": "string",
            "workingDirectory": "string"
         }
      ],
      "cpu": "string",
      "daemonTaskDefinitionArn": "string",
      "deleteRequestedAt": number,
      "executionRoleArn": "string",
      "family": "string",
      "ipcMode": "string",
      "memory": "string",
      "pidMode": "string",
      "registeredAt": number,
      "registeredBy": "string",
      "revision": number,
      "status": "string",
      "taskRoleArn": "string",
      "volumes": [
         {
            "host": {
               "sourcePath": "string"
            },
            "name": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeDaemonTaskDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [daemonTaskDefinition](#API_DescribeDaemonTaskDefinition_ResponseSyntax) **   <a name="ECS-DescribeDaemonTaskDefinition-response-daemonTaskDefinition"></a>
The full daemon task definition description.
Type: [DaemonTaskDefinition](API_DaemonTaskDefinition.md) object

## Errors
<a name="API_DescribeDaemonTaskDefinition_Errors"></a>

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

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

## Examples
<a name="API_DescribeDaemonTaskDefinition_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DescribeDaemonTaskDefinition_Example_1"></a>

This example describes the first revision of the monitoring-agent daemon task definition.

#### Sample Request
<a name="API_DescribeDaemonTaskDefinition_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeDaemonTaskDefinition
X-Amz-Date: 20250315T103000Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "daemonTaskDefinition": "monitoring-agent:1"
}
```

#### Sample Response
<a name="API_DescribeDaemonTaskDefinition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 15 Mar 2025 10:30:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 679
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemonTaskDefinition": {
    "daemonTaskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:1",
    "family": "monitoring-agent",
    "revision": 1,
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
        ],
        "mountPoints": [],
        "secrets": []
      }
    ],
    "cpu": "128",
    "memory": "256",
    "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
    "taskRoleArn": "arn:aws:iam::123456789012:role/ecsDaemonTaskRole",
    "volumes": [],
    "status": "ACTIVE",
    "registeredAt": "2025-03-15T10:30:00.000Z",
    "registeredBy": "arn:aws:iam::123456789012:user/admin"
  }
}
```

## See Also
<a name="API_DescribeDaemonTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeDaemonTaskDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeDaemonTaskDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeDaemonTaskDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeDaemonTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeDaemonTaskDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeDaemonTaskDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeDaemonTaskDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeDaemonTaskDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeDaemonTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeDaemonTaskDefinition)

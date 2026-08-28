---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterTaskDefinition.html
---

# DeregisterTaskDefinition
<a name="API_DeregisterTaskDefinition"></a>

Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as `INACTIVE`. Existing tasks and services that reference an `INACTIVE` task definition continue to run without disruption. Existing services that reference an `INACTIVE` task definition can still scale up or down by modifying the service's desired count. If you want to delete a task definition revision, you must first deregister the task definition revision.

You can't use an `INACTIVE` task definition to run new tasks or create new services, and you can't update an existing service to reference an `INACTIVE` task definition. However, there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect.

**Note**
At this time, `INACTIVE` task definitions remain discoverable in your account indefinitely. However, this behavior is subject to change in the future. We don't recommend that you rely on `INACTIVE` task definitions persisting beyond the lifecycle of any associated tasks and services.

You must deregister a task definition revision before you delete it. For more information, see [DeleteTaskDefinitions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteTaskDefinitions.html).

## Request Syntax
<a name="API_DeregisterTaskDefinition_RequestSyntax"></a>

```
{
   "taskDefinition": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterTaskDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [taskDefinition](#API_DeregisterTaskDefinition_RequestSyntax) **   <a name="ECS-DeregisterTaskDefinition-request-taskDefinition"></a>
The `family` and `revision` (`family:revision`) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a `revision`.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeregisterTaskDefinition_ResponseSyntax"></a>

```
{
   "taskDefinition": {
      "compatibilities": [ "string" ],
      "containerDefinitions": [
         {
            "command": [ "string" ],
            "cpu": number,
            "credentialSpecs": [ "string" ],
            "dependsOn": [
               {
                  "condition": "string",
                  "containerName": "string"
               }
            ],
            "disableNetworking": boolean,
            "dnsSearchDomains": [ "string" ],
            "dnsServers": [ "string" ],
            "dockerLabels": {
               "string" : "string"
            },
            "dockerSecurityOptions": [ "string" ],
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
            "extraHosts": [
               {
                  "hostname": "string",
                  "ipAddress": "string"
               }
            ],
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
            "hostname": "string",
            "image": "string",
            "interactive": boolean,
            "links": [ "string" ],
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
               "maxSwap": number,
               "sharedMemorySize": number,
               "swappiness": number,
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
            "portMappings": [
               {
                  "appProtocol": "string",
                  "containerPort": number,
                  "containerPortRange": "string",
                  "hostPort": number,
                  "name": "string",
                  "protocol": "string"
               }
            ],
            "privileged": boolean,
            "pseudoTerminal": boolean,
            "readonlyRootFilesystem": boolean,
            "repositoryCredentials": {
               "credentialsParameter": "string"
            },
            "resourceRequirements": [
               {
                  "type": "string",
                  "value": "string"
               }
            ],
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
            "versionConsistency": "string",
            "volumesFrom": [
               {
                  "readOnly": boolean,
                  "sourceContainer": "string"
               }
            ],
            "workingDirectory": "string"
         }
      ],
      "cpu": "string",
      "deleteRequestedAt": number,
      "deregisteredAt": number,
      "enableFaultInjection": boolean,
      "ephemeralStorage": {
         "sizeInGiB": number
      },
      "executionRoleArn": "string",
      "family": "string",
      "inferenceAccelerators": [
         {
            "deviceName": "string",
            "deviceType": "string"
         }
      ],
      "ipcMode": "string",
      "memory": "string",
      "networkMode": "string",
      "pidMode": "string",
      "placementConstraints": [
         {
            "expression": "string",
            "type": "string"
         }
      ],
      "proxyConfiguration": {
         "containerName": "string",
         "properties": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "type": "string"
      },
      "registeredAt": number,
      "registeredBy": "string",
      "requiresAttributes": [
         {
            "name": "string",
            "targetId": "string",
            "targetType": "string",
            "value": "string"
         }
      ],
      "requiresCompatibilities": [ "string" ],
      "revision": number,
      "runtimePlatform": {
         "cpuArchitecture": "string",
         "operatingSystemFamily": "string"
      },
      "status": "string",
      "taskDefinitionArn": "string",
      "taskRoleArn": "string",
      "volumes": [
         {
            "configuredAtLaunch": boolean,
            "dockerVolumeConfiguration": {
               "autoprovision": boolean,
               "driver": "string",
               "driverOpts": {
                  "string" : "string"
               },
               "labels": {
                  "string" : "string"
               },
               "scope": "string"
            },
            "efsVolumeConfiguration": {
               "authorizationConfig": {
                  "accessPointId": "string",
                  "iam": "string"
               },
               "fileSystemId": "string",
               "rootDirectory": "string",
               "transitEncryption": "string",
               "transitEncryptionPort": number
            },
            "fsxWindowsFileServerVolumeConfiguration": {
               "authorizationConfig": {
                  "credentialsParameter": "string",
                  "domain": "string"
               },
               "fileSystemId": "string",
               "rootDirectory": "string"
            },
            "host": {
               "sourcePath": "string"
            },
            "name": "string",
            "s3filesVolumeConfiguration": {
               "accessPointArn": "string",
               "fileSystemArn": "string",
               "rootDirectory": "string",
               "transitEncryptionPort": number
            }
         }
      ]
   }
}
```

## Response Elements
<a name="API_DeregisterTaskDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskDefinition](#API_DeregisterTaskDefinition_ResponseSyntax) **   <a name="ECS-DeregisterTaskDefinition-response-taskDefinition"></a>
The full description of the deregistered task.
Type: [TaskDefinition](API_TaskDefinition.md) object

## Errors
<a name="API_DeregisterTaskDefinition_Errors"></a>

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
<a name="API_DeregisterTaskDefinition_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DeregisterTaskDefinition_Example_1"></a>

The following example request deregisters the first revision of the `cpu-wave` task definition family (`cpu-wave:1`). In the resulting output, the task definition status becomes `INACTIVE`.

#### Sample Request
<a name="API_DeregisterTaskDefinition_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 35
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DeregisterTaskDefinition
X-Amz-Date: 20150429T184806Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "taskDefinition": "cpu-wave:1"
}
```

#### Sample Response
<a name="API_DeregisterTaskDefinition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 12 Jun 2015 23:07:39 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 491
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "taskDefinition": {
    "containerDefinitions": [
      {
        "command": [
          "apt-get update; apt-get install stress; while true; do stress --cpu $(( RANDOM % 4 )) -t $(( RANDOM % 10 )); done"
        ],
        "cpu": 50,
        "entryPoint": [
          "bash",
          "-c"
        ],
        "environment": [],
        "essential": true,
        "image": "public.ecr.aws/docker/library/ubuntu:latest",
        "memory": 100,
        "mountPoints": [],
        "name": "wave",
        "portMappings": [],
        "volumesFrom": []
      }
    ],
    "family": "cpu-wave",
    "revision": 1,
    "status": "INACTIVE",
    "taskDefinitionArn": "arn:aws:ecs:us-west-2:012345678910:task-definition/cpu-wave:1",
    "volumes": []
  }
}
```

## See Also
<a name="API_DeregisterTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DeregisterTaskDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DeregisterTaskDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeregisterTaskDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DeregisterTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeregisterTaskDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DeregisterTaskDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DeregisterTaskDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DeregisterTaskDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeregisterTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeregisterTaskDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskDefinition.html
---

# DescribeTaskDefinition
<a name="API_DescribeTaskDefinition"></a>

Describes a task definition. You can specify a `family` and `revision` to find information about a specific task definition, or you can simply specify the family to find the latest `ACTIVE` revision in that family.

**Note**
You can only describe `INACTIVE` task definitions while an active task or service references them.

## Request Syntax
<a name="API_DescribeTaskDefinition_RequestSyntax"></a>

```
{
   "include": [ "{{string}}" ],
   "taskDefinition": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTaskDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [include](#API_DescribeTaskDefinition_RequestSyntax) **   <a name="ECS-DescribeTaskDefinition-request-include"></a>
Determines whether to see the resource tags for the task definition. If `TAGS` is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.
Type: Array of strings
Valid Values: `TAGS`
Required: No

 ** [taskDefinition](#API_DescribeTaskDefinition_RequestSyntax) **   <a name="ECS-DescribeTaskDefinition-request-taskDefinition"></a>
The `family` for the latest `ACTIVE` revision, `family` and `revision` (`family:revision`) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeTaskDefinition_ResponseSyntax"></a>

```
{
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ],
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
<a name="API_DescribeTaskDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_DescribeTaskDefinition_ResponseSyntax) **   <a name="ECS-DescribeTaskDefinition-response-tags"></a>
The metadata that's applied to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.
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

 ** [taskDefinition](#API_DescribeTaskDefinition_ResponseSyntax) **   <a name="ECS-DescribeTaskDefinition-response-taskDefinition"></a>
The full task definition description.
Type: [TaskDefinition](API_TaskDefinition.md) object

## Errors
<a name="API_DescribeTaskDefinition_Errors"></a>

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
<a name="API_DescribeTaskDefinition_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DescribeTaskDefinition_Example_1"></a>

This example request provides descriptive information about the 10th revision of a task definition in the `hello_world` family.

#### Sample Request
<a name="API_DescribeTaskDefinition_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 36
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeTaskDefinition
X-Amz-Date: 20150429T190902Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "taskDefinition": "hello_world:10"
}
```

#### Sample Response
<a name="API_DescribeTaskDefinition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 19:09:03 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 574
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "taskDefinition": {
    "containerDefinitions": [
      {
        "cpu": 10,
        "environment": [],
        "essential": true,
        "image": "public.ecr.aws/docker/library/wordpress:latest",
        "links": [
          "mysql"
        ],
        "memory": 500,
        "mountPoints": [],
        "name": "wordpress",
        "portMappings": [
          {
            "containerPort": 80,
            "hostPort": 80
          }
        ],
        "volumesFrom": []
      },
      {
        "cpu": 10,
        "environment": [
          {
            "name": "MYSQL_ROOT_PASSWORD",
            "value": "password"
          }
        ],
        "essential": true,
        "image": "public.ecr.aws/docker/library/mysql:latest",
        "memory": 500,
        "mountPoints": [],
        "name": "mysql",
        "portMappings": [],
        "volumesFrom": []
      }
    ],
    "family": "hello_world",
    "revision": 10,
    "taskDefinitionArn": "arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:10",
    "volumes": []
  }
}
```

## See Also
<a name="API_DescribeTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeTaskDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeTaskDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeTaskDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeTaskDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeTaskDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeTaskDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeTaskDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeTaskDefinition)

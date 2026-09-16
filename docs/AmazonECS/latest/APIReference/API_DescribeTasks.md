---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html
---

# DescribeTasks
<a name="API_DescribeTasks"></a>

Describes a specified task or tasks.

Currently, stopped tasks appear in the returned results for at least one hour.

If you have tasks with tags, and then delete the cluster, the tagged tasks are returned in the response. If you create a new cluster with the same name as the deleted cluster, the tagged tasks are not included in the response.

## Request Syntax
<a name="API_DescribeTasks_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "include": [ "{{string}}" ],
   "tasks": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_DescribeTasks_RequestSyntax) **   <a name="ECS-DescribeTasks-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task or tasks to describe. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [include](#API_DescribeTasks_RequestSyntax) **   <a name="ECS-DescribeTasks-request-include"></a>
Specifies whether you want to see the resource tags for the task. If `TAGS` is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.
Type: Array of strings
Valid Values: `TAGS`
Required: No

 ** [tasks](#API_DescribeTasks_RequestSyntax) **   <a name="ECS-DescribeTasks-request-tasks"></a>
A list of up to 100 task IDs or full ARN entries.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_DescribeTasks_ResponseSyntax"></a>

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
<a name="API_DescribeTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_DescribeTasks_ResponseSyntax) **   <a name="ECS-DescribeTasks-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

 ** [tasks](#API_DescribeTasks_ResponseSyntax) **   <a name="ECS-DescribeTasks-response-tasks"></a>
The list of tasks.
Type: Array of [Task](API_Task.md) objects

## Errors
<a name="API_DescribeTasks_Errors"></a>

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

## Examples
<a name="API_DescribeTasks_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DescribeTasks_Example_1"></a>

This example request provides descriptive information about a task with an ARN of `arn:aws:ecs:us-east-1:123456789012:cluster/default` in the `default` cluster.

#### Sample Request
<a name="API_DescribeTasks_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 51
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeTasks
X-Amz-Date: 20250212T181908Z
User-Agent: aws-cli/2.2.26 Python/2.7.12 Darwin/16.1.0 botocore/1.4.66
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "tasks": [
    "arn:aws:ecs:us-east-1:1234567890:cluster/default"
  ]
}
```

#### Sample Response
<a name="API_DescribeTasks_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 21 Nov 2016 21:49:16 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 1238
Connection: keep-alive

x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
    "tasks": [
        {
            "attachments": [
                {
                    "id": "39888c47-dd47-482b-b6b5-1ea60b6633e7",
                    "type": "ElasticNetworkInterface",
                    "status": "ATTACHED",
                    "details": [
                        {
                            "name": "subnetId",
                            "value": "subnet-0db5010045995c2d5"
                        },
                        {
                            "name": "networkInterfaceId",
                            "value": "eni-0800851957d7918fa"
                        },
                        {
                            "name": "macAddress",
                            "value": "0a:ff:cc:73:2e:b7"
                        },
                        {
                            "name": "privateDnsName",
                            "value": "ip-10-0-0-250.ec2.internal"
                        },
                        {
                            "name": "privateIPv4Address",
                            "value": "10.0.0.250"
                        }
                    ]
                }
            ],
            "attributes": [
                {
                    "name": "ecs.cpu-architecture",
                    "value": "x86_64"
                }
            ],
            "availabilityZone": "us-east-1a",
            "capacityProviderName": "FARGATE",
            "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/default",
            "connectivity": "CONNECTED",
            "connectivityAt": "2025-02-03T16:01:58.863000-05:00",
            "containers": [
                {
                    "containerArn": "arn:aws:ecs:us-east-1:123456789012:container/default/154bdb1df5b446b280fe900d12c452a1/417f6954-30e9-4e60-84e5-bad3743617ab",
                    "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/default/154bdb1df5b446b280fe900d12c452a1",
                    "name": "aws-otel-collector",
                    "image": "public.ecr.aws/aws-observability/aws-otel-collector:v0.32.0",
                    "imageDigest": "sha256:7a1b3560655071bcacd66902c20ebe9a69470d5691fe3bd36baace7c2f3c4640",
                    "runtimeId": "154bdb1df5b446b280fe900d12c452a1-4027662657",
                    "lastStatus": "RUNNING",
                    "networkBindings": [],
                    "networkInterfaces": [
                        {
                            "attachmentId": "39888c47-dd47-482b-b6b5-1ea60b6633e7",
                            "privateIpv4Address": "10.0.0.250"
                        }
                    ],
                    "healthStatus": "UNKNOWN",
                    "cpu": "0"
                },
                {
                    "containerArn": "arn:aws:ecs:us-east-1:123456789012:container/default/154bdb1df5b446b280fe900d12c452a1/52c6b197-710b-4860-9d52-262a56550b6a",
                    "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/default/154bdb1df5b446b280fe900d12c452a1",
                    "name": "web",
                    "image": "nginx",
                    "imageDigest": "sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206a",
                    "runtimeId": "154bdb1df5b446b280fe900d12c452a1-0265927825",
                    "lastStatus": "RUNNING",
                    "networkBindings": [],
                    "networkInterfaces": [
                        {
                            "attachmentId": "39888c47-dd47-482b-b6b5-1ea60b6633e7",
                            "privateIpv4Address": "10.0.0.250"
                        }
                    ],
                    "healthStatus": "HEALTHY",
                    "cpu": "99",
                    "memory": "100"
                }
            ],
            "cpu": "256",
            "createdAt": "2025-02-03T16:01:55.201000-05:00",
            "desiredStatus": "RUNNING",
            "enableExecuteCommand": false,
            "group": "family:webserver",
            "healthStatus": "HEALTHY",
            "lastStatus": "RUNNING",
            "launchType": "FARGATE",
            "memory": "512",
            "overrides": {
                "containerOverrides": [
                    {
                        "name": "aws-otel-collector"
                    },
                    {
                        "name": "web"
                    }
                ],
                "inferenceAcceleratorOverrides": []
            },
            "platformVersion": "1.4.0",
            "platformFamily": "Linux",
            "pullStartedAt": "2025-02-03T16:02:10.727000-05:00",
            "pullStoppedAt": "2025-02-03T16:02:17.868000-05:00",
            "startedAt": "2025-02-03T16:02:17.978000-05:00",
            "tags": [],
            "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/default/154bdb1df5b446b280fe900d12c452a1",
            "taskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:task-definition/webserver:5",
            "version": 4,
            "ephemeralStorage": {
                "sizeInGiB": 20
            },
            "fargateEphemeralStorage": {
                "sizeInGiB": 20
            }
        }
    ],
    "failures": []
}
```

## See Also
<a name="API_DescribeTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeTasks)

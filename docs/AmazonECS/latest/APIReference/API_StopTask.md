---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StopTask.html
---

# StopTask
<a name="API_StopTask"></a>

Stops a running task. Any tags associated with the task will be deleted.

When you call `StopTask` on a task, the equivalent of `docker stop` is issued to the containers running in the task. This results in a stop signal value and a default 30-second timeout, after which the `SIGKILL` value is sent and the containers are forcibly stopped. This signal can be defined in your container image with the `STOPSIGNAL` instruction and will default to `SIGTERM`. If the container handles the `SIGTERM` value gracefully and exits within 30 seconds from receiving it, no `SIGKILL` value is sent.

For Windows containers, POSIX signals do not work and runtime stops the container by sending a `CTRL_SHUTDOWN_EVENT`. For more information, see [Unable to react to graceful shutdown of (Windows) container \#25982](https://github.com/moby/moby/issues/25982) on GitHub.

**Note**
The default 30-second timeout can be configured on the Amazon ECS container agent with the `ECS_CONTAINER_STOP_TIMEOUT` variable. For more information, see [Amazon ECS Container Agent Configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide*.

## Request Syntax
<a name="API_StopTask_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "reason": "{{string}}",
   "task": "{{string}}"
}
```

## Request Parameters
<a name="API_StopTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_StopTask_RequestSyntax) **   <a name="ECS-StopTask-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [reason](#API_StopTask_RequestSyntax) **   <a name="ECS-StopTask-request-reason"></a>
An optional message specified when a task is stopped. For example, if you're using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent [DescribeTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html)> API operations on this task.
Type: String
Required: No

 ** [task](#API_StopTask_RequestSyntax) **   <a name="ECS-StopTask-request-task"></a>
Thefull Amazon Resource Name (ARN) of the task.
Type: String
Required: Yes

## Response Syntax
<a name="API_StopTask_ResponseSyntax"></a>

```
{
   "task": {
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
}
```

## Response Elements
<a name="API_StopTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [task](#API_StopTask_ResponseSyntax) **   <a name="ECS-StopTask-response-task"></a>
The task that was stopped.
Type: [Task](API_Task.md) object

## Errors
<a name="API_StopTask_Errors"></a>

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
<a name="API_StopTask_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_StopTask_Example_1"></a>

This example request stops a task with the ID `1dc5c17a-422b-4dc4-b493-371970c6c4d6` in the default cluster.

#### Sample Request
<a name="API_StopTask_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 88
X-Amz-Target: AmazonEC2ContainerServiceV20141113.StopTask
X-Amz-Date: 20250203T220318Z
User-Agent: aws-cli/2.2.26 Python/3.12.6 Darwin/16.1.0 botocore/1.4.66
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "task": "arn:aws:ecs:us-east-1:123456789012:task/MyCluster/36ad4ef947bb470b89010d864574237e"
}
```

#### Sample Response
<a name="API_StopTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 03 Feb 2025 22:03:18 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 1260
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
    "task": {
        "attachments": [
            {
                "id": "9711cfc0-8c7d-470b-93e4-9d2041731db6",
                "type": "ElasticNetworkInterface",
                "status": "ATTACHED",
                "details": [
                    {
                        "name": "subnetId",
                        "value": "subnet-0d0eab1bb38d5ca64"
                    },
                    {
                        "name": "networkInterfaceId",
                        "value": "eni-0f6b537b3ec7ba800"
                    },
                    {
                        "name": "macAddress",
                        "value": "0e:fd:16:ec:9a:01"
                    },
                    {
                        "name": "privateDnsName",
                        "value": "ip-10-0-1-114.ec2.internal"
                    },
                    {
                        "name": "privateIPv4Address",
                        "value": "10.0.1.114"
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
        "availabilityZone": "us-east-1b",
        "capacityProviderName": "FARGATE",
        "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/MyCluster",
        "connectivity": "CONNECTED",
        "connectivityAt": "2025-02-03T15:26:37.435000-05:00",
        "containers": [
            {
                "containerArn": "arn:aws:ecs:us-east-1:123456789012:container/MyCluster/36ad4ef947bb470b89010d864574237e/0a7d1107-a0c8-45c4-ac05-f0aaab4c63db",
                "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/MyCluster/36ad4ef947bb470b89010d864574237e",
                "name": "web",
                "image": "nginx",
                "imageDigest": "sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206a",
                "runtimeId": "36ad4ef947bb470b89010d864574237e-0265927825",
                "lastStatus": "RUNNING",
                "networkBindings": [],
                "networkInterfaces": [
                    {
                        "attachmentId": "9711cfc0-8c7d-470b-93e4-9d2041731db6",
                        "privateIpv4Address": "10.0.1.114"
                    }
                ],
                "cpu": "99",
                "memory": "100"
            },
            {
                "containerArn": "arn:aws:ecs:us-east-1:123456789012:container/MyCluster/36ad4ef947bb470b89010d864574237e/48dfdefe-b605-4747-b071-5f6bc8650b2d",
                "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/MyCluster/36ad4ef947bb470b89010d864574237e",
                "name": "aws-otel-collector",
                "image": "public.ecr.aws/aws-observability/aws-otel-collector:v0.32.0",
                "imageDigest": "sha256:7a1b3560655071bcacd66902c20ebe9a69470d5691fe3bd36baace7c2f3c4640",
                "runtimeId": "36ad4ef947bb470b89010d864574237e-4027662657",
                "lastStatus": "RUNNING",
                "networkBindings": [],
                "networkInterfaces": [
                    {
                        "attachmentId": "9711cfc0-8c7d-470b-93e4-9d2041731db6",
                        "privateIpv4Address": "10.0.1.114"
                    }
                ],
                "cpu": "0"
            }
        ],
        "cpu": "256",
        "createdAt": "2025-02-03T15:26:33.277000-05:00",
        "desiredStatus": "STOPPED",
        "enableExecuteCommand": false,
        "group": "family:webserver",
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
        "pullStartedAt": "2025-02-03T15:26:44.970000-05:00",
        "pullStoppedAt": "2025-02-03T15:26:51.926000-05:00",
        "startedAt": "2025-02-03T15:26:53.096000-05:00",
        "stopCode": "UserInitiated",
        "stoppedReason": "Task stopped by user",
        "stoppingAt": "2025-02-03T15:27:51.392000-05:00",
        "tags": [],
        "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/MyCluster/36ad4ef947bb470b89010d864574237e",
        "taskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:task-definition/webserver:5",
        "version": 4,
        "ephemeralStorage": {
            "sizeInGiB": 20
        },
        "fargateEphemeralStorage": {
            "sizeInGiB": 20
        }
    }
}
```

## See Also
<a name="API_StopTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/StopTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/StopTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/StopTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/StopTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/StopTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/StopTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/StopTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/StopTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/StopTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/StopTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

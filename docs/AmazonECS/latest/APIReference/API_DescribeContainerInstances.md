---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeContainerInstances.html
---

# DescribeContainerInstances
<a name="API_DescribeContainerInstances"></a>

Describes one or more container instances. Returns metadata about each container instance requested.

## Request Syntax
<a name="API_DescribeContainerInstances_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "containerInstances": [ "{{string}}" ],
   "include": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeContainerInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_DescribeContainerInstances_RequestSyntax) **   <a name="ECS-DescribeContainerInstances-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the container instance or container instances you are describing were launched in any cluster other than the default cluster.
Type: String
Required: No

 ** [containerInstances](#API_DescribeContainerInstances_RequestSyntax) **   <a name="ECS-DescribeContainerInstances-request-containerInstances"></a>
A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.
Type: Array of strings
Required: Yes

 ** [include](#API_DescribeContainerInstances_RequestSyntax) **   <a name="ECS-DescribeContainerInstances-request-include"></a>
Specifies whether you want to see the resource tags for the container instance. If `TAGS` is specified, the tags are included in the response. If `CONTAINER_INSTANCE_HEALTH` is specified, the container instance health is included in the response. If this field is omitted, tags and container instance health status aren't included in the response.
Type: Array of strings
Valid Values: `TAGS | CONTAINER_INSTANCE_HEALTH`
Required: No

## Response Syntax
<a name="API_DescribeContainerInstances_ResponseSyntax"></a>

```
{
   "containerInstances": [
      {
         "agentConnected": boolean,
         "agentUpdateStatus": "string",
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
         "capacityProviderName": "string",
         "containerInstanceArn": "string",
         "ec2InstanceId": "string",
         "healthStatus": {
            "details": [
               {
                  "lastStatusChange": number,
                  "lastUpdated": number,
                  "status": "string",
                  "statusReason": "string",
                  "type": "string"
               }
            ],
            "overallStatus": "string"
         },
         "pendingTasksCount": number,
         "registeredAt": number,
         "registeredResources": [
            {
               "doubleValue": number,
               "integerValue": number,
               "longValue": number,
               "name": "string",
               "stringSetValue": [ "string" ],
               "type": "string"
            }
         ],
         "remainingResources": [
            {
               "doubleValue": number,
               "integerValue": number,
               "longValue": number,
               "name": "string",
               "stringSetValue": [ "string" ],
               "type": "string"
            }
         ],
         "runningTasksCount": number,
         "status": "string",
         "statusReason": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "version": number,
         "versionInfo": {
            "agentHash": "string",
            "agentVersion": "string",
            "dockerVersion": "string"
         }
      }
   ],
   "failures": [
      {
         "arn": "string",
         "detail": "string",
         "reason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeContainerInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [containerInstances](#API_DescribeContainerInstances_ResponseSyntax) **   <a name="ECS-DescribeContainerInstances-response-containerInstances"></a>
The list of container instances.
Type: Array of [ContainerInstance](API_ContainerInstance.md) objects

 ** [failures](#API_DescribeContainerInstances_ResponseSyntax) **   <a name="ECS-DescribeContainerInstances-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

## Errors
<a name="API_DescribeContainerInstances_Errors"></a>

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
<a name="API_DescribeContainerInstances_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DescribeContainerInstances_Example_1"></a>

This example request provides descriptive information about a container instance with an ID of `f9cc75bb-0c94-46b9-bf6d-49d320bc1551` in the `default` cluster.

#### Sample Request
<a name="API_DescribeContainerInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 64
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeContainerInstances
X-Amz-Date: 20160520T171518Z
User-Agent: aws-cli/1.10.30 Python/2.7.11 Darwin/15.4.0 botocore/1.4.17
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "containerInstances": [
        "f9cc75bb-0c94-46b9-bf6d-49d320bc1551"
    ]
}
```

#### Sample Response
<a name="API_DescribeContainerInstances_Example_1_Response"></a>

```
{
    "containerInstances": [
        {
            "agentConnected": true,
            "attributes": [
                {
                    "name": "com.amazonaws.ecs.capability.privileged-container"
                },
                {
                    "name": "com.amazonaws.ecs.capability.docker-remote-api.1.17"
                },
                {
                    "name": "com.amazonaws.ecs.capability.docker-remote-api.1.18"
                },
                {
                    "name": "com.amazonaws.ecs.capability.docker-remote-api.1.19"
                },
                {
                    "name": "com.amazonaws.ecs.capability.docker-remote-api.1.20"
                },
                {
                    "name": "com.amazonaws.ecs.capability.docker-remote-api.1.21"
                },
                {
                    "name": "com.amazonaws.ecs.capability.logging-driver.json-file"
                },
                {
                    "name": "com.amazonaws.ecs.capability.logging-driver.syslog"
                },
                {
                    "name": "com.amazonaws.ecs.capability.logging-driver.awslogs"
                },
                {
                    "name": "com.amazonaws.ecs.capability.ecr-auth"
                }
            ],
            "containerInstanceArn": "arn:aws:ecs:us-west-2:012345678910:container-instance/default/f9cc75bb-0c94-46b9-bf6d-49d320bc1551",
            "ec2InstanceId": "i-042f39dc",
            "pendingTasksCount": 0,
            "registeredResources": [
                {
                    "doubleValue": 0,
                    "integerValue": 1024,
                    "longValue": 0,
                    "name": "CPU",
                    "type": "INTEGER"
                },
                {
                    "doubleValue": 0,
                    "integerValue": 995,
                    "longValue": 0,
                    "name": "MEMORY",
                    "type": "INTEGER"
                },
                {
                    "doubleValue": 0,
                    "integerValue": 0,
                    "longValue": 0,
                    "name": "PORTS",
                    "stringSetValue": [
                        "22",
                        "2376",
                        "2375",
                        "51678"
                    ],
                    "type": "STRINGSET"
                },
                {
                    "doubleValue": 0,
                    "integerValue": 0,
                    "longValue": 0,
                    "name": "PORTS_UDP",
                    "stringSetValue": [],
                    "type": "STRINGSET"
                }
            ],
            "remainingResources": [
                {
                    "doubleValue": 0,
                    "integerValue": 1024,
                    "longValue": 0,
                    "name": "CPU",
                    "type": "INTEGER"
                },
                {
                    "doubleValue": 0,
                    "integerValue": 995,
                    "longValue": 0,
                    "name": "MEMORY",
                    "type": "INTEGER"
                },
                {
                    "doubleValue": 0,
                    "integerValue": 0,
                    "longValue": 0,
                    "name": "PORTS",
                    "stringSetValue": [
                        "22",
                        "2376",
                        "2375",
                        "51678"
                    ],
                    "type": "STRINGSET"
                },
                {
                    "doubleValue": 0,
                    "integerValue": 0,
                    "longValue": 0,
                    "name": "PORTS_UDP",
                    "stringSetValue": [],
                    "type": "STRINGSET"
                }
            ],
            "runningTasksCount": 0,
            "status": "ACTIVE",
            "version": 850,
            "versionInfo": {
                "agentHash": "0931217",
                "agentVersion": "1.9.0",
                "dockerVersion": "DockerVersion: 1.9.1"
            }
        }
    ],
    "failures": []
}
```

## See Also
<a name="API_DescribeContainerInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeContainerInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeContainerInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeContainerInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeContainerInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeContainerInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeContainerInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeContainerInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeContainerInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeContainerInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeContainerInstances)

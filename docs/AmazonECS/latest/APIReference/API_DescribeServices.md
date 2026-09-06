---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html
---

# DescribeServices
<a name="API_DescribeServices"></a>

Describes the specified services running in your cluster.

## Request Syntax
<a name="API_DescribeServices_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "include": [ "{{string}}" ],
   "services": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeServices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_DescribeServices_RequestSyntax) **   <a name="ECS-DescribeServices-request-cluster"></a>
The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the service or services you are describing were launched in any cluster other than the default cluster.
Type: String
Required: No

 ** [include](#API_DescribeServices_RequestSyntax) **   <a name="ECS-DescribeServices-request-include"></a>
Determines whether you want to see the resource tags for the service. If `TAGS` is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.
Type: Array of strings
Valid Values: `TAGS`
Required: No

 ** [services](#API_DescribeServices_RequestSyntax) **   <a name="ECS-DescribeServices-request-services"></a>
A list of services to describe. You may specify up to 10 services to describe in a single operation.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_DescribeServices_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "arn": "string",
         "detail": "string",
         "reason": "string"
      }
   ],
   "services": [
      {
         "availabilityZoneRebalancing": "string",
         "capacityProviderStrategy": [
            {
               "base": number,
               "capacityProvider": "string",
               "weight": number
            }
         ],
         "clusterArn": "string",
         "createdAt": number,
         "createdBy": "string",
         "currentServiceDeployment": "string",
         "currentServiceRevisions": [
            {
               "arn": "string",
               "pendingTaskCount": number,
               "requestedTaskCount": number,
               "runningTaskCount": number
            }
         ],
         "deploymentConfiguration": {
            "alarms": {
               "alarmNames": [ "string" ],
               "enable": boolean,
               "rollback": boolean
            },
            "bakeTimeInMinutes": number,
            "canaryConfiguration": {
               "canaryBakeTimeInMinutes": number,
               "canaryPercent": number
            },
            "deploymentCircuitBreaker": {
               "enable": boolean,
               "resetOnHealthyTask": boolean,
               "rollback": boolean,
               "thresholdConfiguration": {
                  "type": "string",
                  "value": number
               }
            },
            "earlySuccessCriteria": {
               "enable": boolean,
               "healthyPercent": number,
               "sourceServiceRevisionCleanup": "string"
            },
            "lifecycleHooks": [
               {
                  "hookDetails": JSON value,
                  "hookTargetArn": "string",
                  "lifecycleStages": [ "string" ],
                  "roleArn": "string",
                  "targetType": "string",
                  "timeoutConfiguration": {
                     "action": "string",
                     "timeoutInMinutes": number
                  }
               }
            ],
            "linearConfiguration": {
               "stepBakeTimeInMinutes": number,
               "stepPercent": number
            },
            "maximumPercent": number,
            "minimumHealthyPercent": number,
            "strategy": "string"
         },
         "deploymentController": {
            "type": "string"
         },
         "deployments": [
            {
               "capacityProviderStrategy": [
                  {
                     "base": number,
                     "capacityProvider": "string",
                     "weight": number
                  }
               ],
               "createdAt": number,
               "desiredCount": number,
               "failedTasks": number,
               "fargateEphemeralStorage": {
                  "kmsKeyId": "string"
               },
               "id": "string",
               "launchType": "string",
               "networkConfiguration": {
                  "awsvpcConfiguration": {
                     "assignPublicIp": "string",
                     "securityGroups": [ "string" ],
                     "subnets": [ "string" ]
                  }
               },
               "pendingCount": number,
               "platformFamily": "string",
               "platformVersion": "string",
               "rolloutState": "string",
               "rolloutStateReason": "string",
               "runningCount": number,
               "serviceConnectConfiguration": {
                  "accessLogConfiguration": {
                     "format": "string",
                     "includeQueryParameters": "string"
                  },
                  "enabled": boolean,
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
                  "namespace": "string",
                  "services": [
                     {
                        "clientAliases": [
                           {
                              "dnsName": "string",
                              "port": number,
                              "testTrafficRules": {
                                 "header": {
                                    "name": "string",
                                    "value": {
                                       "exact": "string"
                                    }
                                 }
                              }
                           }
                        ],
                        "discoveryName": "string",
                        "ingressPortOverride": number,
                        "portName": "string",
                        "timeout": {
                           "idleTimeoutSeconds": number,
                           "perRequestTimeoutSeconds": number
                        },
                        "tls": {
                           "issuerCertificateAuthority": {
                              "awsPcaAuthorityArn": "string"
                           },
                           "kmsKey": "string",
                           "roleArn": "string"
                        }
                     }
                  ]
               },
               "serviceConnectResources": [
                  {
                     "discoveryArn": "string",
                     "discoveryName": "string"
                  }
               ],
               "status": "string",
               "taskDefinition": "string",
               "updatedAt": number,
               "volumeConfigurations": [
                  {
                     "managedEBSVolume": {
                        "encrypted": boolean,
                        "filesystemType": "string",
                        "iops": number,
                        "kmsKeyId": "string",
                        "roleArn": "string",
                        "sizeInGiB": number,
                        "snapshotId": "string",
                        "tagSpecifications": [
                           {
                              "propagateTags": "string",
                              "resourceType": "string",
                              "tags": [
                                 {
                                    "key": "string",
                                    "value": "string"
                                 }
                              ]
                           }
                        ],
                        "throughput": number,
                        "volumeInitializationRate": number,
                        "volumeType": "string"
                     },
                     "name": "string"
                  }
               ],
               "vpcLatticeConfigurations": [
                  {
                     "portName": "string",
                     "roleArn": "string",
                     "targetGroupArn": "string"
                  }
               ]
            }
         ],
         "desiredCount": number,
         "enableECSManagedTags": boolean,
         "enableExecuteCommand": boolean,
         "events": [
            {
               "createdAt": number,
               "id": "string",
               "message": "string"
            }
         ],
         "healthCheckGracePeriodSeconds": number,
         "launchType": "string",
         "loadBalancers": [
            {
               "advancedConfiguration": {
                  "alternateTargetGroupArn": "string",
                  "productionListenerRule": "string",
                  "roleArn": "string",
                  "testListenerRule": "string"
               },
               "containerName": "string",
               "containerPort": number,
               "loadBalancerName": "string",
               "targetGroupArn": "string"
            }
         ],
         "networkConfiguration": {
            "awsvpcConfiguration": {
               "assignPublicIp": "string",
               "securityGroups": [ "string" ],
               "subnets": [ "string" ]
            }
         },
         "pendingCount": number,
         "placementConstraints": [
            {
               "expression": "string",
               "type": "string"
            }
         ],
         "placementStrategy": [
            {
               "field": "string",
               "type": "string"
            }
         ],
         "platformFamily": "string",
         "platformVersion": "string",
         "propagateTags": "string",
         "resourceManagementType": "string",
         "roleArn": "string",
         "runningCount": number,
         "schedulingStrategy": "string",
         "serviceArn": "string",
         "serviceName": "string",
         "serviceRegistries": [
            {
               "containerName": "string",
               "containerPort": number,
               "port": number,
               "registryArn": "string"
            }
         ],
         "status": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "taskDefinition": "string",
         "taskSets": [
            {
               "capacityProviderStrategy": [
                  {
                     "base": number,
                     "capacityProvider": "string",
                     "weight": number
                  }
               ],
               "clusterArn": "string",
               "computedDesiredCount": number,
               "createdAt": number,
               "externalId": "string",
               "fargateEphemeralStorage": {
                  "kmsKeyId": "string"
               },
               "id": "string",
               "launchType": "string",
               "loadBalancers": [
                  {
                     "advancedConfiguration": {
                        "alternateTargetGroupArn": "string",
                        "productionListenerRule": "string",
                        "roleArn": "string",
                        "testListenerRule": "string"
                     },
                     "containerName": "string",
                     "containerPort": number,
                     "loadBalancerName": "string",
                     "targetGroupArn": "string"
                  }
               ],
               "networkConfiguration": {
                  "awsvpcConfiguration": {
                     "assignPublicIp": "string",
                     "securityGroups": [ "string" ],
                     "subnets": [ "string" ]
                  }
               },
               "pendingCount": number,
               "platformFamily": "string",
               "platformVersion": "string",
               "runningCount": number,
               "scale": {
                  "unit": "string",
                  "value": number
               },
               "serviceArn": "string",
               "serviceRegistries": [
                  {
                     "containerName": "string",
                     "containerPort": number,
                     "port": number,
                     "registryArn": "string"
                  }
               ],
               "stabilityStatus": "string",
               "stabilityStatusAt": number,
               "startedBy": "string",
               "status": "string",
               "tags": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ],
               "taskDefinition": "string",
               "taskSetArn": "string",
               "updatedAt": number
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_DescribeServices_ResponseSyntax) **   <a name="ECS-DescribeServices-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

 ** [services](#API_DescribeServices_ResponseSyntax) **   <a name="ECS-DescribeServices-response-services"></a>
The list of services described.
Type: Array of [Service](API_Service.md) objects

## Errors
<a name="API_DescribeServices_Errors"></a>

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
<a name="API_DescribeServices_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DescribeServices_Example_1"></a>

This example request provides a full description of the `test-service` service in the `telemetry` cluster.

#### Sample Request
<a name="API_DescribeServices_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 55
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeServices
X-Amz-Date: 20150528T163859Z
User-Agent: aws-cli/1.7.30 Python/2.7.9 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "services": [
    "test-service"
  ],
  "cluster": "telemetry"
}
```

#### Sample Response
<a name="API_DescribeServices_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 19:02:59 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 2449
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "failures": [],
  "services": [
    {
      "clusterArn": "arn:aws:ecs:us-west-2:012345678910:cluster/telemetry",
      "deploymentConfiguration": {
          "maximumPercent": 200,
          "minimumHealthyPercent": 100
      },
      "deployments": [
        {
          "createdAt": 1432829320.611,
          "desiredCount": 4,
          "id": "ecs-svc/9223370604025455196",
          "pendingCount": 0,
          "runningCount": 4,
          "status": "PRIMARY",
          "taskDefinition": "arn:aws:ecs:us-west-2:012345678910:task-definition/hpcc-t2-medium:1",
          "updatedAt": 1432829320.611
        }
      ],
      "desiredCount": 4,
      "events": [],
      "loadBalancers": [],
      "pendingCount": 0,
      "runningCount": 4,
      "serviceArn": "arn:aws:ecs:us-west-2:012345678910:service/default/test-service",
      "serviceName": "test-service",
      "status": "ACTIVE",
      "taskDefinition": "arn:aws:ecs:us-west-2:012345678910:task-definition/hpcc-t2-medium:1"
    }
  ]
}
```

### Example 2
<a name="API_DescribeServices_Example_2"></a>

This example describes a service that has a pause lifecycle hook configured.

#### Sample Request
<a name="API_DescribeServices_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 75
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeServices
X-Amz-Date: 20260506T160000Z
User-Agent: aws-cli/2.26 Python/3.12.6 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "services": [
    "ecs-service-with-pause-hook"
  ],
  "cluster": "my-cluster"
}
```

#### Sample Response
<a name="API_DescribeServices_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue May 6, 2026 16:00:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 1200
Connection: keep-alive
RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "failures": [],
  "services": [
    {
      "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/ecs-service-with-pause-hook",
      "serviceName": "ecs-service-with-pause-hook",
      "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster",
      "deploymentConfiguration": {
          "maximumPercent": 200,
          "minimumHealthyPercent": 100,
          "strategy": "BLUE_GREEN",
          "lifecycleHooks": [
              {
                  "targetType": "PAUSE",
                  "lifecycleStages": ["POST_PRODUCTION_TRAFFIC_SHIFT"],
                  "timeoutConfiguration": {
                      "timeoutInMinutes": 60,
                      "action": "ROLLBACK"
                  }
              }
          ]
      },
      "deployments": [
        {
          "id": "ecs-svc/9223370604025455196",
          "status": "PRIMARY",
          "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/ecs-demo:1",
          "desiredCount": 2,
          "pendingCount": 0,
          "runningCount": 2,
          "createdAt": 1746547200.000,
          "updatedAt": 1746547200.000
        }
      ],
      "desiredCount": 2,
      "events": [],
      "loadBalancers": [],
      "pendingCount": 0,
      "runningCount": 2,
      "status": "ACTIVE",
      "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/ecs-demo:1"
    }
  ]
}
```

## See Also
<a name="API_DescribeServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeServices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeServices)

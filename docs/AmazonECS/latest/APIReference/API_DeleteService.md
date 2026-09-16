---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteService.html
---

# DeleteService
<a name="API_DeleteService"></a>

Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you can't delete it, and you must update the service to a desired task count of zero. For more information, see [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html).

**Note**
When you delete a service, if there are still running tasks that require cleanup, the service status moves from `ACTIVE` to `DRAINING`, and the service is no longer visible in the console or in the [ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html) API operation. After all tasks have transitioned to either `STOPPING` or `STOPPED` status, the service status moves from `DRAINING` to `INACTIVE`. Services in the `DRAINING` or `INACTIVE` status can still be viewed with the [DescribeServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html) API operation. However, in the future, `INACTIVE` services may be cleaned up and purged from Amazon ECS record keeping, and [DescribeServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html) calls on those services return a `ServiceNotFoundException` error.

**Important**
If you attempt to create a new service with the same name as an existing service in either `ACTIVE` or `DRAINING` status, you receive an error.

## Request Syntax
<a name="API_DeleteService_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "force": {{boolean}},
   "service": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_DeleteService_RequestSyntax) **   <a name="ECS-DeleteService-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [force](#API_DeleteService_RequestSyntax) **   <a name="ECS-DeleteService-request-force"></a>
If `true`, allows you to delete a service even if it wasn't scaled down to zero tasks. It's only necessary to use this if the service uses the `REPLICA` scheduling strategy.
Type: Boolean
Required: No

 ** [service](#API_DeleteService_RequestSyntax) **   <a name="ECS-DeleteService-request-service"></a>
The name of the service to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteService_ResponseSyntax"></a>

```
{
   "service": {
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
}
```

## Response Elements
<a name="API_DeleteService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_DeleteService_ResponseSyntax) **   <a name="ECS-DeleteService-response-service"></a>
The full description of the deleted service.
Type: [Service](API_Service.md) object

## Errors
<a name="API_DeleteService_Errors"></a>

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

 ** ServiceNotFoundException **
The specified service wasn't found. You can view your available services with [ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html). Amazon ECS services are cluster specific and Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_DeleteService_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DeleteService_Example_1"></a>

This example API request deletes the `test` service from the `default` cluster.

#### Sample Request
<a name="API_DeleteService_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 19
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DeleteService
X-Amz-Date: 20150429T172539Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "service": "test"
}
```

#### Sample Response
<a name="API_DeleteService_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 17:25:40 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 13590
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "service": {
    "clusterArn": "arn:aws:ecs:us-east-1:012345678910:cluster/default",
    "deploymentConfiguration": {
        "maximumPercent": 200,
        "minimumHealthyPercent": 100
    },
    "deployments": [
      {
        "createdAt": 1430320735.285,
        "desiredCount": 0,
        "id": "ecs-svc/9223370606534040511",
        "pendingCount": 0,
        "runningCount": 0,
        "status": "PRIMARY",
        "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/sleep360:27",
        "updatedAt": 1430320735.285
      }
    ],
    "desiredCount": 0,
    "events": [],
    "loadBalancers": [],
    "pendingCount": 0,
    "runningCount": 0,
    "serviceArn": "arn:aws:ecs:us-east-1:012345678910:service/default/test",
    "serviceName": "test",
    "status": "DRAINING",
    "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/sleep360:27"
  }
}
```

## See Also
<a name="API_DeleteService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DeleteService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DeleteService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeleteService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DeleteService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeleteService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DeleteService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DeleteService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DeleteService)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeleteService)

---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceRevisions.html
---

# DescribeServiceRevisions
<a name="API_DescribeServiceRevisions"></a>

Describes one or more service revisions.

A service revision is a version of the service that includes the values for the Amazon ECS resources (for example, task definition) and the environment resources (for example, load balancers, subnets, and security groups). For more information, see [Amazon ECS service revisions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html).

You can't describe a service revision that was created before October 25, 2024.

## Request Syntax
<a name="API_DescribeServiceRevisions_RequestSyntax"></a>

```
{
   "serviceRevisionArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeServiceRevisions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceRevisionArns](#API_DescribeServiceRevisions_RequestSyntax) **   <a name="ECS-DescribeServiceRevisions-request-serviceRevisionArns"></a>
The ARN of the service revision.
You can specify a maximum of 20 ARNs.
You can call [ListServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html) to get the ARNs.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_DescribeServiceRevisions_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "arn": "string",
         "detail": "string",
         "reason": "string"
      }
   ],
   "serviceRevisions": [
      {
         "capacityProviderStrategy": [
            {
               "base": number,
               "capacityProvider": "string",
               "weight": number
            }
         ],
         "clusterArn": "string",
         "containerImages": [
            {
               "containerName": "string",
               "image": "string",
               "imageDigest": "string"
            }
         ],
         "createdAt": number,
         "ecsManagedResources": {
            "autoScaling": {
               "applicationAutoScalingPolicies": [
                  {
                     "arn": "string",
                     "metric": "string",
                     "policyType": "string",
                     "status": "string",
                     "statusReason": "string",
                     "targetValue": number,
                     "updatedAt": number
                  }
               ],
               "scalableTarget": {
                  "arn": "string",
                  "maxCapacity": number,
                  "minCapacity": number,
                  "status": "string",
                  "statusReason": "string",
                  "updatedAt": number
               }
            },
            "ingressPaths": [
               {
                  "accessType": "string",
                  "certificate": {
                     "arn": "string",
                     "domainName": "string",
                     "status": "string",
                     "statusReason": "string",
                     "updatedAt": number
                  },
                  "endpoint": "string",
                  "listener": {
                     "arn": "string",
                     "status": "string",
                     "statusReason": "string",
                     "updatedAt": number
                  },
                  "loadBalancer": {
                     "arn": "string",
                     "scheme": "string",
                     "securityGroupIds": [ "string" ],
                     "status": "string",
                     "statusReason": "string",
                     "subnetIds": [ "string" ],
                     "updatedAt": number
                  },
                  "loadBalancerSecurityGroups": [
                     {
                        "arn": "string",
                        "status": "string",
                        "statusReason": "string",
                        "updatedAt": number
                     }
                  ],
                  "rule": {
                     "arn": "string",
                     "status": "string",
                     "statusReason": "string",
                     "updatedAt": number
                  },
                  "targetGroups": [
                     {
                        "arn": "string",
                        "healthCheckPath": "string",
                        "healthCheckPort": number,
                        "port": number,
                        "status": "string",
                        "statusReason": "string",
                        "updatedAt": number
                     }
                  ]
               }
            ],
            "logGroups": [
               {
                  "arn": "string",
                  "logGroupName": "string",
                  "status": "string",
                  "statusReason": "string",
                  "updatedAt": number
               }
            ],
            "metricAlarms": [
               {
                  "arn": "string",
                  "status": "string",
                  "statusReason": "string",
                  "updatedAt": number
               }
            ],
            "serviceSecurityGroups": [
               {
                  "arn": "string",
                  "status": "string",
                  "statusReason": "string",
                  "updatedAt": number
               }
            ]
         },
         "fargateEphemeralStorage": {
            "kmsKeyId": "string"
         },
         "guardDutyEnabled": boolean,
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
         "monitoring": {
            "metricConfigurations": [
               {
                  "metricNames": [ "string" ],
                  "resolutionSeconds": number
               }
            ]
         },
         "networkConfiguration": {
            "awsvpcConfiguration": {
               "assignPublicIp": "string",
               "securityGroups": [ "string" ],
               "subnets": [ "string" ]
            }
         },
         "overrides": {
            "runtimePlatform": {
               "cpuArchitecture": "string"
            }
         },
         "platformFamily": "string",
         "platformVersion": "string",
         "resolvedConfiguration": {
            "loadBalancers": [
               {
                  "productionListenerRule": "string",
                  "targetGroupArn": "string"
               }
            ],
            "vpcLatticeConfigurations": [
               {
                  "productionListenerRule": "string",
                  "targetGroupArn": "string"
               }
            ]
         },
         "serviceArn": "string",
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
         "serviceRegistries": [
            {
               "containerName": "string",
               "containerPort": number,
               "port": number,
               "registryArn": "string"
            }
         ],
         "serviceRevisionArn": "string",
         "taskDefinition": "string",
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
               "advancedConfiguration": {
                  "alternateTargetGroupArn": "string",
                  "productionListenerRule": "string",
                  "testListenerRule": "string"
               },
               "portName": "string",
               "roleArn": "string",
               "targetGroupArn": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeServiceRevisions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_DescribeServiceRevisions_ResponseSyntax) **   <a name="ECS-DescribeServiceRevisions-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

 ** [serviceRevisions](#API_DescribeServiceRevisions_ResponseSyntax) **   <a name="ECS-DescribeServiceRevisions-response-serviceRevisions"></a>
The list of service revisions described.
Type: Array of [ServiceRevision](API_ServiceRevision.md) objects

## Errors
<a name="API_DescribeServiceRevisions_Errors"></a>

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

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_DescribeServiceRevisions_Examples"></a>

### Example
<a name="API_DescribeServiceRevisions_Example_1"></a>

This example request provides a full description of the service revision with the ARN `arn:aws:ecs:us-west-2:123456789012:service-revision/testc/sd1/4980306466373577095`.

#### Sample Request
<a name="API_DescribeServiceRevisions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 55
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeServiceRevisions
X-Amz-Date: 20150528T163859Z
User-Agent: aws-cli/2.17 Python/3.11.9 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{

  "serviceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/testc/sd1/4980306466373577095"
}
```

#### Sample Response
<a name="API_DescribeServiceRevisions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue, 10 Sep 2024 18:50:14 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 220
Connection: keep-alive
RequestId: 360c5551-123e-4e74-9914-7582d3a28807
{
    "serviceRevisions": [
        {
            "serviceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/example/sd-example/4980306466373577095",
            "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/example/sd-example",
            "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/example",
            "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/large-ngingx:1",
            "launchType": "FARGATE",
            "platformVersion": "1.4.0",
            "platformFamily": "DockerLinux",
            "networkConfiguration": {
                "awsvpcConfiguration": {
                    "subnets": [
                        "subnet-0a4040e73895f04e1"
                    ],
                    "securityGroups": [
                        "sg-09605d60a6bc1b296"
                    ],
                    "assignPublicIp": "ENABLED"
                }
            },
            "createdAt": "2024-09-10T16:49:26.39Z"
        }
    ],
    "failures": []
}
    ],
    "failures": []
}
```

## See Also
<a name="API_DescribeServiceRevisions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeServiceRevisions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeServiceRevisions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeServiceRevisions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeServiceRevisions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeServiceRevisions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeServiceRevisions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeServiceRevisions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeServiceRevisions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeServiceRevisions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeServiceRevisions)

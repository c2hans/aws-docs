---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html
---

# DescribeServiceDeployments
<a name="API_DescribeServiceDeployments"></a>

Describes one or more of your service deployments.

A service deployment happens when you release a software update for the service. For more information, see [View service history using Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html).

## Request Syntax
<a name="API_DescribeServiceDeployments_RequestSyntax"></a>

```
{
   "serviceDeploymentArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeServiceDeployments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceDeploymentArns](#API_DescribeServiceDeployments_RequestSyntax) **   <a name="ECS-DescribeServiceDeployments-request-serviceDeploymentArns"></a>
The ARN of the service deployment.
You can specify a maximum of 20 ARNs.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_DescribeServiceDeployments_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "arn": "string",
         "detail": "string",
         "reason": "string"
      }
   ],
   "serviceDeployments": [
      {
         "alarms": {
            "alarmNames": [ "string" ],
            "status": "string",
            "triggeredAlarmNames": [ "string" ]
         },
         "clusterArn": "string",
         "createdAt": number,
         "deploymentCircuitBreaker": {
            "failureCount": number,
            "status": "string",
            "threshold": number
         },
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
         "finishedAt": number,
         "lifecycleHookDetails": [
            {
               "expiresAt": number,
               "hookId": "string",
               "status": "string",
               "targetArn": "string",
               "targetType": "string",
               "timeoutAction": "string"
            }
         ],
         "lifecycleStage": "string",
         "rollback": {
            "reason": "string",
            "serviceRevisionArn": "string",
            "startedAt": number
         },
         "serviceArn": "string",
         "serviceDeploymentArn": "string",
         "sourceServiceRevisions": [
            {
               "arn": "string",
               "pendingTaskCount": number,
               "requestedProductionTrafficWeight": number,
               "requestedTaskCount": number,
               "requestedTestTrafficWeight": number,
               "runningTaskCount": number
            }
         ],
         "startedAt": number,
         "status": "string",
         "statusReason": "string",
         "stoppedAt": number,
         "targetServiceRevision": {
            "arn": "string",
            "pendingTaskCount": number,
            "requestedProductionTrafficWeight": number,
            "requestedTaskCount": number,
            "requestedTestTrafficWeight": number,
            "runningTaskCount": number
         },
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeServiceDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_DescribeServiceDeployments_ResponseSyntax) **   <a name="ECS-DescribeServiceDeployments-response-failures"></a>
Any failures associated with the call.
If you decsribe a deployment with a service revision created before October 25, 2024, the call fails. The failure includes the service revision ARN and the reason set to `MISSING`.
Type: Array of [Failure](API_Failure.md) objects

 ** [serviceDeployments](#API_DescribeServiceDeployments_ResponseSyntax) **   <a name="ECS-DescribeServiceDeployments-response-serviceDeployments"></a>
The list of service deployments described.
Type: Array of [ServiceDeployment](API_ServiceDeployment.md) objects

## Errors
<a name="API_DescribeServiceDeployments_Errors"></a>

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
<a name="API_DescribeServiceDeployments_Examples"></a>

### Example
<a name="API_DescribeServiceDeployments_Example_1"></a>

This example request provides a full description of the service deployments for the `sd-example` service on the `example` cluster.

#### Sample Request
<a name="API_DescribeServiceDeployments_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 55
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeServiceDeployments
X-Amz-Date: 20150528T163859Z
User-Agent: aws-cli/2.17 Python/3.11.9 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{

  "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5"
}
```

#### Sample Response
<a name="API_DescribeServiceDeployments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue, 10 Sep 2024 18:50:14 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 220
Connection: keep-alive
RequestId: 360c5551-123e-4e74-9914-7582d3a28807
{
    "serviceDeployments": [
        {
            "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5",
            "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/example/sd-example",
            "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/example",
            "updatedAt": "2024-09-10T16:49:35.57Z",
            "targetServiceRevision": {
                "arn": "arn:aws:ecs:us-west-2:123456789012:service-revision/example/sd-example/4980306466373577095",
                "requestedTaskCount": 0,
                "runningTaskCount": 0,
                "pendingTaskCount": 0
            },
            "status": "PENDING",
            "deploymentConfiguration": {
                "deploymentCircuitBreaker": {
                    "enable": false,
                    "rollback": false
                },
                "maximumPercent": 200,
                "minimumHealthyPercent": 100
            }
        }
    ],
    "failures": []
}
```

### Example 2
<a name="API_DescribeServiceDeployments_Example_2"></a>

This example describes a service deployment that is currently paused at a lifecycle hook.

#### Sample Request
<a name="API_DescribeServiceDeployments_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 130
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeServiceDeployments
X-Amz-Date: 20260506T160000Z
User-Agent: aws-cli/2.26 Python/3.12.6 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/xyz789ABC123"
}
```

#### Sample Response
<a name="API_DescribeServiceDeployments_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue May 6, 2026 16:00:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 850
Connection: keep-alive
RequestId: 580e7773-345g-6f96-1136-hi4567890123

{
    "serviceDeployments": [
        {
            "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/xyz789ABC123",
            "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
            "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster",
            "updatedAt": "2026-05-06T16:05:00.00Z",
            "targetServiceRevision": {
                "arn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/1234567890123456789",
                "requestedTaskCount": 2,
                "runningTaskCount": 2,
                "pendingTaskCount": 0
            },
            "status": "IN_PROGRESS",
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
            "lifecycleHookDetails": [
                {
                    "hookId": "ecs-pause-Xk7rT2mP9sLwQn4vB8fYd3hJ6gA1cE5iO0uR_ZpWq",
                    "targetType": "PAUSE",
                    "status": "AWAITING_ACTION",
                    "expiresAt": "2026-05-06T16:03:00.00Z",
                    "timeoutAction": "ROLLBACK"
                }
            ]
        }
    ],
    "failures": []
}
```

## See Also
<a name="API_DescribeServiceDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeServiceDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeServiceDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeServiceDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeServiceDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeServiceDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeServiceDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeServiceDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeServiceDeployments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeServiceDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeServiceDeployments)

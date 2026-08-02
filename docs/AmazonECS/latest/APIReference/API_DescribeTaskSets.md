---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskSets.html
---

# DescribeTaskSets
<a name="API_DescribeTaskSets"></a>

Describes the task sets in the specified cluster and service. This is used when a service uses the `EXTERNAL` deployment controller type. For more information, see [Amazon ECS Deployment Types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html) in the *Amazon Elastic Container Service Developer Guide*.

## Request Syntax
<a name="API_DescribeTaskSets_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "include": [ "{{string}}" ],
   "service": "{{string}}",
   "taskSets": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeTaskSets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_DescribeTaskSets_RequestSyntax) **   <a name="ECS-DescribeTaskSets-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.
Type: String
Required: Yes

 ** [include](#API_DescribeTaskSets_RequestSyntax) **   <a name="ECS-DescribeTaskSets-request-include"></a>
Specifies whether to see the resource tags for the task set. If `TAGS` is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.
Type: Array of strings
Valid Values: `TAGS`
Required: No

 ** [service](#API_DescribeTaskSets_RequestSyntax) **   <a name="ECS-DescribeTaskSets-request-service"></a>
The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in.
Type: String
Required: Yes

 ** [taskSets](#API_DescribeTaskSets_RequestSyntax) **   <a name="ECS-DescribeTaskSets-request-taskSets"></a>
The ID or full Amazon Resource Name (ARN) of task sets to describe.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_DescribeTaskSets_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "arn": "string",
         "detail": "string",
         "reason": "string"
      }
   ],
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
```

## Response Elements
<a name="API_DescribeTaskSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_DescribeTaskSets_ResponseSyntax) **   <a name="ECS-DescribeTaskSets-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

 ** [taskSets](#API_DescribeTaskSets_ResponseSyntax) **   <a name="ECS-DescribeTaskSets-response-taskSets"></a>
The list of task sets described.
Type: Array of [TaskSet](API_TaskSet.md) objects

## Errors
<a name="API_DescribeTaskSets_Errors"></a>

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

 ** ServiceNotActiveException **
The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

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

## See Also
<a name="API_DescribeTaskSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeTaskSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeTaskSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeTaskSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeTaskSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeTaskSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeTaskSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeTaskSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeTaskSets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeTaskSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeTaskSets)

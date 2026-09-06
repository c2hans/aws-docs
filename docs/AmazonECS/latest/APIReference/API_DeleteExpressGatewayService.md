---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteExpressGatewayService.html
---

# DeleteExpressGatewayService
<a name="API_DeleteExpressGatewayService"></a>

Deletes an Express service and removes all associated AWS resources. This operation stops service tasks, removes the Application Load Balancer, target groups, security groups, auto-scaling policies, and other managed infrastructure components.

The service enters a `DRAINING` state where existing tasks complete current requests without starting new tasks. After all tasks stop, the service and infrastructure are permanently removed.

This operation cannot be reversed. Back up important data and verify the service is no longer needed before deletion.

## Request Syntax
<a name="API_DeleteExpressGatewayService_RequestSyntax"></a>

```
{
   "serviceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteExpressGatewayService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceArn](#API_DeleteExpressGatewayService_RequestSyntax) **   <a name="ECS-DeleteExpressGatewayService-request-serviceArn"></a>
The Amazon Resource Name (ARN) of the Express service to delete. The ARN uniquely identifies the service within your AWS account and region.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteExpressGatewayService_ResponseSyntax"></a>

```
{
   "service": {
      "activeConfigurations": [
         {
            "cpu": "string",
            "createdAt": number,
            "executionRoleArn": "string",
            "healthCheckPath": "string",
            "ingressPaths": [
               {
                  "accessType": "string",
                  "endpoint": "string"
               }
            ],
            "memory": "string",
            "networkConfiguration": {
               "securityGroups": [ "string" ],
               "subnets": [ "string" ]
            },
            "primaryContainer": {
               "awsLogsConfiguration": {
                  "logGroup": "string",
                  "logStreamPrefix": "string"
               },
               "command": [ "string" ],
               "containerPort": number,
               "environment": [
                  {
                     "name": "string",
                     "value": "string"
                  }
               ],
               "image": "string",
               "repositoryCredentials": {
                  "credentialsParameter": "string"
               },
               "secrets": [
                  {
                     "name": "string",
                     "valueFrom": "string"
                  }
               ]
            },
            "scalingTarget": {
               "autoScalingMetric": "string",
               "autoScalingTargetValue": number,
               "maxTaskCount": number,
               "minTaskCount": number
            },
            "serviceRevisionArn": "string",
            "taskDefinitionArn": "string",
            "taskRoleArn": "string"
         }
      ],
      "cluster": "string",
      "createdAt": number,
      "currentDeployment": "string",
      "infrastructureRoleArn": "string",
      "serviceArn": "string",
      "serviceName": "string",
      "status": {
         "statusCode": "string",
         "statusReason": "string"
      },
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_DeleteExpressGatewayService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_DeleteExpressGatewayService_ResponseSyntax) **   <a name="ECS-DeleteExpressGatewayService-response-service"></a>
The full description of the deleted express service.
Type: [ECSExpressGatewayService](API_ECSExpressGatewayService.md) object

## Errors
<a name="API_DeleteExpressGatewayService_Errors"></a>

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
<a name="API_DeleteExpressGatewayService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DeleteExpressGatewayService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DeleteExpressGatewayService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeleteExpressGatewayService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DeleteExpressGatewayService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeleteExpressGatewayService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DeleteExpressGatewayService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DeleteExpressGatewayService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DeleteExpressGatewayService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteExpressGatewayService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeleteExpressGatewayService)

---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateExpressGatewayService.html
---

# UpdateExpressGatewayService
<a name="API_UpdateExpressGatewayService"></a>

Updates an existing Express service configuration. Modifies container settings, resource allocation, auto-scaling configuration, and other service parameters without recreating the service.

Amazon ECS creates a new service revision with updated configuration and performs a rolling deployment to replace existing tasks. The service remains available during updates, ensuring zero-downtime deployments.

Some parameters like the infrastructure role cannot be modified after service creation and require creating a new service.

## Request Syntax
<a name="API_UpdateExpressGatewayService_RequestSyntax"></a>

```
{
   "cpu": "{{string}}",
   "executionRoleArn": "{{string}}",
   "healthCheckPath": "{{string}}",
   "memory": "{{string}}",
   "networkConfiguration": {
      "securityGroups": [ "{{string}}" ],
      "subnets": [ "{{string}}" ]
   },
   "primaryContainer": {
      "awsLogsConfiguration": {
         "logGroup": "{{string}}",
         "logStreamPrefix": "{{string}}"
      },
      "command": [ "{{string}}" ],
      "containerPort": {{number}},
      "environment": [
         {
            "name": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "image": "{{string}}",
      "repositoryCredentials": {
         "credentialsParameter": "{{string}}"
      },
      "secrets": [
         {
            "name": "{{string}}",
            "valueFrom": "{{string}}"
         }
      ]
   },
   "scalingTarget": {
      "autoScalingMetric": "{{string}}",
      "autoScalingTargetValue": {{number}},
      "maxTaskCount": {{number}},
      "minTaskCount": {{number}}
   },
   "serviceArn": "{{string}}",
   "taskDefinitionArn": "{{string}}",
   "taskRoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateExpressGatewayService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cpu](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-cpu"></a>
The number of CPU units used by the task.
Type: String
Required: No

 ** [executionRoleArn](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the task execution role for the Express service.
Type: String
Required: No

 ** [healthCheckPath](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-healthCheckPath"></a>
The path on the container for Application Load Balancer health checks.
Type: String
Required: No

 ** [memory](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-memory"></a>
The amount of memory (in MiB) used by the task.
Type: String
Required: No

 ** [networkConfiguration](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-networkConfiguration"></a>
The network configuration for the Express service tasks. By default, the network configuration for an Express service uses the default VPC.
Type: [ExpressGatewayServiceNetworkConfiguration](API_ExpressGatewayServiceNetworkConfiguration.md) object
Required: No

 ** [primaryContainer](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-primaryContainer"></a>
The primary container configuration for the Express service.
Type: [ExpressGatewayContainer](API_ExpressGatewayContainer.md) object
Required: No

 ** [scalingTarget](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-scalingTarget"></a>
The auto-scaling configuration for the Express service.
Type: [ExpressGatewayScalingTarget](API_ExpressGatewayScalingTarget.md) object
Required: No

 ** [serviceArn](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-serviceArn"></a>
The Amazon Resource Name (ARN) of the Express service to update.
Type: String
Required: Yes

 ** [taskDefinitionArn](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-taskDefinitionArn"></a>
The Amazon Resource Name (ARN) of a task definition to use to update the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.
The task definition must have a container named `Main` with a single TCP port mapping that includes a container port and port name. The task definition must also have `FARGATE` compatibility.
If you provide a task definition ARN, you cannot also specify `primaryContainer`, `executionRoleArn`, `taskRoleArn`, `cpu`, or `memory`.
Type: String
Required: No

 ** [taskRoleArn](#API_UpdateExpressGatewayService_RequestSyntax) **   <a name="ECS-UpdateExpressGatewayService-request-taskRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role for containers in this task.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateExpressGatewayService_ResponseSyntax"></a>

```
{
   "service": {
      "cluster": "string",
      "createdAt": number,
      "serviceArn": "string",
      "serviceName": "string",
      "status": {
         "statusCode": "string",
         "statusReason": "string"
      },
      "targetConfiguration": {
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
      },
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_UpdateExpressGatewayService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_UpdateExpressGatewayService_ResponseSyntax) **   <a name="ECS-UpdateExpressGatewayService-response-service"></a>
The full description of your express gateway service following the update call.
Type: [UpdatedExpressGatewayService](API_UpdatedExpressGatewayService.md) object

## Errors
<a name="API_UpdateExpressGatewayService_Errors"></a>

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
<a name="API_UpdateExpressGatewayService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/UpdateExpressGatewayService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/UpdateExpressGatewayService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateExpressGatewayService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/UpdateExpressGatewayService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateExpressGatewayService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/UpdateExpressGatewayService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/UpdateExpressGatewayService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/UpdateExpressGatewayService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/UpdateExpressGatewayService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateExpressGatewayService)

---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateExpressGatewayService.html
---

# CreateExpressGatewayService
<a name="API_CreateExpressGatewayService"></a>

Creates an Express service that simplifies deploying containerized web applications on Amazon ECS with managed AWS infrastructure. This operation provisions and configures Application Load Balancers, target groups, security groups, and auto-scaling policies automatically.

Specify a primary container configuration with your application image and basic settings. Amazon ECS creates the necessary AWS resources for traffic distribution, health monitoring, network access control, and capacity management.

Provide an execution role for task operations and an infrastructure role for managing AWS resources on your behalf.

## Request Syntax
<a name="API_CreateExpressGatewayService_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "cpu": "{{string}}",
   "executionRoleArn": "{{string}}",
   "healthCheckPath": "{{string}}",
   "infrastructureRoleArn": "{{string}}",
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
   "serviceName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "taskDefinitionArn": "{{string}}",
   "taskRoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateExpressGatewayService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster on which to create the Express service. If you do not specify a cluster, the `default` cluster is assumed.
Type: String
Required: No

 ** [cpu](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-cpu"></a>
The number of CPU units used by the task. This parameter determines the CPU allocation for each task in the Express service. The default value for an Express service is 256 (.25 vCPU).
Type: String
Required: No

 ** [executionRoleArn](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make AWS API calls on your behalf. This role is required for Amazon ECS to pull container images from Amazon ECR, send container logs to Amazon CloudWatch Logs, and retrieve sensitive data from AWS Systems Manager Parameter Store or AWS Secrets Manager.
The execution role must include the `AmazonECSTaskExecutionRolePolicy` managed policy or equivalent permissions. For Express services, this role is used during task startup and runtime for container management operations.
Type: String
Required: No

 ** [healthCheckPath](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-healthCheckPath"></a>
The path on the container that the Application Load Balancer uses for health checks. This should be a valid HTTP endpoint that returns a successful response (HTTP 200) when the application is healthy.
If not specified, the default health check path is `/ping`. The health check path must start with a forward slash and can include query parameters. Examples: `/health`, `/api/status`, `/ping?format=json`.
Type: String
Required: No

 ** [infrastructureRoleArn](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-infrastructureRoleArn"></a>
The Amazon Resource Name (ARN) of the infrastructure role that grants Amazon ECS permission to create and manage AWS resources on your behalf for the Express service. This role is used to provision and manage Application Load Balancers, target groups, security groups, auto-scaling policies, and other AWS infrastructure components.
The infrastructure role must include permissions for Elastic Load Balancing, Application Auto Scaling, Amazon EC2 (for security groups), and other services required for managed infrastructure. This role is only used during Express service creation, updates, and deletion operations.
Type: String
Required: Yes

 ** [memory](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-memory"></a>
The amount of memory (in MiB) used by the task. This parameter determines the memory allocation for each task in the Express service. The default value for an express service is 512 MiB.
Type: String
Required: No

 ** [networkConfiguration](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-networkConfiguration"></a>
The network configuration for the Express service tasks. This specifies the VPC subnets and security groups for the tasks.
For Express services, you can specify custom security groups and subnets. If not provided, Amazon ECS will use the default VPC configuration and create appropriate security groups automatically. The network configuration determines how your service integrates with your VPC and what network access it has.
Type: [ExpressGatewayServiceNetworkConfiguration](API_ExpressGatewayServiceNetworkConfiguration.md) object
Required: No

 ** [primaryContainer](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-primaryContainer"></a>
The primary container configuration for the Express service. This defines the main application container that will receive traffic from the Application Load Balancer.
The primary container must specify at minimum a container image. You can also configure the container port (defaults to 80), logging configuration, environment variables, secrets, and startup commands. The container image can be from Amazon ECR, Docker Hub, or any other container registry accessible to your execution role.
Type: [ExpressGatewayContainer](API_ExpressGatewayContainer.md) object
Required: No

 ** [scalingTarget](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-scalingTarget"></a>
The auto-scaling configuration for the Express service. This defines how the service automatically adjusts the number of running tasks based on demand.
You can specify the minimum and maximum number of tasks, the scaling metric (CPU utilization, memory utilization, or request count per target), and the target value for the metric. If not specified, the default target value for an Express service is 60.
Type: [ExpressGatewayScalingTarget](API_ExpressGatewayScalingTarget.md) object
Required: No

 ** [serviceName](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-serviceName"></a>
The name of the Express service. This name must be unique within the specified cluster and can contain up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens. The name is used to identify the service in the Amazon ECS console and API operations.
If you don't specify a service name, Amazon ECS generates a unique name for the service. The service name becomes part of the service ARN and cannot be changed after the service is created.
Type: String
Required: No

 ** [tags](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-tags"></a>
The metadata that you apply to the Express service to help categorize and organize it. Each tag consists of a key and an optional value. You can apply up to 50 tags to a service.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [taskDefinitionArn](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-taskDefinitionArn"></a>
The Amazon Resource Name (ARN) of a task definition to use to create the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.
The task definition must have a container named `Main` with a single TCP port mapping that includes a container port and port name. The task definition must also have `FARGATE` compatibility.
If you provide a task definition ARN, you cannot also specify `primaryContainer`, `executionRoleArn`, `taskRoleArn`, `cpu`, or `memory`.
Type: String
Required: No

 ** [taskRoleArn](#API_CreateExpressGatewayService_RequestSyntax) **   <a name="ECS-CreateExpressGatewayService-request-taskRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. This role allows your application code to access other AWS services securely.
The task role is different from the execution role. While the execution role is used by the Amazon ECS agent to set up the task, the task role is used by your application code running inside the container to make AWS API calls. If your application doesn't need to access AWS services, you can omit this parameter.
Type: String
Required: No

## Response Syntax
<a name="API_CreateExpressGatewayService_ResponseSyntax"></a>

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
<a name="API_CreateExpressGatewayService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_CreateExpressGatewayService_ResponseSyntax) **   <a name="ECS-CreateExpressGatewayService-response-service"></a>
The full description of your Express service following the create operation.
Type: [ECSExpressGatewayService](API_ECSExpressGatewayService.md) object

## Errors
<a name="API_CreateExpressGatewayService_Errors"></a>

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

 ** PlatformTaskDefinitionIncompatibilityException **
The specified platform version doesn't satisfy the required capabilities of the task definition.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** PlatformUnknownException **
The specified platform version doesn't exist.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateExpressGatewayService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/CreateExpressGatewayService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/CreateExpressGatewayService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CreateExpressGatewayService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/CreateExpressGatewayService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CreateExpressGatewayService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/CreateExpressGatewayService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/CreateExpressGatewayService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/CreateExpressGatewayService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/CreateExpressGatewayService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CreateExpressGatewayService)

---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeExpressGatewayService.html
---

# DescribeExpressGatewayService
<a name="API_DescribeExpressGatewayService"></a>

Retrieves detailed information about an Express service, including current status, configuration, managed infrastructure, and service revisions.

Returns comprehensive service details, active service revisions, ingress paths with endpoints, and managed AWS resource status including load balancers and auto-scaling policies.

Use the `include` parameter to retrieve additional information such as resource tags.

## Request Syntax
<a name="API_DescribeExpressGatewayService_RequestSyntax"></a>

```
{
   "include": [ "{{string}}" ],
   "serviceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeExpressGatewayService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [include](#API_DescribeExpressGatewayService_RequestSyntax) **   <a name="ECS-DescribeExpressGatewayService-request-include"></a>
Specifies additional information to include in the response. Valid values are `TAGS` to include resource tags associated with the Express service.
Type: Array of strings
Valid Values: `TAGS`
Required: No

 ** [serviceArn](#API_DescribeExpressGatewayService_RequestSyntax) **   <a name="ECS-DescribeExpressGatewayService-request-serviceArn"></a>
The Amazon Resource Name (ARN) of the Express service to describe. The ARN uniquely identifies the service within your AWS account and region.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeExpressGatewayService_ResponseSyntax"></a>

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
<a name="API_DescribeExpressGatewayService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_DescribeExpressGatewayService_ResponseSyntax) **   <a name="ECS-DescribeExpressGatewayService-response-service"></a>
The full description of the described express service.
Type: [ECSExpressGatewayService](API_ECSExpressGatewayService.md) object

## Errors
<a name="API_DescribeExpressGatewayService_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource wasn't found.
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
<a name="API_DescribeExpressGatewayService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeExpressGatewayService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeExpressGatewayService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeExpressGatewayService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeExpressGatewayService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeExpressGatewayService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeExpressGatewayService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeExpressGatewayService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeExpressGatewayService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeExpressGatewayService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeExpressGatewayService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

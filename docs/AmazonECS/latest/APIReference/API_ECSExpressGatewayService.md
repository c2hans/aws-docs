---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ECSExpressGatewayService.html
---

# ECSExpressGatewayService
<a name="API_ECSExpressGatewayService"></a>

Represents an Express service, which provides a simplified way to deploy containerized web applications on Amazon ECS with managed AWS infrastructure. An Express service automatically provisions and manages Application Load Balancers, target groups, security groups, and auto-scaling policies.

Express services use a service revision architecture where each service can have multiple active configurations, enabling blue-green deployments and gradual rollouts. The service maintains a list of active configurations and manages the lifecycle of the underlying AWS resources.

## Contents
<a name="API_ECSExpressGatewayService_Contents"></a>

 ** activeConfigurations **   <a name="ECS-Type-ECSExpressGatewayService-activeConfigurations"></a>
The list of active service configurations for the Express service.
Type: Array of [ExpressGatewayServiceConfiguration](API_ExpressGatewayServiceConfiguration.md) objects
Required: No

 ** cluster **   <a name="ECS-Type-ECSExpressGatewayService-cluster"></a>
The short name or full ARN of the cluster that hosts the Express service.
Type: String
Required: No

 ** createdAt **   <a name="ECS-Type-ECSExpressGatewayService-createdAt"></a>
The Unix timestamp for when the Express service was created.
Type: Timestamp
Required: No

 ** currentDeployment **   <a name="ECS-Type-ECSExpressGatewayService-currentDeployment"></a>
The current deployment configuration for the Express service.
Type: String
Required: No

 ** infrastructureRoleArn **   <a name="ECS-Type-ECSExpressGatewayService-infrastructureRoleArn"></a>
The ARN of the infrastructure role that manages AWS resources for the Express service.
Type: String
Required: No

 ** serviceArn **   <a name="ECS-Type-ECSExpressGatewayService-serviceArn"></a>
The ARN that identifies the Express service.
Type: String
Required: No

 ** serviceName **   <a name="ECS-Type-ECSExpressGatewayService-serviceName"></a>
The name of the Express service.
Type: String
Required: No

 ** status **   <a name="ECS-Type-ECSExpressGatewayService-status"></a>
The current status of the Express service.
Type: [ExpressGatewayServiceStatus](API_ExpressGatewayServiceStatus.md) object
Required: No

 ** tags **   <a name="ECS-Type-ECSExpressGatewayService-tags"></a>
The metadata applied to the Express service.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** updatedAt **   <a name="ECS-Type-ECSExpressGatewayService-updatedAt"></a>
The Unix timestamp for when the Express service was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ECSExpressGatewayService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ECSExpressGatewayService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ECSExpressGatewayService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ECSExpressGatewayService)

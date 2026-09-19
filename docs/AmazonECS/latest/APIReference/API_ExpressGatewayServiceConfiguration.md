---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExpressGatewayServiceConfiguration.html
---

# ExpressGatewayServiceConfiguration
<a name="API_ExpressGatewayServiceConfiguration"></a>

Represents a specific configuration revision of an Express service, containing all the settings and parameters for that revision.

## Contents
<a name="API_ExpressGatewayServiceConfiguration_Contents"></a>

 ** cpu **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-cpu"></a>
The CPU allocation for tasks in this service revision.
Type: String
Required: No

 ** cpuArchitecture **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-cpuArchitecture"></a>
The CPU architecture that the task runs on.
Valid values:
+  `X86_64` - The x86 64-bit architecture.
+  `ARM64` - The 64-bit ARM architecture.
Different service revisions can report different architectures. This value isn't returned when the service uses a customer-provided task definition that doesn't specify a CPU architecture.
Type: String
Valid Values: `X86_64 | ARM64`
Required: No

 ** createdAt **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-createdAt"></a>
The Unix timestamp for when this service revision was created.
Type: Timestamp
Required: No

 ** executionRoleArn **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-executionRoleArn"></a>
The ARN of the task execution role for the service revision.
Type: String
Required: No

 ** healthCheckPath **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-healthCheckPath"></a>
The health check path for this service revision.
Type: String
Required: No

 ** ingressPaths **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-ingressPaths"></a>
The entry point into this service revision.
Type: Array of [IngressPathSummary](API_IngressPathSummary.md) objects
Required: No

 ** memory **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-memory"></a>
The memory allocation for tasks in this service revision.
Type: String
Required: No

 ** networkConfiguration **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-networkConfiguration"></a>
The network configuration for tasks in this service revision.
Type: [ExpressGatewayServiceNetworkConfiguration](API_ExpressGatewayServiceNetworkConfiguration.md) object
Required: No

 ** primaryContainer **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-primaryContainer"></a>
The primary container configuration for this service revision.
Type: [ExpressGatewayContainer](API_ExpressGatewayContainer.md) object
Required: No

 ** scalingTarget **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-scalingTarget"></a>
The auto-scaling configuration for this service revision.
Type: [ExpressGatewayScalingTarget](API_ExpressGatewayScalingTarget.md) object
Required: No

 ** serviceRevisionArn **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-serviceRevisionArn"></a>
The ARN of the service revision.
Type: String
Required: No

 ** taskDefinitionArn **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-taskDefinitionArn"></a>
The ARN of the task definition used by this service revision. This is present for all Express services and reflects the task definition in use, whether managed by Amazon ECS or provided by the customer.
Type: String
Required: No

 ** taskRoleArn **   <a name="ECS-Type-ExpressGatewayServiceConfiguration-taskRoleArn"></a>
The ARN of the task role for the service revision.
Type: String
Required: No

## See Also
<a name="API_ExpressGatewayServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ExpressGatewayServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ExpressGatewayServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ExpressGatewayServiceConfiguration)

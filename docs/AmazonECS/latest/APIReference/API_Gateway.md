---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Gateway.html
---

# Gateway
<a name="API_Gateway"></a>

The details of a gateway, including its configuration, status, and the infrastructure settings for its type.

## Contents
<a name="API_Gateway_Contents"></a>

 ** accessType **   <a name="ECS-Type-Gateway-accessType"></a>
Specifies whether the gateway is publicly accessible (`PUBLIC`) or private (`PRIVATE`). The gateway derives this value from its scheme when you create the gateway, and the value is immutable.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: No

 ** configuration **   <a name="ECS-Type-Gateway-configuration"></a>
The type-specific configuration for the gateway.
Type: [DescribeGatewayConfiguration](API_DescribeGatewayConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** createdAt **   <a name="ECS-Type-Gateway-createdAt"></a>
The Unix timestamp for the time when the gateway was created.
Type: Timestamp
Required: No

 ** deletionProtection **   <a name="ECS-Type-Gateway-deletionProtection"></a>
Specifies whether deletion protection is enabled for the gateway.
Type: Boolean
Required: No

 ** failures **   <a name="ECS-Type-Gateway-failures"></a>
The per-resource failure details for asynchronous gateway processes, such as an `UpdateGateway` operation that couldn't update every load balancer.
Type: Array of [GatewayResourceFailure](API_GatewayResourceFailure.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** gatewayArn **   <a name="ECS-Type-Gateway-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String
Required: No

 ** infrastructureRoleArn **   <a name="ECS-Type-Gateway-infrastructureRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the gateway uses to manage infrastructure on your behalf.
Type: String
Required: No

 ** name **   <a name="ECS-Type-Gateway-name"></a>
The name of the gateway.
Type: String
Required: No

 ** propagateTags **   <a name="ECS-Type-Gateway-propagateTags"></a>
Specifies whether the gateway propagates its tags to the infrastructure it manages.
Type: String
Valid Values: `NONE | GATEWAY`
Required: No

 ** status **   <a name="ECS-Type-Gateway-status"></a>
The status of the gateway.
Type: String
Valid Values: `ACTIVE | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | DELETED`
Required: No

 ** statusReason **   <a name="ECS-Type-Gateway-statusReason"></a>
A human-readable explanation of the current status. This value is populated when the gateway is in a failure state, such as `UPDATE_FAILED`.
Type: String
Required: No

 ** tags **   <a name="ECS-Type-Gateway-tags"></a>
The metadata applied to the gateway. Each tag consists of a key and an optional value.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** updatedAt **   <a name="ECS-Type-Gateway-updatedAt"></a>
The Unix timestamp for the time when the gateway was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Gateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Gateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Gateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Gateway)

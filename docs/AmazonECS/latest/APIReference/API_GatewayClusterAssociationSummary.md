---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayClusterAssociationSummary.html
---

# GatewayClusterAssociationSummary
<a name="API_GatewayClusterAssociationSummary"></a>

A summary of an association between a gateway and a cluster.

## Contents
<a name="API_GatewayClusterAssociationSummary_Contents"></a>

 ** clusterArn **   <a name="ECS-Type-GatewayClusterAssociationSummary-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster.
Type: String
Required: No

 ** gatewayArn **   <a name="ECS-Type-GatewayClusterAssociationSummary-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String
Required: No

 ** status **   <a name="ECS-Type-GatewayClusterAssociationSummary-status"></a>
The status of the association.
Type: String
Valid Values: `ACTIVE | DISASSOCIATING | INACTIVE`
Required: No

## See Also
<a name="API_GatewayClusterAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayClusterAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayClusterAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayClusterAssociationSummary)

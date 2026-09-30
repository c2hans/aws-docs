---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_VpcLatticeAdvancedConfiguration.html
---

# VpcLatticeAdvancedConfiguration
<a name="API_VpcLatticeAdvancedConfiguration"></a>

The advanced settings for VPC Lattice used in blue/green deployments. Specify the alternate target group and listener rules required for traffic shifting during blue/green deployments. For more information, see [Required resources for Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-implementation.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_VpcLatticeAdvancedConfiguration_Contents"></a>

 ** alternateTargetGroupArn **   <a name="ECS-Type-VpcLatticeAdvancedConfiguration-alternateTargetGroupArn"></a>
The Amazon Resource Name (ARN) of the alternate target group associated with the VPC Lattice Configuration for Amazon ECS blue/green deployments.
Type: String
Required: No

 ** productionListenerRule **   <a name="ECS-Type-VpcLatticeAdvancedConfiguration-productionListenerRule"></a>
The Amazon Resource Name (ARN) that identifies the production listener rule or listener for routing production traffic.
Type: String
Required: No

 ** testListenerRule **   <a name="ECS-Type-VpcLatticeAdvancedConfiguration-testListenerRule"></a>
The Amazon Resource Name (ARN) that identifies the test listener rule or listener for routing test traffic.
Type: String
Required: No

## See Also
<a name="API_VpcLatticeAdvancedConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/VpcLatticeAdvancedConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/VpcLatticeAdvancedConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/VpcLatticeAdvancedConfiguration)

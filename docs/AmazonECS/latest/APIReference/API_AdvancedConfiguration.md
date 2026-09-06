---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_AdvancedConfiguration.html
---

# AdvancedConfiguration
<a name="API_AdvancedConfiguration"></a>

The advanced settings for a load balancer used in blue/green deployments. Specify the alternate target group, listener rules, and IAM role required for traffic shifting during blue/green deployments. For more information, see [Required resources for Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-implementation.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_AdvancedConfiguration_Contents"></a>

 ** alternateTargetGroupArn **   <a name="ECS-Type-AdvancedConfiguration-alternateTargetGroupArn"></a>
The Amazon Resource Name (ARN) of the alternate target group for Amazon ECS blue/green deployments.
Type: String
Required: No

 ** productionListenerRule **   <a name="ECS-Type-AdvancedConfiguration-productionListenerRule"></a>
The Amazon Resource Name (ARN) that that identifies the production listener rule (in the case of an Application Load Balancer) or listener (in the case for an Network Load Balancer) for routing production traffic.
Type: String
Required: No

 ** roleArn **   <a name="ECS-Type-AdvancedConfiguration-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon ECS permission to call the Elastic Load Balancing APIs for you.
Type: String
Required: No

 ** testListenerRule **   <a name="ECS-Type-AdvancedConfiguration-testListenerRule"></a>
The Amazon Resource Name (ARN) that identifies ) that identifies the test listener rule (in the case of an Application Load Balancer) or listener (in the case for an Network Load Balancer) for routing test traffic.
Type: String
Required: No

## See Also
<a name="API_AdvancedConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/AdvancedConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/AdvancedConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/AdvancedConfiguration)

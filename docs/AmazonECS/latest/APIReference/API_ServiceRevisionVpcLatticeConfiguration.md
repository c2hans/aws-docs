---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceRevisionVpcLatticeConfiguration.html
---

# ServiceRevisionVpcLatticeConfiguration
<a name="API_ServiceRevisionVpcLatticeConfiguration"></a>

The resolved VPC Lattice configuration for a service revision. This includes information about which target groups serve traffic and which listener rules direct traffic to them.

## Contents
<a name="API_ServiceRevisionVpcLatticeConfiguration_Contents"></a>

 ** productionListenerRule **   <a name="ECS-Type-ServiceRevisionVpcLatticeConfiguration-productionListenerRule"></a>
The Amazon Resource Name (ARN) of the production listener rule or listener that directs traffic to the target group associated with the service revision.
Type: String
Required: No

 ** targetGroupArn **   <a name="ECS-Type-ServiceRevisionVpcLatticeConfiguration-targetGroupArn"></a>
The Amazon Resource Name (ARN) of the target group associated with the service revision.
Type: String
Required: No

## See Also
<a name="API_ServiceRevisionVpcLatticeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceRevisionVpcLatticeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceRevisionVpcLatticeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceRevisionVpcLatticeConfiguration)

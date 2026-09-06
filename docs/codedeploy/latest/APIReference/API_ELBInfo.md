---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ELBInfo.html
---

# ELBInfo
<a name="API_ELBInfo"></a>

Information about a Classic Load Balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

## Contents
<a name="API_ELBInfo_Contents"></a>

 ** name **   <a name="CodeDeploy-Type-ELBInfo-name"></a>
For blue/green deployments, the name of the Classic Load Balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the Classic Load Balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.
Type: String
Required: No

## See Also
<a name="API_ELBInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ELBInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ELBInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ELBInfo)

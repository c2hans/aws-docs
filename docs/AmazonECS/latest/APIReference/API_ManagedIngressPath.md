---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedIngressPath.html
---

# ManagedIngressPath
<a name="API_ManagedIngressPath"></a>

The entry point into the Express service.

## Contents
<a name="API_ManagedIngressPath_Contents"></a>

 ** accessType **   <a name="ECS-Type-ManagedIngressPath-accessType"></a>
The type of access to the endpoint for the Express service.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: Yes

 ** endpoint **   <a name="ECS-Type-ManagedIngressPath-endpoint"></a>
The endpoint for access to the Express service.
Type: String
Required: Yes

 ** certificate **   <a name="ECS-Type-ManagedIngressPath-certificate"></a>
The ACM certificate for the Express service's domain.
Type: [ManagedCertificate](API_ManagedCertificate.md) object
Required: No

 ** listener **   <a name="ECS-Type-ManagedIngressPath-listener"></a>
The listeners associated with the Application Load Balancer.
Type: [ManagedListener](API_ManagedListener.md) object
Required: No

 ** loadBalancer **   <a name="ECS-Type-ManagedIngressPath-loadBalancer"></a>
The Application Load Balancer associated with the Express service.
Type: [ManagedLoadBalancer](API_ManagedLoadBalancer.md) object
Required: No

 ** loadBalancerSecurityGroups **   <a name="ECS-Type-ManagedIngressPath-loadBalancerSecurityGroups"></a>
The security groups associated with the Application Load Balancer.
Type: Array of [ManagedSecurityGroup](API_ManagedSecurityGroup.md) objects
Required: No

 ** rule **   <a name="ECS-Type-ManagedIngressPath-rule"></a>
The listener rules for the Application Load Balancer.
Type: [ManagedListenerRule](API_ManagedListenerRule.md) object
Required: No

 ** targetGroups **   <a name="ECS-Type-ManagedIngressPath-targetGroups"></a>
The target groups associated with the Application Load Balancer.
Type: Array of [ManagedTargetGroup](API_ManagedTargetGroup.md) objects
Required: No

## See Also
<a name="API_ManagedIngressPath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedIngressPath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedIngressPath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedIngressPath)

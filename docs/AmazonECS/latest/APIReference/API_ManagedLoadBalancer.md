---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedLoadBalancer.html
---

# ManagedLoadBalancer
<a name="API_ManagedLoadBalancer"></a>

The Application Load Balancer associated with the Express service.

## Contents
<a name="API_ManagedLoadBalancer_Contents"></a>

 ** scheme **   <a name="ECS-Type-ManagedLoadBalancer-scheme"></a>
The scheme of the load balancer. By default, the scheme of the load balancer is `internet-facing`.
Type: String
Required: Yes

 ** status **   <a name="ECS-Type-ManagedLoadBalancer-status"></a>
The status of the load balancer.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | DELETED | FAILED`
Required: Yes

 ** updatedAt **   <a name="ECS-Type-ManagedLoadBalancer-updatedAt"></a>
The Unix timestamp for when this load balancer was most recently updated.
Type: Timestamp
Required: Yes

 ** arn **   <a name="ECS-Type-ManagedLoadBalancer-arn"></a>
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: No

 ** securityGroupIds **   <a name="ECS-Type-ManagedLoadBalancer-securityGroupIds"></a>
The IDs of the security groups associated with the load balancer.
Type: Array of strings
Required: No

 ** statusReason **   <a name="ECS-Type-ManagedLoadBalancer-statusReason"></a>
Information about why the load balancer is in the current status.
Type: String
Required: No

 ** subnetIds **   <a name="ECS-Type-ManagedLoadBalancer-subnetIds"></a>
The IDs of the subnets associated with the load balancer.
Type: Array of strings
Required: No

## See Also
<a name="API_ManagedLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedLoadBalancer)

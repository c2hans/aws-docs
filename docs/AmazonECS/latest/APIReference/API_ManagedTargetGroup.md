---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedTargetGroup.html
---

# ManagedTargetGroup
<a name="API_ManagedTargetGroup"></a>

The target group associated with the Express service's Application Load Balancer. For more information about load balancer target groups, see [CreateTargetGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateTargetGroup.html) in the *Elastic Load Balancing API Reference*

## Contents
<a name="API_ManagedTargetGroup_Contents"></a>

 ** healthCheckPath **   <a name="ECS-Type-ManagedTargetGroup-healthCheckPath"></a>
The destination for health checks on the targets.
Type: String
Required: Yes

 ** healthCheckPort **   <a name="ECS-Type-ManagedTargetGroup-healthCheckPort"></a>
The port the load balancer uses when performing health checks on targets.
Type: Integer
Required: Yes

 ** port **   <a name="ECS-Type-ManagedTargetGroup-port"></a>
The port on which the targets receive traffic.
Type: Integer
Required: Yes

 ** status **   <a name="ECS-Type-ManagedTargetGroup-status"></a>
The status of the target group.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | DELETED | FAILED`
Required: Yes

 ** updatedAt **   <a name="ECS-Type-ManagedTargetGroup-updatedAt"></a>
The Unix timestamp for when the target group was last updated.
Type: Timestamp
Required: Yes

 ** arn **   <a name="ECS-Type-ManagedTargetGroup-arn"></a>
The Amazon Resource Name (ARN) of the target group.
Type: String
Required: No

 ** statusReason **   <a name="ECS-Type-ManagedTargetGroup-statusReason"></a>
Information about why the target group is in the current status.
Type: String
Required: No

## See Also
<a name="API_ManagedTargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedTargetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedTargetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedTargetGroup)

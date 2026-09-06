---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServiceLoadBalancersDetails.html
---

# AwsEcsServiceLoadBalancersDetails
<a name="API_AwsEcsServiceLoadBalancersDetails"></a>

Information about a load balancer that the service uses.

## Contents
<a name="API_AwsEcsServiceLoadBalancersDetails_Contents"></a>

 ** ContainerName **   <a name="securityhub-Type-AwsEcsServiceLoadBalancersDetails-ContainerName"></a>
The name of the container to associate with the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ContainerPort **   <a name="securityhub-Type-AwsEcsServiceLoadBalancersDetails-ContainerPort"></a>
The port on the container to associate with the load balancer. This port must correspond to a `containerPort` in the task definition the tasks in the service are using. For tasks that use the EC2 launch type, the container instance they are launched on must allow ingress traffic on the `hostPort` of the port mapping.
Type: Integer
Required: No

 ** LoadBalancerName **   <a name="securityhub-Type-AwsEcsServiceLoadBalancersDetails-LoadBalancerName"></a>
The name of the load balancer to associate with the Amazon ECS service or task set.
Only specified when using a Classic Load Balancer. For an Application Load Balancer or a Network Load Balancer, the load balancer name is omitted.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TargetGroupArn **   <a name="securityhub-Type-AwsEcsServiceLoadBalancersDetails-TargetGroupArn"></a>
The ARN of the Elastic Load Balancing target group or groups associated with a service or task set.
Only specified when using an Application Load Balancer or a Network Load Balancer. For a Classic Load Balancer, the target group ARN is omitted.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsServiceLoadBalancersDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServiceLoadBalancersDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServiceLoadBalancersDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServiceLoadBalancersDetails)

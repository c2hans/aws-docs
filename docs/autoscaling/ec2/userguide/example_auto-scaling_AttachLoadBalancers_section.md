---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_AttachLoadBalancers_section.html
---

# Use `AttachLoadBalancers` with a CLI
<a name="example_auto-scaling_AttachLoadBalancers_section"></a>

The following code examples show how to use `AttachLoadBalancers`.

------
#### [ CLI ]

**AWS CLI**
**To attach a Classic Load Balancer to an Auto Scaling group**
This example attaches the specified Classic Load Balancer to the specified Auto Scaling group.

```
aws autoscaling attach-load-balancers \
    --load-balancer-names {{my-load-balancer}} \
    --auto-scaling-group-name {{my-asg}}
```
This command produces no output.
For more information, see [Elastic Load Balancing and Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [AttachLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-load-balancers.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example attaches the specified load balancer to the specified Auto Scaling group.**

```
Add-ASLoadBalancer -LoadBalancerName my-lb -AutoScalingGroupName my-asg
```
+  For API details, see [AttachLoadBalancers](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example attaches the specified load balancer to the specified Auto Scaling group.**

```
Add-ASLoadBalancer -LoadBalancerName my-lb -AutoScalingGroupName my-asg
```
+  For API details, see [AttachLoadBalancers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

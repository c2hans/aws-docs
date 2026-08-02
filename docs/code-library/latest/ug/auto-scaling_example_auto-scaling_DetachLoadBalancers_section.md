---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DetachLoadBalancers_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DetachLoadBalancers` with a CLI
<a name="auto-scaling_example_auto-scaling_DetachLoadBalancers_section"></a>

The following code examples show how to use `DetachLoadBalancers`.

------
#### [ CLI ]

**AWS CLI**
**To detach a Classic Load Balancer from an Auto Scaling group**
This example detaches the specified Classic Load Balancer from the specified Auto Scaling group.

```
aws autoscaling detach-load-balancers \
    --load-balancer-names {{my-load-balancer}} \
    --auto-scaling-group-name {{my-asg}}
```
This command produces no output.
For more information, see [Attaching a load balancer to your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DetachLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/detach-load-balancers.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example detaches the specified load balancer from the specified Auto Scaling group.**

```
Dismount-ASLoadBalancer -LoadBalancerName my-lb -AutoScalingGroupName my-asg
```
+  For API details, see [DetachLoadBalancers](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example detaches the specified load balancer from the specified Auto Scaling group.**

```
Dismount-ASLoadBalancer -LoadBalancerName my-lb -AutoScalingGroupName my-asg
```
+  For API details, see [DetachLoadBalancers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

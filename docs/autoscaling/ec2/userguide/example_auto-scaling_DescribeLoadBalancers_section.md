---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeLoadBalancers_section.html
---

# Use `DescribeLoadBalancers` with a CLI
<a name="example_auto-scaling_DescribeLoadBalancers_section"></a>

The following code examples show how to use `DescribeLoadBalancers`.

------
#### [ CLI ]

**AWS CLI**
**To describe the Classic Load Balancers for an Auto Scaling group**
This example describes the Classic Load Balancers for the specified Auto Scaling group.

```
aws autoscaling describe-load-balancers \
    --auto-scaling-group-name {{my-asg}}
```
Output:

```
{
    "LoadBalancers": [
        {
            "State": "Added",
            "LoadBalancerName": "my-load-balancer"
        }
    ]
}
```
+  For API details, see [DescribeLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-load-balancers.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the load balancers for the specified Auto Scaling group.**

```
Get-ASLoadBalancer -AutoScalingGroupName my-asg
```
**Output:**

```
LoadBalancerName    State
----------------    -----
my-lb               Added
```
+  For API details, see [DescribeLoadBalancers](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the load balancers for the specified Auto Scaling group.**

```
Get-ASLoadBalancer -AutoScalingGroupName my-asg
```
**Output:**

```
LoadBalancerName    State
----------------    -----
my-lb               Added
```
+  For API details, see [DescribeLoadBalancers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

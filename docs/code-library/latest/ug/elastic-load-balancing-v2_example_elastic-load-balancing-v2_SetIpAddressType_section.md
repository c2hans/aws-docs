---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing-v2_example_elastic-load-balancing-v2_SetIpAddressType_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `SetIpAddressType` with a CLI
<a name="elastic-load-balancing-v2_example_elastic-load-balancing-v2_SetIpAddressType_section"></a>

The following code examples show how to use `SetIpAddressType`.

------
#### [ CLI ]

**AWS CLI**
**To set the address type of a load balancer**
This example sets the address type of the specified load balancer to `dualstack`. The load balancer subnets must have associated IPv6 CIDR blocks.
Command:

```
aws elbv2 set-ip-address-type --load-balancer-arn {{arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188}} --ip-address-type {{dualstack}}
```
Output:

```
{
    "IpAddressType": "dualstack"
}
```
+  For API details, see [SetIpAddressType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-ip-address-type.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example changes Load balancer IP address type from 'IPv4' to 'DualStack'.**

```
Set-ELB2IpAddressType -LoadBalancerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/test-alb/3651b4394dd9a24f' -IpAddressType dualstack
```
**Output:**

```
Value
-----
dualstack
```
+  For API details, see [SetIpAddressType](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example changes Load balancer IP address type from 'IPv4' to 'DualStack'.**

```
Set-ELB2IpAddressType -LoadBalancerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/test-alb/3651b4394dd9a24f' -IpAddressType dualstack
```
**Output:**

```
Value
-----
dualstack
```
+  For API details, see [SetIpAddressType](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

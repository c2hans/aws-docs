---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeLoadBalancerAttributes_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeLoadBalancerAttributes` with a CLI
<a name="elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeLoadBalancerAttributes_section"></a>

The following code examples show how to use `DescribeLoadBalancerAttributes`.

------
#### [ CLI ]

**AWS CLI**
**To describe load balancer attributes**
The following `describe-load-balancer-attributes` example displays the attributes of the specified load balancer.

```
aws elbv2 describe-load-balancer-attributes \
    --load-balancer-arn {{arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188}}
```
The following example output show the attributes for an Application Load Balancer.

```
{
    "Attributes": [
        {
            "Value": "false",
            "Key": "access_logs.s3.enabled"
        },
        {
            "Value": "",
            "Key": "access_logs.s3.bucket"
        },
        {
            "Value": "",
            "Key": "access_logs.s3.prefix"
        },
        {
            "Value": "60",
            "Key": "idle_timeout.timeout_seconds"
        },
        {
            "Value": "false",
            "Key": "deletion_protection.enabled"
        },
        {
            "Value": "true",
            "Key": "routing.http2.enabled"
        }
    ]
}
```
The following example output includes the attributes for a Network Load Balancer.

```
{
    "Attributes": [
        {
            "Value": "false",
            "Key": "access_logs.s3.enabled"
        },
        {
            "Value": "",
            "Key": "access_logs.s3.bucket"
        },
        {
            "Value": "",
            "Key": "access_logs.s3.prefix"
        },
        {
            "Value": "false",
            "Key": "deletion_protection.enabled"
        },
        {
            "Value": "false",
            "Key": "load_balancing.cross_zone.enabled"
        }
    ]
}
```
+  For API details, see [DescribeLoadBalancerAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-load-balancer-attributes.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This command describes the attributes of given Load balancer.**

```
Get-ELB2LoadBalancerAttribute -LoadBalancerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/test-elb/238d34ad8d94bc2e'
```
**Output:**

```
Key                               Value
---                               -----
access_logs.s3.enabled            false
load_balancing.cross_zone.enabled true
access_logs.s3.prefix
deletion_protection.enabled       false
access_logs.s3.bucket
```
+  For API details, see [DescribeLoadBalancerAttributes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This command describes the attributes of given Load balancer.**

```
Get-ELB2LoadBalancerAttribute -LoadBalancerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/test-elb/238d34ad8d94bc2e'
```
**Output:**

```
Key                               Value
---                               -----
access_logs.s3.enabled            false
load_balancing.cross_zone.enabled true
access_logs.s3.prefix
deletion_protection.enabled       false
access_logs.s3.bucket
```
+  For API details, see [DescribeLoadBalancerAttributes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

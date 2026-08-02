---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DisableAvailabilityZonesForLoadBalancer_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DisableAvailabilityZonesForLoadBalancer` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DisableAvailabilityZonesForLoadBalancer_section"></a>

The following code examples show how to use `DisableAvailabilityZonesForLoadBalancer`.

------
#### [ CLI ]

**AWS CLI**
**To disable Availability Zones for a load balancer**
This example removes the specified Availability Zone from the set of Availability Zones for the specified load balancer.
Command:

```
aws elb disable-availability-zones-for-load-balancer --load-balancer-name {{my-load-balancer}} --availability-zones {{us-west-2a}}
```
Output:

```
{
    "AvailabilityZones": [
        "us-west-2b"
    ]
}
```
+  For API details, see [DisableAvailabilityZonesForLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/disable-availability-zones-for-load-balancer.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the specified Availability Zone from the specified load balancer. The output includes the remaining Availability Zones.**

```
Disable-ELBAvailabilityZoneForLoadBalancer -LoadBalancerName my-load-balancer -AvailabilityZone us-west-2a
```
**Output:**

```
us-west-2b
```
+  For API details, see [DisableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the specified Availability Zone from the specified load balancer. The output includes the remaining Availability Zones.**

```
Disable-ELBAvailabilityZoneForLoadBalancer -LoadBalancerName my-load-balancer -AvailabilityZone us-west-2a
```
**Output:**

```
us-west-2b
```
+  For API details, see [DisableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

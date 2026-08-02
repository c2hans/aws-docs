---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_EnableAvailabilityZonesForLoadBalancer_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `EnableAvailabilityZonesForLoadBalancer` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_EnableAvailabilityZonesForLoadBalancer_section"></a>

The following code examples show how to use `EnableAvailabilityZonesForLoadBalancer`.

------
#### [ CLI ]

**AWS CLI**
**To enable Availability Zones for a load balancer**
This example adds the specified Availability Zone to the specified load balancer.
Command:

```
aws elb enable-availability-zones-for-load-balancer --load-balancer-name {{my-load-balancer}} --availability-zones {{us-west-2b}}
```
Output:

```
{
    "AvailabilityZones": [
        "us-west-2a",
        "us-west-2b"
    ]
}
```
+  For API details, see [EnableAvailabilityZonesForLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/enable-availability-zones-for-load-balancer.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds the specified Availability Zone to the specified load balancer. The output includes the complete list of Availability Zones.**

```
Enable-ELBAvailabilityZoneForLoadBalancer -LoadBalancerName my-load-balancer -AvailabilityZone us-west-2a
```
**Output:**

```
us-west-2a
us-west-2b
```
+  For API details, see [EnableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds the specified Availability Zone to the specified load balancer. The output includes the complete list of Availability Zones.**

```
Enable-ELBAvailabilityZoneForLoadBalancer -LoadBalancerName my-load-balancer -AvailabilityZone us-west-2a
```
**Output:**

```
us-west-2a
us-west-2b
```
+  For API details, see [EnableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

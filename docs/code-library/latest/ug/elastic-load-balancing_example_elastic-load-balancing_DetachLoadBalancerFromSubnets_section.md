---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DetachLoadBalancerFromSubnets_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DetachLoadBalancerFromSubnets` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DetachLoadBalancerFromSubnets_section"></a>

The following code examples show how to use `DetachLoadBalancerFromSubnets`.

------
#### [ CLI ]

**AWS CLI**
**To detach load balancers from subnets**
This example detaches the specified load balancer from the specified subnet.
Command:

```
aws elb detach-load-balancer-from-subnets --load-balancer-name {{my-load-balancer}} --subnets {{subnet-0ecac448}}
```
Output:

```
{
   "Subnets": [
       "subnet-15aaab61"
   ]
}
```
+  For API details, see [DetachLoadBalancerFromSubnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/detach-load-balancer-from-subnets.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the specified subnet from the set of subnets configured for the specified load balancer. The output includes the remaining subnets.**

```
Dismount-ELBLoadBalancerFromSubnet -LoadBalancerName my-load-balancer -Subnet subnet-12345678
```
**Output:**

```
subnet-87654321
```
+  For API details, see [DetachLoadBalancerFromSubnets](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the specified subnet from the set of subnets configured for the specified load balancer. The output includes the remaining subnets.**

```
Dismount-ELBLoadBalancerFromSubnet -LoadBalancerName my-load-balancer -Subnet subnet-12345678
```
**Output:**

```
subnet-87654321
```
+  For API details, see [DetachLoadBalancerFromSubnets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

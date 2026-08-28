---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_AttachLoadBalancerToSubnets_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AttachLoadBalancerToSubnets` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_AttachLoadBalancerToSubnets_section"></a>

The following code examples show how to use `AttachLoadBalancerToSubnets`.

------
#### [ CLI ]

**AWS CLI**
**To attach subnets to a load balancer**
This example adds the specified subnet to the set of configured subnets for the specified load balancer.
Command:

```
aws elb attach-load-balancer-to-subnets --load-balancer-name {{my-load-balancer}} --subnets {{subnet-0ecac448}}
```
Output:

```
{
   "Subnets": [
       "subnet-15aaab61",
       "subnet-0ecac448"
   ]
}
```
+  For API details, see [AttachLoadBalancerToSubnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/attach-load-balancer-to-subnets.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds the specified subnet to the set of subnets configured for the specified load balancer. The output includes the complete list of subnets.**

```
Add-ELBLoadBalancerToSubnet -LoadBalancerName my-load-balancer -Subnet subnet-12345678
```
**Output:**

```
subnet-12345678
subnet-87654321
```
+  For API details, see [AttachLoadBalancerToSubnets](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds the specified subnet to the set of subnets configured for the specified load balancer. The output includes the complete list of subnets.**

```
Add-ELBLoadBalancerToSubnet -LoadBalancerName my-load-balancer -Subnet subnet-12345678
```
**Output:**

```
subnet-12345678
subnet-87654321
```
+  For API details, see [AttachLoadBalancerToSubnets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

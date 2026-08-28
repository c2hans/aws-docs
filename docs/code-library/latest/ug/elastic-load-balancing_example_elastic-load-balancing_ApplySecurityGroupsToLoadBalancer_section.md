---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_ApplySecurityGroupsToLoadBalancer_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ApplySecurityGroupsToLoadBalancer` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_ApplySecurityGroupsToLoadBalancer_section"></a>

The following code examples show how to use `ApplySecurityGroupsToLoadBalancer`.

------
#### [ CLI ]

**AWS CLI**
**To associate a security group with a load balancer in a VPC**
This example associates a security group with the specified load balancer in a VPC.
Command:

```
aws elb apply-security-groups-to-load-balancer --load-balancer-name {{my-load-balancer}} --security-groups {{sg-fc448899}}
```
Output:

```
{
  "SecurityGroups": [
      "sg-fc448899"
  ]
}
```
+  For API details, see [ApplySecurityGroupsToLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/apply-security-groups-to-load-balancer.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example replaces the current security group for the specified load balancer with the specified security group.**

```
Join-ELBSecurityGroupToLoadBalancer -LoadBalancerName my-load-balancer -SecurityGroup sg-87654321
```
**Output:**

```
sg-87654321
```
**Example 2: To keep the current security group and specify an additional security group, specify both the existing and new security groups.**

```
Join-ELBSecurityGroupToLoadBalancer -LoadBalancerName my-load-balancer -SecurityGroup @("sg-12345678", "sg-87654321")
```
**Output:**

```
sg-12345678
sg-87654321
```
+  For API details, see [ApplySecurityGroupsToLoadBalancer](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example replaces the current security group for the specified load balancer with the specified security group.**

```
Join-ELBSecurityGroupToLoadBalancer -LoadBalancerName my-load-balancer -SecurityGroup sg-87654321
```
**Output:**

```
sg-87654321
```
**Example 2: To keep the current security group and specify an additional security group, specify both the existing and new security groups.**

```
Join-ELBSecurityGroupToLoadBalancer -LoadBalancerName my-load-balancer -SecurityGroup @("sg-12345678", "sg-87654321")
```
**Output:**

```
sg-12345678
sg-87654321
```
+  For API details, see [ApplySecurityGroupsToLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

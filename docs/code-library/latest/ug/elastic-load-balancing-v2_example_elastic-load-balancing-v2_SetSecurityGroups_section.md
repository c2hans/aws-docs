---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing-v2_example_elastic-load-balancing-v2_SetSecurityGroups_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `SetSecurityGroups` with a CLI
<a name="elastic-load-balancing-v2_example_elastic-load-balancing-v2_SetSecurityGroups_section"></a>

The following code examples show how to use `SetSecurityGroups`.

------
#### [ CLI ]

**AWS CLI**
**To associate a security group with a load balancer**
This example associates the specified security group with the specified load balancer.
Command:

```
aws elbv2 set-security-groups --load-balancer-arn {{arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188}} --security-groups {{sg-5943793c}}
```
Output:

```
{
  "SecurityGroupIds": [
      "sg-5943793c"
  ]
}
```
+  For API details, see [SetSecurityGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-security-groups.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds security group 'sg-07c3414abb8811cbd' to the specified Load balancer.**

```
Set-ELB2SecurityGroup -LoadBalancerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/test-alb/3651b4394dd9a24f' -SecurityGroup 'sg-07c3414abb8811cbd'
```
**Output:**

```
sg-07c3414abb8811cbd
```
+  For API details, see [SetSecurityGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds security group 'sg-07c3414abb8811cbd' to the specified Load balancer.**

```
Set-ELB2SecurityGroup -LoadBalancerArn 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/test-alb/3651b4394dd9a24f' -SecurityGroup 'sg-07c3414abb8811cbd'
```
**Output:**

```
sg-07c3414abb8811cbd
```
+  For API details, see [SetSecurityGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

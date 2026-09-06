---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DeleteLoadBalancer_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteLoadBalancer` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DeleteLoadBalancer_section"></a>

The following code examples show how to use `DeleteLoadBalancer`.

------
#### [ CLI ]

**AWS CLI**
**To delete a load balancer**
This example deletes the specified load balancer.
Command:

```
aws elb delete-load-balancer --load-balancer-name {{my-load-balancer}}
```
+  For API details, see [DeleteLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBLoadBalancer -LoadBalancerName my-load-balancer
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBLoadBalancer (DeleteLoadBalancer)" on Target "my-load-balancer".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteLoadBalancer](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBLoadBalancer -LoadBalancerName my-load-balancer
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBLoadBalancer (DeleteLoadBalancer)" on Target "my-load-balancer".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

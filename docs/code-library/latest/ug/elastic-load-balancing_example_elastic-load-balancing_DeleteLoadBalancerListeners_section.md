---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DeleteLoadBalancerListeners_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteLoadBalancerListeners` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DeleteLoadBalancerListeners_section"></a>

The following code examples show how to use `DeleteLoadBalancerListeners`.

------
#### [ CLI ]

**AWS CLI**
**To delete a listener from your load balancer**
This example deletes the listener for the specified port from the specified load balancer.
Command:

```
aws elb delete-load-balancer-listeners --load-balancer-name {{my-load-balancer}} --load-balancer-ports {{80}}
```
+  For API details, see [DeleteLoadBalancerListeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer-listeners.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the listener on port 80 for the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBLoadBalancerListener -LoadBalancerName my-load-balancer -LoadBalancerPort 80
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBLoadBalancerListener (DeleteLoadBalancerListeners)" on Target "80".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteLoadBalancerListeners](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the listener on port 80 for the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBLoadBalancerListener -LoadBalancerName my-load-balancer -LoadBalancerPort 80
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBLoadBalancerListener (DeleteLoadBalancerListeners)" on Target "80".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteLoadBalancerListeners](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

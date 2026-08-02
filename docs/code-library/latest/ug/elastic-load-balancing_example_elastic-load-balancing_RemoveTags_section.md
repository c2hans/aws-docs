---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_RemoveTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RemoveTags` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_RemoveTags_section"></a>

The following code examples show how to use `RemoveTags`.

------
#### [ CLI ]

**AWS CLI**
**To remove tags from a load balancer**
This example removes a tag from the specified load balancer.
Command:

```
aws elb remove-tags --load-balancer-name {{my-load-balancer}} --tags {{project}}
```
+  For API details, see [RemoveTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/remove-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the specified tag from the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-ELBResourceTag -LoadBalancerName my-load-balancer -Tag @{ Key="project" }
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-ELBResourceTag (RemoveTags)" on target "Amazon.ElasticLoadBalancing.Model.TagKeyOnly".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: With Powershell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.ElasticLoadBalancing.Model.TagKeyOnly
$tag.Key = "project"
Remove-ELBResourceTag -Tag $tag -Force
```
+  For API details, see [RemoveTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the specified tag from the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-ELBResourceTag -LoadBalancerName my-load-balancer -Tag @{ Key="project" }
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-ELBResourceTag (RemoveTags)" on target "Amazon.ElasticLoadBalancing.Model.TagKeyOnly".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: With Powershell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.ElasticLoadBalancing.Model.TagKeyOnly
$tag.Key = "project"
Remove-ELBResourceTag -Tag $tag -Force
```
+  For API details, see [RemoveTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

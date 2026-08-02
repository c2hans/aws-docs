---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_AddTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AddTags` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_AddTags_section"></a>

The following code examples show how to use `AddTags`.

------
#### [ CLI ]

**AWS CLI**
**To add a tag to a load balancer**
This example adds tags to the specified load balancer.
Command:

```
aws elb add-tags --load-balancer-name {{my-load-balancer}} --tags {{"Key=project,Value=lima"}} {{"Key=department,Value=digital-media"}}
```
+  For API details, see [AddTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/add-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds the specified tags to the specified load balancer. The syntax used by this example requires PowerShell version 3 or later.**

```
Add-ELBResourceTag -LoadBalancerName my-load-balancer -Tag @{ Key="project";Value="lima" },@{ Key="department";Value="digital-media" }
```
**Example 2: With PowerShell version 2, you must use New-Object to create a tag for the Tag parameter.**

```
$tag = New-Object Amazon.ElasticLoadBalancing.Model.Tag
$tag.Key = "project"
$tag.Value = "lima"
Add-ELBResourceTag -LoadBalancerName my-load-balancer -Tag $tag
```
+  For API details, see [AddTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds the specified tags to the specified load balancer. The syntax used by this example requires PowerShell version 3 or later.**

```
Add-ELBResourceTag -LoadBalancerName my-load-balancer -Tag @{ Key="project";Value="lima" },@{ Key="department";Value="digital-media" }
```
**Example 2: With PowerShell version 2, you must use New-Object to create a tag for the Tag parameter.**

```
$tag = New-Object Amazon.ElasticLoadBalancing.Model.Tag
$tag.Key = "project"
$tag.Value = "lima"
Add-ELBResourceTag -LoadBalancerName my-load-balancer -Tag $tag
```
+  For API details, see [AddTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

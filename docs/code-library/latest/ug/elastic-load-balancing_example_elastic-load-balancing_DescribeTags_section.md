---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DescribeTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeTags` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DescribeTags_section"></a>

The following code examples show how to use `DescribeTags`.

------
#### [ CLI ]

**AWS CLI**
**To describe the tags assigned to a load balancer**
This example describes the tags assigned to the specified load balancer.
Command:

```
aws elb describe-tags --load-balancer-name {{my-load-balancer}}
```
Output:

```
{
  "TagDescriptions": [
      {
          "Tags": [
              {
                  "Value": "lima",
                  "Key": "project"
              },
              {
                  "Value": "digital-media",
                  "Key": "department"
              }
          ],
          "LoadBalancerName": "my-load-balancer"
      }
  ]
}
```
+  For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the tags for the specified load balancers.**

```
Get-ELBResourceTag -LoadBalancerName @("my-load-balancer","my-internal-load-balancer")
```
**Output:**

```
LoadBalancerName             Tags
----------------             ----
my-load-balancer             {project, department}
my-internal-load-balancer    {project, department}
```
**Example 2: This example describes the tags for the specified load balancer.**

```
(Get-ELBResourceTag -LoadBalancerName my-load-balancer).Tags
```
**Output:**

```
Key           Value
---           -----
project       lima
department    digital-media
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the tags for the specified load balancers.**

```
Get-ELBResourceTag -LoadBalancerName @("my-load-balancer","my-internal-load-balancer")
```
**Output:**

```
LoadBalancerName             Tags
----------------             ----
my-load-balancer             {project, department}
my-internal-load-balancer    {project, department}
```
**Example 2: This example describes the tags for the specified load balancer.**

```
(Get-ELBResourceTag -LoadBalancerName my-load-balancer).Tags
```
**Output:**

```
Key           Value
---           -----
project       lima
department    digital-media
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

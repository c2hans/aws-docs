---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DescribePlacementGroups_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribePlacementGroups` with a CLI
<a name="ec2_example_ec2_DescribePlacementGroups_section"></a>

The following code examples show how to use `DescribePlacementGroups`.

------
#### [ CLI ]

**AWS CLI**
**To describe your placement groups**
This example command describes all of your placement groups.
Command:

```
aws ec2 describe-placement-groups
```
Output:

```
{
    "PlacementGroups": [
        {
            "GroupName": "my-cluster",
            "State": "available",
            "Strategy": "cluster"
        },
        ...
    ]
}
```
+  For API details, see [DescribePlacementGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-placement-groups.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the specified placement group.**

```
Get-EC2PlacementGroup -GroupName my-placement-group
```
**Output:**

```
GroupName             State        Strategy
---------             -----        --------
my-placement-group    available    cluster
```
+  For API details, see [DescribePlacementGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the specified placement group.**

```
Get-EC2PlacementGroup -GroupName my-placement-group
```
**Output:**

```
GroupName             State        Strategy
---------             -----        --------
my-placement-group    available    cluster
```
+  For API details, see [DescribePlacementGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

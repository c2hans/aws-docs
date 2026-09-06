---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_ListTagsForResource_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListTagsForResource` with a CLI
<a name="ssm_example_ssm_ListTagsForResource_section"></a>

The following code examples show how to use `ListTagsForResource`.

------
#### [ CLI ]

**AWS CLI**
**To list the tags applied to a patch baseline**
The following `list-tags-for-resource` example lists the tags for a patch baseline.

```
aws ssm list-tags-for-resource \
    --resource-type {{"PatchBaseline"}} \
    --resource-id {{"pb-0123456789abcdef0"}}
```
Output:

```
{
    "TagList": [
        {
            "Key": "Environment",
            "Value": "Production"
        },
        {
            "Key": "Region",
            "Value": "EMEA"
        }
    ]
}
```
For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.
+  For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-tags-for-resource.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the tags for a maintenance window.**

```
Get-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow"
```
**Output:**

```
Key   Value
---   -----
Stack Production
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the tags for a maintenance window.**

```
Get-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow"
```
**Output:**

```
Key   Value
---   -----
Stack Production
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

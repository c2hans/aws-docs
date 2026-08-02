---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_DescribeTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeTags` with a CLI
<a name="workspaces_example_workspaces_DescribeTags_section"></a>

The following code examples show how to use `DescribeTags`.

------
#### [ CLI ]

**AWS CLI**
**To describe the tags for a WorkSpace**
The following `describe-tags` example describes the tags for the specified WorkSpace.

```
aws workspaces describe-tags \
    --resource-id {{ws-dk1xzr417}}
```
Output:

```
{
    "TagList": [
        {
            "Key": "Department",
            "Value": "Finance"
        }
    ]
}
```
For more information, see [Tag WorkSpaces resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This Sample fetches tag for the given Workspace**

```
Get-WKSTag -WorkspaceId ws-w361s234r -Region us-west-2
```
**Output:**

```
Key         Value
---         -----
auto-delete no
purpose     Workbench
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This Sample fetches tag for the given Workspace**

```
Get-WKSTag -WorkspaceId ws-w361s234r -Region us-west-2
```
**Output:**

```
Key         Value
---         -----
auto-delete no
purpose     Workbench
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

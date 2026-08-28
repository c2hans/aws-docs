---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_DeleteTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteTags` with a CLI
<a name="workspaces_example_workspaces_DeleteTags_section"></a>

The following code examples show how to use `DeleteTags`.

------
#### [ CLI ]

**AWS CLI**
**To delete a tag from a WorkSpace**
The following `delete-tags` example deletes the specified tag from the specified WorkSpace.

```
aws workspaces delete-tags \
    --resource-id {{ws-dk1xzr417}} \
    --tag-keys {{Department}}
```
This command produces no output.
For more information, see [Tag WorkSpaces resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [DeleteTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This sample removes the tag associated with the Workspace**

```
Remove-WKSTag -ResourceId ws-w10b3abcd -TagKey "Type"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-WKSTag (DeleteTags)" on target "ws-w10b3abcd".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This sample removes the tag associated with the Workspace**

```
Remove-WKSTag -ResourceId ws-w10b3abcd -TagKey "Type"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-WKSTag (DeleteTags)" on target "ws-w10b3abcd".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

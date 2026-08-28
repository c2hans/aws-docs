---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_CreateTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateTags` with a CLI
<a name="workspaces_example_workspaces_CreateTags_section"></a>

The following code examples show how to use `CreateTags`.

------
#### [ CLI ]

**AWS CLI**
**To add tags to a WorkSpace**
The following `create-tags` example adds the specified tags to the specified WorkSpace.

```
aws workspaces create-tags \
    --resource-id {{ws-dk1xzr417}} \
    --tags {{Key=Department,Value=Finance}}
```
This command produces no output.
For more information, see [Tag WorkSpaces resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [CreateTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds a new tag to a workspace named `ws-wsname`. The tag has a key of "Name", and a key value of `AWS_Workspace`.**

```
$tag = New-Object Amazon.WorkSpaces.Model.Tag
$tag.Key = "Name"
$tag.Value = "AWS_Workspace"
New-WKSTag -Region us-west-2 -WorkspaceId ws-wsname -Tag $tag
```
**Example 2: This example adds multiple tags to a workspace named `ws-wsname`. One tag has a key of "Name" and a key value of `AWS_Workspace`; the other tag has a tag key of "Stage" and a key value of "Test".**

```
$tag = New-Object Amazon.WorkSpaces.Model.Tag
$tag.Key = "Name"
$tag.Value = "AWS_Workspace"

$tag2 = New-Object Amazon.WorkSpaces.Model.Tag
$tag2.Key = "Stage"
$tag2.Value = "Test"
New-WKSTag -Region us-west-2 -WorkspaceId ws-wsname -Tag $tag,$tag2
```
+  For API details, see [CreateTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds a new tag to a workspace named `ws-wsname`. The tag has a key of "Name", and a key value of `AWS_Workspace`.**

```
$tag = New-Object Amazon.WorkSpaces.Model.Tag
$tag.Key = "Name"
$tag.Value = "AWS_Workspace"
New-WKSTag -Region us-west-2 -WorkspaceId ws-wsname -Tag $tag
```
**Example 2: This example adds multiple tags to a workspace named `ws-wsname`. One tag has a key of "Name" and a key value of `AWS_Workspace`; the other tag has a tag key of "Stage" and a key value of "Test".**

```
$tag = New-Object Amazon.WorkSpaces.Model.Tag
$tag.Key = "Name"
$tag.Value = "AWS_Workspace"

$tag2 = New-Object Amazon.WorkSpaces.Model.Tag
$tag2.Key = "Stage"
$tag2.Value = "Test"
New-WKSTag -Region us-west-2 -WorkspaceId ws-wsname -Tag $tag,$tag2
```
+  For API details, see [CreateTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

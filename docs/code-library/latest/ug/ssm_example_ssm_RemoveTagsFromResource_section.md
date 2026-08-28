---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_RemoveTagsFromResource_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RemoveTagsFromResource` with a CLI
<a name="ssm_example_ssm_RemoveTagsFromResource_section"></a>

The following code examples show how to use `RemoveTagsFromResource`.

------
#### [ CLI ]

**AWS CLI**
**To remove a tag from a patch baseline**
The following `remove-tags-from-resource` example removes tags from a patch baseline.

```
aws ssm remove-tags-from-resource \
    --resource-type {{"PatchBaseline"}} \
    --resource-id {{"pb-0123456789abcdef0"}} \
    --tag-keys {{"Region"}}
```
This command produces no output.
For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.
+  For API details, see [RemoveTagsFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/remove-tags-from-resource.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes a tag from a maintenance window. There is no output if the command succeeds.**

```
Remove-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -TagKey "Production"
```
+  For API details, see [RemoveTagsFromResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes a tag from a maintenance window. There is no output if the command succeeds.**

```
Remove-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -TagKey "Production"
```
+  For API details, see [RemoveTagsFromResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

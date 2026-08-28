---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_DeletePatchBaseline_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeletePatchBaseline` with a CLI
<a name="ssm_example_ssm_DeletePatchBaseline_section"></a>

The following code examples show how to use `DeletePatchBaseline`.

------
#### [ CLI ]

**AWS CLI**
**To delete a patch baseline**
The following `delete-patch-baseline` example deletes the specified patch baseline.

```
aws ssm delete-patch-baseline \
    --baseline-id {{"pb-045f10b4f382baeda"}}
```
Output:

```
{
    "BaselineId": "pb-045f10b4f382baeda"
}
```
For more information, see [Update or Delete a Patch Baseline (Console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-baseline-update-or-delete.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [DeletePatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-patch-baseline.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes a patch baseline.**

```
Remove-SSMPatchBaseline -BaselineId "pb-045f10b4f382baeda"
```
**Output:**

```
pb-045f10b4f382baeda
```
+  For API details, see [DeletePatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes a patch baseline.**

```
Remove-SSMPatchBaseline -BaselineId "pb-045f10b4f382baeda"
```
**Output:**

```
pb-045f10b4f382baeda
```
+  For API details, see [DeletePatchBaseline](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

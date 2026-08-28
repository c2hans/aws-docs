---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeletePatchBaseline_section.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Use `DeletePatchBaseline` with a CLI
<a name="example_ssm_DeletePatchBaseline_section"></a>

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

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

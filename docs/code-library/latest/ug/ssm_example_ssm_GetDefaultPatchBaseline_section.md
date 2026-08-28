---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_GetDefaultPatchBaseline_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetDefaultPatchBaseline` with a CLI
<a name="ssm_example_ssm_GetDefaultPatchBaseline_section"></a>

The following code examples show how to use `GetDefaultPatchBaseline`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To display the default Windows patch baseline**
The following `get-default-patch-baseline` example retrieves details for the default patch baseline for Windows Server.

```
aws ssm get-default-patch-baseline
```
Output:

```
{
  "BaselineId": "pb-0713accee01612345",
  "OperatingSystem": "WINDOWS"
}
```
**Example 2: To display the default patch baseline for Amazon Linux**
The following `get-default-patch-baseline` example retrieves details for the default patch baseline for Amazon Linux.

```
aws ssm get-default-patch-baseline \
    --operating-system {{AMAZON_LINUX}}
```
Output:

```
{
    "BaselineId": "pb-047c6eb9c8fc12345",
    "OperatingSystem": "AMAZON_LINUX"
}
```
For more information, see About Predefined and Custom Patch Baselines <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baselines.html>\_\_ and [Set an Existing Patch Baseline as the Default](https://docs.aws.amazon.com/systems-manager/latest/userguide/set-default-patch-baseline.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [GetDefaultPatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-default-patch-baseline.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example displays the default patch baseline.**

```
Get-SSMDefaultPatchBaseline
```
**Output:**

```
arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966
```
+  For API details, see [GetDefaultPatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example displays the default patch baseline.**

```
Get-SSMDefaultPatchBaseline
```
**Output:**

```
arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966
```
+  For API details, see [GetDefaultPatchBaseline](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

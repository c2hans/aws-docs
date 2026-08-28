---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_DeleteParameter_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteParameter` with a CLI
<a name="ssm_example_ssm_DeleteParameter_section"></a>

The following code examples show how to use `DeleteParameter`.

------
#### [ CLI ]

**AWS CLI**
**To delete a parameter**
The following `delete-parameter` example deletes the specified single parameter.

```
aws ssm delete-parameter \
    --name {{"MyParameter"}}
```
This command produces no output.
For more information, see [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [DeleteParameter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameter.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes a parameter. There is no output if the command succeeds.**

```
Remove-SSMParameter -Name "helloWorld"
```
+  For API details, see [DeleteParameter](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes a parameter. There is no output if the command succeeds.**

```
Remove-SSMParameter -Name "helloWorld"
```
+  For API details, see [DeleteParameter](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

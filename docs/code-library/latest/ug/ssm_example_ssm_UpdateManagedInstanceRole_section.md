---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_UpdateManagedInstanceRole_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateManagedInstanceRole` with a CLI
<a name="ssm_example_ssm_UpdateManagedInstanceRole_section"></a>

The following code examples show how to use `UpdateManagedInstanceRole`.

------
#### [ CLI ]

**AWS CLI**
**To update the IAM role of a managed instance**
The following `update-managed-instance-role` example updates the IAM instance profile of a managed instance.

```
aws ssm update-managed-instance-role \
    --instance-id {{"mi-08ab247cdfEXAMPLE"}} \
    --iam-role {{"ExampleRole"}}
```
This command produces no output.
For more information, see [Step 4: Create an IAM Instance Profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [UpdateManagedInstanceRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-managed-instance-role.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example updates the role of a managed instance. There is no output if the command succeeds.**

```
Update-SSMManagedInstanceRole -InstanceId "mi-08ab247cdf1046573" -IamRole "AutomationRole"
```
+  For API details, see [UpdateManagedInstanceRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example updates the role of a managed instance. There is no output if the command succeeds.**

```
Update-SSMManagedInstanceRole -InstanceId "mi-08ab247cdf1046573" -IamRole "AutomationRole"
```
+  For API details, see [UpdateManagedInstanceRole](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

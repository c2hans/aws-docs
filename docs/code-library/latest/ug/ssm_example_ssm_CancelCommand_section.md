---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_CancelCommand_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CancelCommand` with a CLI
<a name="ssm_example_ssm_CancelCommand_section"></a>

The following code examples show how to use `CancelCommand`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To cancel a command for all instances**
The following `cancel-command` example attempts to cancel the specified command that is already running for all instances.

```
aws ssm cancel-command \
    --command-id {{"662add3d-5831-4a10-b64a-f2ff3EXAMPLE"}}
```
This command produces no output.
**Example 2: To cancel a command for specific instances**
The following `cancel-command` example attempts to cancel a command for the specified instance only.

```
aws ssm cancel-command \
    --command-id {{"662add3d-5831-4a10-b64a-f2ff3EXAMPLE"}}
    --instance-ids {{"i-02573cafcfEXAMPLE"}}
```
This command produces no output.
For more information, see [Tagging Systems Manager Parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-tag.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [CancelCommand](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-command.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example attempts to cancel a command. There is no output if the operation succeeds.**

```
Stop-SSMCommand -CommandId "9ded293e-e792-4440-8e3e-7b8ec5feaa38"
```
+  For API details, see [CancelCommand](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example attempts to cancel a command. There is no output if the operation succeeds.**

```
Stop-SSMCommand -CommandId "9ded293e-e792-4440-8e3e-7b8ec5feaa38"
```
+  For API details, see [CancelCommand](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

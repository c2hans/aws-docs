---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_DeregisterManagedInstance_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeregisterManagedInstance` with a CLI
<a name="ssm_example_ssm_DeregisterManagedInstance_section"></a>

The following code examples show how to use `DeregisterManagedInstance`.

------
#### [ CLI ]

**AWS CLI**
**To deregister a managed instance**
The following `deregister-managed-instance` example deregisters the specified managed instance.

```
aws ssm deregister-managed-instance \
    --instance-id '{{mi-08ab247cdfEXAMPLE}}'
```
This command produces no output.
For more information, see [Deregistering managed nodes in a hybrid and multicloud environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-deregister-hybrid-nodes.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [DeregisterManagedInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-managed-instance.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deregisters a managed instance. There is no output if the command succeeds.**

```
Unregister-SSMManagedInstance -InstanceId "mi-08ab247cdf1046573"
```
+  For API details, see [DeregisterManagedInstance](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deregisters a managed instance. There is no output if the command succeeds.**

```
Unregister-SSMManagedInstance -InstanceId "mi-08ab247cdf1046573"
```
+  For API details, see [DeregisterManagedInstance](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

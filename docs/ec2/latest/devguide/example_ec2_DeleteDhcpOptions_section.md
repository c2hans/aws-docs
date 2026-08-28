---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DeleteDhcpOptions_section.html
---

# Use `DeleteDhcpOptions` with a CLI
<a name="example_ec2_DeleteDhcpOptions_section"></a>

The following code examples show how to use `DeleteDhcpOptions`.

------
#### [ CLI ]

**AWS CLI**
**To delete a DHCP options set**
This example deletes the specified DHCP options set. If the command succeeds, no output is returned.
Command:

```
aws ec2 delete-dhcp-options --dhcp-options-id {{dopt-d9070ebb}}
```
+  For API details, see [DeleteDhcpOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-dhcp-options.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified DHCP options set. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2DhcpOption (DeleteDhcpOptions)" on Target "dopt-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteDhcpOptions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified DHCP options set. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2DhcpOption (DeleteDhcpOptions)" on Target "dopt-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteDhcpOptions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

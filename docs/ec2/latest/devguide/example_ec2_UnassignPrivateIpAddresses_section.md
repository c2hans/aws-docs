---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_UnassignPrivateIpAddresses_section.html
---

# Use `UnassignPrivateIpAddresses` with a CLI
<a name="example_ec2_UnassignPrivateIpAddresses_section"></a>

The following code examples show how to use `UnassignPrivateIpAddresses`.

------
#### [ CLI ]

**AWS CLI**
**To unassign a secondary private IP address from a network interface**
This example unassigns the specified private IP address from the specified network interface. If the command succeeds, no output is returned.
Command:

```
aws ec2 unassign-private-ip-addresses --network-interface-id {{eni-e5aa89a3}} --private-ip-addresses {{10.0.0.82}}
```
+  For API details, see [UnassignPrivateIpAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unassign-private-ip-addresses.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example unassigns the specified private IP address from the specified network interface.**

```
Unregister-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82
```
+  For API details, see [UnassignPrivateIpAddresses](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example unassigns the specified private IP address from the specified network interface.**

```
Unregister-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82
```
+  For API details, see [UnassignPrivateIpAddresses](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

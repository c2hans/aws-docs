---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_CreateVpnConnectionRoute_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateVpnConnectionRoute` with a CLI
<a name="ec2_example_ec2_CreateVpnConnectionRoute_section"></a>

The following code examples show how to use `CreateVpnConnectionRoute`.

------
#### [ CLI ]

**AWS CLI**
**To create a static route for a VPN connection**
This example creates a static route for the specified VPN connection. If the command succeeds, no output is returned.
Command:

```
aws ec2 create-vpn-connection-route --vpn-connection-id {{vpn-40f41529}} --destination-cidr-block {{11.12.0.0/16}}
```
+  For API details, see [CreateVpnConnectionRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection-route.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates the specified static route for the specified VPN connection.**

```
New-EC2VpnConnectionRoute -VpnConnectionId vpn-12345678 -DestinationCidrBlock 11.12.0.0/16
```
+  For API details, see [CreateVpnConnectionRoute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates the specified static route for the specified VPN connection.**

```
New-EC2VpnConnectionRoute -VpnConnectionId vpn-12345678 -DestinationCidrBlock 11.12.0.0/16
```
+  For API details, see [CreateVpnConnectionRoute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

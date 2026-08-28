---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_CreateVpnGateway_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateVpnGateway` with a CLI
<a name="ec2_example_ec2_CreateVpnGateway_section"></a>

The following code examples show how to use `CreateVpnGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Get started with dedicated network connections](ec2_example_directconnect_GettingStarted_051_section.md)

------
#### [ CLI ]

**AWS CLI**
**To create a virtual private gateway**
This example creates a virtual private gateway.
Command:

```
aws ec2 create-vpn-gateway --type {{ipsec.1}}
```
Output:

```
{
    "VpnGateway": {
        "AmazonSideAsn": 64512,
        "State": "available",
        "Type": "ipsec.1",
        "VpnGatewayId": "vgw-9a4cacf3",
        "VpcAttachments": []
    }
}
```
**To create a virtual private gateway with a specific Amazon-side ASN**
This example creates a virtual private gateway and specifies the Autonomous System Number (ASN) for the Amazon side of the BGP session.
Command:

```
aws ec2 create-vpn-gateway --type {{ipsec.1}} --amazon-side-asn {{65001}}
```
Output:

```
{
    "VpnGateway": {
        "AmazonSideAsn": 65001,
        "State": "available",
        "Type": "ipsec.1",
        "VpnGatewayId": "vgw-9a4cacf3",
        "VpcAttachments": []
    }
}
```
+  For API details, see [CreateVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-gateway.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates the specified virtual private gateway.**

```
New-EC2VpnGateway -Type ipsec.1
```
**Output:**

```
AvailabilityZone :
State            : available
Tags             : {}
Type             : ipsec.1
VpcAttachments   : {}
VpnGatewayId     : vgw-1a2b3c4d
```
+  For API details, see [CreateVpnGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates the specified virtual private gateway.**

```
New-EC2VpnGateway -Type ipsec.1
```
**Output:**

```
AvailabilityZone :
State            : available
Tags             : {}
Type             : ipsec.1
VpcAttachments   : {}
VpnGatewayId     : vgw-1a2b3c4d
```
+  For API details, see [CreateVpnGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

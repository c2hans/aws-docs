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
The following `create-vpn-connection-route` example creates a static route for the specified VPN connection.

```
aws ec2 create-vpn-connection-route \
    --vpn-connection-id {{vpn-40f41529}} \
    --destination-cidr-block {{11.12.0.0/16}}
```
This command produces no output.
For more information, see [AWS Site-to-Site VPN routing options](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNRoutingTypes.html) in the *AWS Site-to-Site VPN User Guide*.
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

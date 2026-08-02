---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DetachVpnGateway_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DetachVpnGateway` with a CLI
<a name="ec2_example_ec2_DetachVpnGateway_section"></a>

The following code examples show how to use `DetachVpnGateway`.

------
#### [ CLI ]

**AWS CLI**
**To detach a virtual private gateway from your VPC**
This example detaches the specified virtual private gateway from the specified VPC. If the command succeeds, no output is returned.
Command:

```
aws ec2 detach-vpn-gateway --vpn-gateway-id {{vgw-9a4cacf3}} --vpc-id {{vpc-a01106c2}}
```
+  For API details, see [DetachVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-vpn-gateway.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example detaches the specified virtual private gateway from the specified VPC.**

```
Dismount-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678
```
+  For API details, see [DetachVpnGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example detaches the specified virtual private gateway from the specified VPC.**

```
Dismount-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678
```
+  For API details, see [DetachVpnGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

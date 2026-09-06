---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_AttachVpnGateway_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AttachVpnGateway` with a CLI
<a name="ec2_example_ec2_AttachVpnGateway_section"></a>

The following code examples show how to use `AttachVpnGateway`.

------
#### [ CLI ]

**AWS CLI**
**To attach a virtual private gateway to your VPC**
The following `attach-vpn-gateway` example attaches the specified virtual private gateway to the specified VPC.

```
aws ec2 attach-vpn-gateway \
    --vpn-gateway-id {{vgw-9a4cacf3}} \
    --vpc-id {{vpc-a01106c2}}
```
Output:

```
{
    "VpcAttachment": {
        "State": "attaching",
        "VpcId": "vpc-a01106c2"
    }
}
```
+  For API details, see [AttachVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-vpn-gateway.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example attaches the specified virtual private gateway to the specified VPC.**

```
Add-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678
```
**Output:**

```
State        VpcId
-----        -----
attaching    vpc-12345678
```
+  For API details, see [AttachVpnGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example attaches the specified virtual private gateway to the specified VPC.**

```
Add-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678
```
**Output:**

```
State        VpcId
-----        -----
attaching    vpc-12345678
```
+  For API details, see [AttachVpnGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

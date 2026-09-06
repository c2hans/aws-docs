---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_UnassignPrivateIpAddresses_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UnassignPrivateIpAddresses` with a CLI
<a name="ec2_example_ec2_UnassignPrivateIpAddresses_section"></a>

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

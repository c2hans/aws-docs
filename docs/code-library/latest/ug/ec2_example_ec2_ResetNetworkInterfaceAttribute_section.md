---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ResetNetworkInterfaceAttribute_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ResetNetworkInterfaceAttribute` with a CLI
<a name="ec2_example_ec2_ResetNetworkInterfaceAttribute_section"></a>

The following code examples show how to use `ResetNetworkInterfaceAttribute`.

------
#### [ CLI ]

**AWS CLI**
**To reset a network interface attribute**
The following `reset-network-interface-attribute` example resets the value of the source/destination checking attribute to `true`.

```
aws ec2 reset-network-interface-attribute \
    --network-interface-id {{eni-686ea200}} \
    --source-dest-check {{sourceDestCheck}}
```
This command produces no output.
+  For API details, see [ResetNetworkInterfaceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-network-interface-attribute.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example resets source/destination checking for the specified network interface.**

```
Reset-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -SourceDestCheck
```
+  For API details, see [ResetNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example resets source/destination checking for the specified network interface.**

```
Reset-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -SourceDestCheck
```
+  For API details, see [ResetNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

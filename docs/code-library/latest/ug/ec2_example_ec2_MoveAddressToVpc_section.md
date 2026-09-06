---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_MoveAddressToVpc_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `MoveAddressToVpc` with a CLI
<a name="ec2_example_ec2_MoveAddressToVpc_section"></a>

The following code examples show how to use `MoveAddressToVpc`.

------
#### [ CLI ]

**AWS CLI**
**To move an address to EC2-VPC**
This example moves Elastic IP address 54.123.4.56 to the EC2-VPC platform.
Command:

```
aws ec2 move-address-to-vpc --public-ip {{54.123.4.56}}
```
Output:

```
{
  "Status": "MoveInProgress"
}
```
+  For API details, see [MoveAddressToVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/move-address-to-vpc.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example moves an EC2 instance with a public IP address of 12.345.67.89 to the EC2-VPC platform in the US East (Northern Virginia) region.**

```
Move-EC2AddressToVpc -PublicIp 12.345.67.89 -Region us-east-1
```
**Example 2: This example pipes the results of a Get-EC2Instance command to the Move-EC2AddressToVpc cmdlet. The Get-EC2Instance command gets an instance that is specified by instance ID, then returns the public IP address property of the instance.**

```
(Get-EC2Instance -Instance i-12345678).Instances.PublicIpAddress | Move-EC2AddressToVpc
```
+  For API details, see [MoveAddressToVpc](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example moves an EC2 instance with a public IP address of 12.345.67.89 to the EC2-VPC platform in the US East (Northern Virginia) region.**

```
Move-EC2AddressToVpc -PublicIp 12.345.67.89 -Region us-east-1
```
**Example 2: This example pipes the results of a Get-EC2Instance command to the Move-EC2AddressToVpc cmdlet. The Get-EC2Instance command gets an instance that is specified by instance ID, then returns the public IP address property of the instance.**

```
(Get-EC2Instance -Instance i-12345678).Instances.PublicIpAddress | Move-EC2AddressToVpc
```
+  For API details, see [MoveAddressToVpc](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

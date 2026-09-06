---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ConfirmProductInstance_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ConfirmProductInstance` with a CLI
<a name="ec2_example_ec2_ConfirmProductInstance_section"></a>

The following code examples show how to use `ConfirmProductInstance`.

------
#### [ CLI ]

**AWS CLI**
**To confirm the product instance**
This example determines whether the specified product code is associated with the specified instance.
Command:

```
aws ec2 confirm-product-instance --product-code {{774F4FF8}} --instance-id {{i-1234567890abcdef0}}
```
Output:

```
{
  "OwnerId": "123456789012"
}
```
+  For API details, see [ConfirmProductInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/confirm-product-instance.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example determines whether the specified product code is associated with the specified instance.**

```
Confirm-EC2ProductInstance -ProductCode 774F4FF8 -InstanceId i-12345678
```
+  For API details, see [ConfirmProductInstance](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example determines whether the specified product code is associated with the specified instance.**

```
Confirm-EC2ProductInstance -ProductCode 774F4FF8 -InstanceId i-12345678
```
+  For API details, see [ConfirmProductInstance](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

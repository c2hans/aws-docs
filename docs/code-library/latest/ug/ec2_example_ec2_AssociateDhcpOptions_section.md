---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_AssociateDhcpOptions_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AssociateDhcpOptions` with a CLI
<a name="ec2_example_ec2_AssociateDhcpOptions_section"></a>

The following code examples show how to use `AssociateDhcpOptions`.

------
#### [ CLI ]

**AWS CLI**
**To associate a DHCP options set with your VPC**
This example associates the specified DHCP options set with the specified VPC. If the command succeeds, no output is returned.
Command:

```
aws ec2 associate-dhcp-options --dhcp-options-id {{dopt-d9070ebb}} --vpc-id {{vpc-a01106c2}}
```
**To associate the default DHCP options set with your VPC**
This example associates the default DHCP options set with the specified VPC. If the command succeeds, no output is returned.
Command:

```
aws ec2 associate-dhcp-options --dhcp-options-id {{default}} --vpc-id {{vpc-a01106c2}}
```
+  For API details, see [AssociateDhcpOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-dhcp-options.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example associates the specified DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d -VpcId vpc-12345678
```
**Example 2: This example associates the default DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId default -VpcId vpc-12345678
```
+  For API details, see [AssociateDhcpOptions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example associates the specified DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d -VpcId vpc-12345678
```
**Example 2: This example associates the default DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId default -VpcId vpc-12345678
```
+  For API details, see [AssociateDhcpOptions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

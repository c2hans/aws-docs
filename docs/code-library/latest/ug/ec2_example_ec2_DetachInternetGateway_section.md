---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DetachInternetGateway_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DetachInternetGateway` with a CLI
<a name="ec2_example_ec2_DetachInternetGateway_section"></a>

The following code examples show how to use `DetachInternetGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Create a basic virtual private network](ec2_example_vpc_GettingStartedCLI_section.md)
+  [Getting started with graph databases](ec2_example_ec2_GettingStarted_064_section.md)
+  [Virtual private network with private servers](ec2_example_vpc_GettingStartedPrivate_section.md)

------
#### [ CLI ]

**AWS CLI**
**To detach an internet gateway from your VPC**
The following `detach-internet-gateway` example detaches the specified internet gateway from the specific VPC.

```
aws ec2 detach-internet-gateway \
    --internet-gateway-id {{igw-0d0fb496b3EXAMPLE}} \
    --vpc-id {{vpc-0a60eb65b4EXAMPLE}}
```
This command produces no output.
For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.
+  For API details, see [DetachInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-internet-gateway.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example detaches the specified Internet gateway from the specified VPC.**

```
Dismount-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678
```
+  For API details, see [DetachInternetGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example detaches the specified Internet gateway from the specified VPC.**

```
Dismount-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678
```
+  For API details, see [DetachInternetGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

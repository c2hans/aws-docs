---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeInternetGateways_section.html
---

# Use `DescribeInternetGateways` with a CLI
<a name="example_ec2_DescribeInternetGateways_section"></a>

The following code examples show how to use `DescribeInternetGateways`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Create a basic virtual private network](example_vpc_GettingStartedCLI_section.md)

------
#### [ CLI ]

**AWS CLI**
**To describe an internet gateway**
The following `describe-internet-gateways` example describes the specified internet gateway.

```
aws ec2 describe-internet-gateways \
    --internet-gateway-ids {{igw-0d0fb496b3EXAMPLE}}
```
Output:

```
{
    "InternetGateways": [
        {
            "Attachments": [
                {
                    "State": "available",
                    "VpcId": "vpc-0a60eb65b4EXAMPLE"
                }
            ],
            "InternetGatewayId": "igw-0d0fb496b3EXAMPLE",
            "OwnerId": "123456789012",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "my-igw"
                }
            ]
        }
    ]
}
```
For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.
+  For API details, see [DescribeInternetGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-internet-gateways.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the specified Internet gateway.**

```
Get-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d
```
**Output:**

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
```
**Example 2: This example describes all your Internet gateways.**

```
Get-EC2InternetGateway
```
**Output:**

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
{}                igw-2a3b4c5d          {}
```
+  For API details, see [DescribeInternetGateways](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the specified Internet gateway.**

```
Get-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d
```
**Output:**

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
```
**Example 2: This example describes all your Internet gateways.**

```
Get-EC2InternetGateway
```
**Output:**

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
{}                igw-2a3b4c5d          {}
```
+  For API details, see [DescribeInternetGateways](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

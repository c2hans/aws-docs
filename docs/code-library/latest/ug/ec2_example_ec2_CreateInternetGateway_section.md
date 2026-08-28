---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_CreateInternetGateway_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateInternetGateway` with a CLI
<a name="ec2_example_ec2_CreateInternetGateway_section"></a>

The following code examples show how to use `CreateInternetGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Create a basic virtual private network](ec2_example_vpc_GettingStartedCLI_section.md)
+  [Getting started with graph databases](ec2_example_ec2_GettingStarted_064_section.md)
+  [Virtual private network with private servers](ec2_example_vpc_GettingStartedPrivate_section.md)

------
#### [ CLI ]

**AWS CLI**
**To create an internet gateway**
The following `create-internet-gateway` example creates an internet gateway with the tag `Name=my-igw`.

```
aws ec2 create-internet-gateway \
    --tag-specifications {{ResourceType=internet-gateway,Tags=[{Key=Name,Value=my-igw}]}}
```
Output:

```
{
    "InternetGateway": {
        "Attachments": [],
        "InternetGatewayId": "igw-0d0fb496b3994d755",
        "OwnerId": "123456789012",
        "Tags": [
            {
                "Key": "Name",
                "Value": "my-igw"
            }
        ]
    }
}
```
For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.
+  For API details, see [CreateInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates an Internet gateway.**

```
New-EC2InternetGateway
```
**Output:**

```
Attachments    InternetGatewayId    Tags
-----------    -----------------    ----
{}             igw-1a2b3c4d         {}
```
+  For API details, see [CreateInternetGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates an Internet gateway.**

```
New-EC2InternetGateway
```
**Output:**

```
Attachments    InternetGatewayId    Tags
-----------    -----------------    ----
{}             igw-1a2b3c4d         {}
```
+  For API details, see [CreateInternetGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

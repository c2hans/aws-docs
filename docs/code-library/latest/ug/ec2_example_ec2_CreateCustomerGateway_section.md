---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_CreateCustomerGateway_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateCustomerGateway` with a CLI
<a name="ec2_example_ec2_CreateCustomerGateway_section"></a>

The following code examples show how to use `CreateCustomerGateway`.

------
#### [ CLI ]

**AWS CLI**
**To create a customer gateway**
This example creates a customer gateway with the specified IP address for its outside interface.
Command:

```
aws ec2 create-customer-gateway --type {{ipsec.1}} --public-ip {{12.1.2.3}} --bgp-asn {{65534}}
```
Output:

```
{
    "CustomerGateway": {
        "CustomerGatewayId": "cgw-0e11f167",
        "IpAddress": "12.1.2.3",
        "State": "available",
        "Type": "ipsec.1",
        "BgpAsn": "65534"
    }
}
```
+  For API details, see [CreateCustomerGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-customer-gateway.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates the specified customer gateway.**

```
New-EC2CustomerGateway -Type ipsec.1 -PublicIp 203.0.113.12 -BgpAsn 65534
```
**Output:**

```
BgpAsn            : 65534
CustomerGatewayId : cgw-1a2b3c4d
IpAddress         : 203.0.113.12
State             : available
Tags              : {}
Type              : ipsec.1
```
+  For API details, see [CreateCustomerGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates the specified customer gateway.**

```
New-EC2CustomerGateway -Type ipsec.1 -PublicIp 203.0.113.12 -BgpAsn 65534
```
**Output:**

```
BgpAsn            : 65534
CustomerGatewayId : cgw-1a2b3c4d
IpAddress         : 203.0.113.12
State             : available
Tags              : {}
Type              : ipsec.1
```
+  For API details, see [CreateCustomerGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

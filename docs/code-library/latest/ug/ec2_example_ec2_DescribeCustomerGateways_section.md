---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DescribeCustomerGateways_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeCustomerGateways` with a CLI
<a name="ec2_example_ec2_DescribeCustomerGateways_section"></a>

The following code examples show how to use `DescribeCustomerGateways`.

------
#### [ CLI ]

**AWS CLI**
**To describe your customer gateways**
This example describes your customer gateways.
Command:

```
aws ec2 describe-customer-gateways
```
Output:

```
{
    "CustomerGateways": [
        {
            "CustomerGatewayId": "cgw-b4dc3961",
            "IpAddress": "203.0.113.12",
            "State": "available",
            "Type": "ipsec.1",
            "BgpAsn": "65000"
        },
        {
            "CustomerGatewayId": "cgw-0e11f167",
            "IpAddress": "12.1.2.3",
            "State": "available",
            "Type": "ipsec.1",
            "BgpAsn": "65534"
        }
    ]
}
```
**To describe a specific customer gateway**
This example describes the specified customer gateway.
Command:

```
aws ec2 describe-customer-gateways --customer-gateway-ids {{cgw-0e11f167}}
```
Output:

```
{
    "CustomerGateways": [
        {
            "CustomerGatewayId": "cgw-0e11f167",
            "IpAddress": "12.1.2.3",
            "State": "available",
            "Type": "ipsec.1",
            "BgpAsn": "65534"
        }
    ]
}
```
+  For API details, see [DescribeCustomerGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-customer-gateways.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the specified customer gateway.**

```
Get-EC2CustomerGateway -CustomerGatewayId cgw-1a2b3c4d
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
**Example 2: This example describes any customer gateway whose state is either pending or available.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "pending", "available" )

Get-EC2CustomerGateway -Filter $filter
```
**Example 3: This example describes all your customer gateways.**

```
Get-EC2CustomerGateway
```
+  For API details, see [DescribeCustomerGateways](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the specified customer gateway.**

```
Get-EC2CustomerGateway -CustomerGatewayId cgw-1a2b3c4d
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
**Example 2: This example describes any customer gateway whose state is either pending or available.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "pending", "available" )

Get-EC2CustomerGateway -Filter $filter
```
**Example 3: This example describes all your customer gateways.**

```
Get-EC2CustomerGateway
```
+  For API details, see [DescribeCustomerGateways](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

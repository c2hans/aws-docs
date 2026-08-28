---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_AcceptVpcPeeringConnection_section.html
---

# Use `AcceptVpcPeeringConnection` with a CLI
<a name="example_ec2_AcceptVpcPeeringConnection_section"></a>

The following code examples show how to use `AcceptVpcPeeringConnection`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Working with network peering connections](example_ec2_GettingStarted_015_section.md)

------
#### [ CLI ]

**AWS CLI**
**To accept a VPC peering connection**
This example accepts the specified VPC peering connection request.
Command:

```
aws ec2 accept-vpc-peering-connection --vpc-peering-connection-id {{pcx-1a2b3c4d}}
```
Output:

```
{
  "VpcPeeringConnection": {
    "Status": {
      "Message": "Provisioning",
      "Code": "provisioning"
    },
    "Tags": [],
    "AccepterVpcInfo": {
      "OwnerId": "444455556666",
      "VpcId": "vpc-44455566",
      "CidrBlock": "10.0.1.0/28"
    },
    "VpcPeeringConnectionId": "pcx-1a2b3c4d",
    "RequesterVpcInfo": {
      "OwnerId": "444455556666",
      "VpcId": "vpc-111abc45",
      "CidrBlock": "10.0.0.0/28"
    }
  }
}
```
+  For API details, see [AcceptVpcPeeringConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-vpc-peering-connection.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example approves the requested VpcPeeringConnectionId pcx-1dfad234b56ff78be**

```
Approve-EC2VpcPeeringConnection -VpcPeeringConnectionId pcx-1dfad234b56ff78be
```
**Output:**

```
AccepterVpcInfo        : Amazon.EC2.Model.VpcPeeringConnectionVpcInfo
ExpirationTime         : 1/1/0001 12:00:00 AM
RequesterVpcInfo       : Amazon.EC2.Model.VpcPeeringConnectionVpcInfo
Status                 : Amazon.EC2.Model.VpcPeeringConnectionStateReason
Tags                   : {}
VpcPeeringConnectionId : pcx-1dfad234b56ff78be
```
+  For API details, see [AcceptVpcPeeringConnection](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example approves the requested VpcPeeringConnectionId pcx-1dfad234b56ff78be**

```
Approve-EC2VpcPeeringConnection -VpcPeeringConnectionId pcx-1dfad234b56ff78be
```
**Output:**

```
AccepterVpcInfo        : Amazon.EC2.Model.VpcPeeringConnectionVpcInfo
ExpirationTime         : 1/1/0001 12:00:00 AM
RequesterVpcInfo       : Amazon.EC2.Model.VpcPeeringConnectionVpcInfo
Status                 : Amazon.EC2.Model.VpcPeeringConnectionStateReason
Tags                   : {}
VpcPeeringConnectionId : pcx-1dfad234b56ff78be
```
+  For API details, see [AcceptVpcPeeringConnection](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

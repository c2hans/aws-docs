---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DisassociateRouteTable_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DisassociateRouteTable` with a CLI
<a name="ec2_example_ec2_DisassociateRouteTable_section"></a>

The following code examples show how to use `DisassociateRouteTable`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Create a basic virtual private network](ec2_example_vpc_GettingStartedCLI_section.md)
+  [Working with network peering connections](ec2_example_ec2_GettingStarted_015_section.md)

------
#### [ CLI ]

**AWS CLI**
**To disassociate a route table**
This example disassociates the specified route table from the specified subnet. If the command succeeds, no output is returned.
Command:

```
aws ec2 disassociate-route-table --association-id {{rtbassoc-781d0d1a}}
```
+  For API details, see [DisassociateRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-route-table.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the specified association between a route table and a subnet.**

```
Unregister-EC2RouteTable -AssociationId rtbassoc-1a2b3c4d
```
+  For API details, see [DisassociateRouteTable](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the specified association between a route table and a subnet.**

```
Unregister-EC2RouteTable -AssociationId rtbassoc-1a2b3c4d
```
+  For API details, see [DisassociateRouteTable](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

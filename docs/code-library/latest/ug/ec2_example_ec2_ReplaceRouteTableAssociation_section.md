---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ReplaceRouteTableAssociation_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ReplaceRouteTableAssociation` with a CLI
<a name="ec2_example_ec2_ReplaceRouteTableAssociation_section"></a>

The following code examples show how to use `ReplaceRouteTableAssociation`.

------
#### [ CLI ]

**AWS CLI**
**To replace the route table associated with a subnet**
This example associates the specified route table with the subnet for the specified route table association.
Command:

```
aws ec2 replace-route-table-association --association-id {{rtbassoc-781d0d1a}} --route-table-id {{rtb-22574640}}
```
Output:

```
{
    "NewAssociationId": "rtbassoc-3a1f0f58"
}
```
+  For API details, see [ReplaceRouteTableAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-route-table-association.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example associates the specified route table with the subnet for the specified route table association.**

```
Set-EC2RouteTableAssociation -RouteTableId rtb-1a2b3c4d -AssociationId rtbassoc-12345678
```
**Output:**

```
rtbassoc-87654321
```
+  For API details, see [ReplaceRouteTableAssociation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example associates the specified route table with the subnet for the specified route table association.**

```
Set-EC2RouteTableAssociation -RouteTableId rtb-1a2b3c4d -AssociationId rtbassoc-12345678
```
**Output:**

```
rtbassoc-87654321
```
+  For API details, see [ReplaceRouteTableAssociation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

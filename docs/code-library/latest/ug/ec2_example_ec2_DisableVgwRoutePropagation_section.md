---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DisableVgwRoutePropagation_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DisableVgwRoutePropagation` with a CLI
<a name="ec2_example_ec2_DisableVgwRoutePropagation_section"></a>

The following code examples show how to use `DisableVgwRoutePropagation`.

------
#### [ CLI ]

**AWS CLI**
**To disable route propagation**
This example disables the specified virtual private gateway from propagating static routes to the specified route table. If the command succeeds, no output is returned.
Command:

```
aws ec2 disable-vgw-route-propagation --route-table-id {{rtb-22574640}} --gateway-id {{vgw-9a4cacf3}}
```
+  For API details, see [DisableVgwRoutePropagation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vgw-route-propagation.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example disables the VGW from automatically propagating routes to the specified routing table.**

```
Disable-EC2VgwRoutePropagation -RouteTableId rtb-12345678 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [DisableVgwRoutePropagation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example disables the VGW from automatically propagating routes to the specified routing table.**

```
Disable-EC2VgwRoutePropagation -RouteTableId rtb-12345678 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [DisableVgwRoutePropagation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

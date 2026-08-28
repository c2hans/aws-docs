---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-sg-updates-update.html
---

# Update AWS Transit Gateway security group inbound rules
<a name="tgw-sg-updates-update"></a>

You can update any of the inbound security group rules associated with a transit gateway. You can update security group rules using either the Amazon VPC Console console or by using the command-line or API. For more information about security group referencing, see [Security group referencing](tgw-vpc-attachments.md#vpc-attachment-security).

**To update your security group rules using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**.

1. Select the security group, and choose **Actions**, **Edit inbound rules** to modify the inbound rules.

1. To add a rule, choose **Add rule** and specify the type, protocol, and port range. For **Source** (inbound rule), enter the ID of the security group in the VPC connected to the transit gateway.
**Note**
Security groups in a VPC connected to the transit gateway are not automatically displayed.

1. To edit an existing rule, change its values (for example, the source or the description).

1. To delete a rule, choose **Delete** next to the rule.

1. Choose **Save rules**.

**To update inbound rules using the command line**
+ [authorize-security-group-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-security-group-ingress.html) (AWS CLI)
+ [Grant-EC2SecurityGroupIngress](https://docs.aws.amazon.com/powershell/latest/reference/items/Grant-EC2SecurityGroupIngress.html) (AWS Tools for Windows PowerShell)
+ [Revoke-EC2SecurityGroupIngress](https://docs.aws.amazon.com/powershell/latest/reference/items/Revoke-EC2SecurityGroupIngress.html) (AWS Tools for Windows PowerShell)
+ [revoke-security-group-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/revoke-security-group-ingress.html) (AWS CLI)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

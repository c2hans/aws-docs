---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tgw-attachment.html
---

# Transit gateway route table attachments in AWS Cloud WAN
<a name="cloudwan-tgw-attachment"></a>

Transit gateway route tables contain the rules that determine how your network traffic is routed between your VPCs and VPNs. A transit gateway route table can be added as an attachment type in your AWS Cloud WAN core network. You can create a transit gateway route table attachment through either the console or by using the command line or API.

Before creating the attachment you must first have created your transit gateway route table.
+  For more information about transit gateway route tables, see [Routing](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html#tgw-routing-overview) in the *AWS Transit Gateway User Guide*.
+ For the steps to create a transit gateway route table, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) in the *AWS Transit Gateway User Guide*.

**Topics**
+ [Create a transit gateway route table attachment](cloudwan-tgw-attachment-add.md)
+ [View or edit a transit gateway route table attachment](cloudwan-attachments-viewing-editing-rtb.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

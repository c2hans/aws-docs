---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-shared-attachments.html
---

# Shared attachments in AWS Cloud WAN
<a name="cloudwan-shared-attachments"></a>

You can share attachments on any of your shared core networks. For more information on sharing core networks, see [Shared AWS Cloud WAN core network](cloudwan-share-network.md).

 When a core network owner shares their core network with your account, you are then able to create new VPC, transit gateway route table, or Direct Connect gateway attachments for the shared core network. You can also view the current attachments or delete an attachment from the shared core network.

**Note**
A shared core network currently supports only VPC, transit gateway route table, and Direct Connect gateway attachments.

**Topics**
+ [Create a shared VPC attachment](cloudwan-vpc-share-create.md)
+ [Create a shared transit gateway route table attachment](cloudwan-tgw-share.md)
+ [Create a shared Direct Connect gateway attachment](cloudwan-dx-share.md)
+ [View shared attachments](cloudwan-shared-view.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

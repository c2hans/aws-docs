---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-global-network-delete.html
---

# Delete an AWS Cloud WAN global network
<a name="cloudwan-global-network-delete"></a>

Delete a Cloud WAN global network if you no longer need that network. Deleting a global can't be undone.

Before you delete a global network, you must first delete any core networks that are associated with it. For more information on deleting core networks, see [Delete an AWS Cloud WAN core network](cloudwan-core-network-delete.md).

**To delete a global network**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. Choose the **Details** tab.

1. On the **Details** page, choose **Delete**, and then confirm that you are deleting the global network.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

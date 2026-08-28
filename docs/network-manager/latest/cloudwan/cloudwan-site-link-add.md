---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-site-link-add.html
---

# Create a link for a site in an AWS Cloud WAN global network
<a name="cloudwan-site-link-add"></a>

Create a link that can be used to associate a device with a site.

**To add a link**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Sites**.

1. Choose the link for the site **ID** that you want to add a link to, and then choose the **Links** tab.
**Note**
Choose the link. Do not select the check box.

1. Choose the **Links** tab, and then choose **Create link**.

1. For **Name** and **Description**, enter a name and description for the link.

1. For **Upload speed (Mbps)**, enter the upload speed in Mbps.

1.  For **Download speed (Mbps)**, enter the download speed in Mbps.

1. (Optional) For **Provider**, enter the name of the service provider.

1. (Optional) For **Type**, enter the type of link, for example, **broadband**.

1. (Optional) Under **Additional settings**, add one or more **Key** and **Value** **Tags** to help further identify this link.

1. Choose **Create link**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
